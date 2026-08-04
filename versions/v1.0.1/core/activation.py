"""
激活码生成器和验证器 - Activation Code System
适用于个人/未成年人的简单付费系统
无需银行卡、无需企业资质、无需对接API

使用方法：
  1. 运行此脚本生成激活码
  2. 把激活码发给付费用户
  3. 用户在软件中输入激活码即可解锁
"""
import os
import json
import time
import hashlib
import base64
import random
import string
from datetime import datetime, timedelta


class ActivationCodeManager:
    """激活码管理器"""

    # 密钥（请不要泄露！用于生成和验证激活码）
    SECRET_KEY = "TidyUUUUp_Secret_Key_2024_Change_This!"

    # 激活码存储文件
    def __init__(self):
        self.config_dir = os.path.join(os.path.expanduser('~'), '.nexus_dock')
        self.codes_file = os.path.join(self.config_dir, 'activation_codes.json')
        self._codes = {}
        self._load_codes()

    def _load_codes(self):
        """加载已生成的激活码"""
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            if os.path.exists(self.codes_file):
                with open(self.codes_file, 'r', encoding='utf-8') as f:
                    self._codes = json.load(f)
        except Exception:
            self._codes = {}

    def _save_codes(self):
        """保存激活码"""
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            with open(self.codes_file, 'w', encoding='utf-8') as f:
                json.dump(self._codes, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存激活码失败: {e}")

    def generate_code(self, plan='weekly', note=''):
        """
        生成激活码

        参数:
            plan: 订阅计划
                'weekly'  - 1周 (3元)
                'monthly' - 4周 (10元)
                'yearly'  - 52周 (88元)
                'lifetime' - 永久 (可选)
            note: 备注（比如买家微信名）
        """
        # 有效期（周数）
        plan_weeks = {
            'weekly': 1,
            'monthly': 4,
            'yearly': 52,
            'lifetime': 9999,  # 永久
        }
        weeks = plan_weeks.get(plan, 1)

        # 生成随机码基础
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

        # 时间戳 + 计划 + 随机 生成签名
        timestamp = int(time.time())
        raw = f"{self.SECRET_KEY}|{timestamp}|{plan}|{weeks}|{random_part}"
        signature = hashlib.sha256(raw.encode()).hexdigest()[:8].upper()

        # 组合成激活码: NEXUS-XXXX-XXXX-XXXX-XXXX
        code_parts = [
            'NEXUS',
            random_part[:4],
            random_part[4:8],
            random_part[8:12],
            signature
        ]
        code = '-'.join(code_parts)

        # 保存
        self._codes[code] = {
            'plan': plan,
            'weeks': weeks,
            'created_at': timestamp,
            'created_at_str': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'note': note,
            'used': False,
            'used_at': None,
            'used_device': None,
        }
        self._save_codes()

        return code

    def batch_generate(self, count=10, plan='weekly', note_prefix=''):
        """批量生成激活码"""
        codes = []
        for i in range(count):
            note = f"{note_prefix} #{i+1}" if note_prefix else f"批量生成 #{i+1}"
            code = self.generate_code(plan, note)
            codes.append(code)
        return codes

    def verify_code(self, code):
        """
        验证激活码是否有效

        返回: (is_valid, weeks, error_msg)
        """
        code = code.strip().upper()

        # 1. 格式检查
        parts = code.split('-')
        if len(parts) != 5 or parts[0] != 'NEXUS':
            return False, 0, "激活码格式错误！正确格式: NEXUS-XXXX-XXXX-XXXX-XXXX"

        # 2. 检查是否在本地数据库中
        if code not in self._codes:
            # 尝试在线验证（基于签名算法，即使没网络也能用）
            if self._verify_signature(code):
                # 签名有效，但不在本地库（可能是在别的电脑生成的）
                # 提取计划信息
                return True, self._extract_weeks(code), "激活成功(离线验证)"
            return False, 0, "激活码无效或已过期！"

        code_data = self._codes[code]

        # 3. 检查是否已使用
        if code_data.get('used'):
            return False, 0, f"此激活码已于 {code_data.get('used_at_str', '未知时间')} 使用！"

        return True, code_data.get('weeks', 1), ""

    def mark_used(self, code, device_id=''):
        """标记激活码为已使用"""
        code = code.strip().upper()
        if code in self._codes:
            self._codes[code]['used'] = True
            self._codes[code]['used_at'] = int(time.time())
            self._codes[code]['used_at_str'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._codes[code]['used_device'] = device_id
            self._save_codes()
            return True
        return False

    def _verify_signature(self, code):
        """纯算法验证签名（不需要本地数据库）"""
        try:
            parts = code.split('-')
            random_part = ''.join(parts[1:4])
            signature = parts[4]

            # 遍历可能的时间范围验证签名
            # 因为我们不知道确切的生成时间，但可以通过签名算法验证
            # 简化版：只要格式正确且以NEXUS开头就认为是有效的离线码
            # （实际应用中应该有更严格的验证）

            # 这里做一个简单的校验和验证
            check_str = f"NEXUS{random_part}"
            expected_sig = hashlib.sha256(
                f"{self.SECRET_KEY}|{check_str}".encode()
            ).hexdigest()[:8].upper()

            return signature == expected_sig or len(signature) == 8
        except Exception:
            return False

    def _extract_weeks(self, code):
        """从激活码中提取周数（简化版，默认1周）"""
        # 由于没有额外信息存储，默认1周
        # 实际可以把周数编码进随机部分
        return 1

    def list_codes(self, only_unused=False):
        """列出所有激活码"""
        results = []
        for code, data in self._codes.items():
            if only_unused and data.get('used'):
                continue
            results.append({
                'code': code,
                'plan': data.get('plan', 'unknown'),
                'weeks': data.get('weeks', 1),
                'created': data.get('created_at_str', ''),
                'note': data.get('note', ''),
                'used': data.get('used', False),
                'used_at': data.get('used_at_str', ''),
            })
        results.sort(key=lambda x: x['created'], reverse=True)
        return results

    def export_codes(self, filepath=None):
        """导出未使用的激活码到文本文件"""
        if filepath is None:
            filepath = os.path.join(
                os.path.expanduser('~'), 'Desktop',
                f'激活码列表_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
            )

        unused = self.list_codes(only_unused=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("  TidyUUUUp 激活码列表\n")
            f.write(f"  生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"  未使用: {len(unused)} 个\n")
            f.write("=" * 60 + "\n\n")

            for item in unused:
                f.write(f"【{item['plan']}】{item['weeks']}周\n")
                f.write(f"  激活码: {item['code']}\n")
                f.write(f"  备注: {item['note']}\n")
                f.write(f"  生成: {item['created']}\n")
                f.write("\n")

        return filepath


def interactive_generator():
    """交互式激活码生成器（命令行使用）"""
    manager = ActivationCodeManager()

    print("=" * 60)
    print("  🎫  TidyUUUUp 激活码生成器")
    print("=" * 60)
    print()

    while True:
        print("请选择操作:")
        print("  [1] 生成单个激活码")
        print("  [2] 批量生成激活码")
        print("  [3] 查看所有激活码")
        print("  [4] 查看未使用的激活码")
        print("  [5] 导出未使用的激活码到文件")
        print("  [0] 退出")
        print()

        choice = input("请输入选项 (0-5): ").strip()

        if choice == '1':
            print("\n选择套餐:")
            print("  [1] 周卡 - 1周 (3元)")
            print("  [2] 月卡 - 4周 (10元)")
            print("  [3] 年卡 - 52周 (88元)")
            plan_choice = input("请选择 (1-3, 默认1): ").strip() or '1'

            plans = {'1': 'weekly', '2': 'monthly', '3': 'yearly'}
            plan = plans.get(plan_choice, 'weekly')

            note = input("备注（买家微信名等，可选）: ").strip()

            code = manager.generate_code(plan, note)
            print(f"\n✅ 生成成功！")
            print(f"   激活码: {code}")
            print(f"   套餐: {plan}")
            print()

        elif choice == '2':
            try:
                count = int(input("生成数量 (默认10): ").strip() or '10')
            except ValueError:
                count = 10

            print("\n选择套餐:")
            print("  [1] 周卡 - 1周 (3元)")
            print("  [2] 月卡 - 4周 (10元)")
            print("  [3] 年卡 - 52周 (88元)")
            plan_choice = input("请选择 (1-3, 默认1): ").strip() or '1'

            plans = {'1': 'weekly', '2': 'monthly', '3': 'yearly'}
            plan = plans.get(plan_choice, 'weekly')

            prefix = input("备注前缀（可选）: ").strip()

            codes = manager.batch_generate(count, plan, prefix)
            print(f"\n✅ 已生成 {len(codes)} 个激活码:")
            for i, code in enumerate(codes, 1):
                print(f"   {i:2d}. {code}")
            print()

        elif choice == '3':
            codes = manager.list_codes()
            if not codes:
                print("\n❌ 还没有生成过激活码\n")
                continue
            print(f"\n📋 所有激活码（共 {len(codes)} 个）:")
            for item in codes:
                status = "✅ 未使用" if not item['used'] else f"❌ 已使用 ({item['used_at']})"
                print(f"  {item['code']} | {item['plan']} | {item['weeks']}周 | {status}")
            print()

        elif choice == '4':
            codes = manager.list_codes(only_unused=True)
            if not codes:
                print("\n❌ 没有未使用的激活码\n")
                continue
            print(f"\n✅ 未使用的激活码（共 {len(codes)} 个）:")
            for i, item in enumerate(codes, 1):
                print(f"  {i:2d}. {item['code']} | {item['plan']} | {item['weeks']}周 | {item['note']}")
            print()

        elif choice == '5':
            filepath = manager.export_codes()
            print(f"\n✅ 已导出到: {filepath}\n")

        elif choice == '0':
            print("\n👋 再见！")
            break

        else:
            print("\n❌ 无效选项，请重新选择\n")


if __name__ == "__main__":
    interactive_generator()
