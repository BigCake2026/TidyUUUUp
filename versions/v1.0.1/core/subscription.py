"""
订阅管理器 - Subscription Manager
7天免费试用 + 按周订阅（3元/周）
支持通过浏览器打开支付页面接入API
"""
import os
import json
import time
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtCore import QObject, pyqtSignal


class SubscriptionManager(QObject):
    """订阅管理器"""

    status_changed = pyqtSignal(str)  # trial / active / expired
    trial_days_remaining = pyqtSignal(int)

    # 价格配置
    PRICE_WEEKLY = 3.0       # 3元/周
    PRICE_MONTHLY = 10.0     # 10元/月 (优惠)
    PRICE_YEARLY = 88.0      # 88元/年 (超值)

    TRIAL_DAYS = 7           # 7天免费试用

    def __init__(self):
        super().__init__()
        self.config_dir = os.path.join(os.path.expanduser('~'), '.nexus_dock')
        self.license_file = os.path.join(self.config_dir, 'license.dat')
        self._license_data = None
        self._load_license()

    def _load_license(self):
        """加载许可证数据"""
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            if os.path.exists(self.license_file):
                with open(self.license_file, 'r', encoding='utf-8') as f:
                    encoded = f.read().strip()
                    decoded = base64.b64decode(encoded).decode('utf-8')
                    self._license_data = json.loads(decoded)
                    return
        except Exception:
            pass

        # 没有有效许可证，创建试用期
        self._license_data = {
            'status': 'trial',
            'trial_start': datetime.now().timestamp(),
            'subscription_end': None,
            'payment_history': [],
            'device_id': self._get_device_id(),
        }
        self._save_license()

    def _save_license(self):
        """保存许可证数据（简单加密）"""
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            data_str = json.dumps(self._license_data, ensure_ascii=False)
            encoded = base64.b64encode(data_str.encode('utf-8')).decode('utf-8')
            with open(self.license_file, 'w', encoding='utf-8') as f:
                f.write(encoded)
        except Exception as e:
            print(f"保存许可证失败: {e}")

    def _get_device_id(self):
        """获取设备唯一标识"""
        try:
            import platform
            info = f"{platform.node()}-{platform.processor()}-{platform.machine()}"
            return hashlib.md5(info.encode()).hexdigest()[:16]
        except Exception:
            return 'unknown-' + str(int(time.time()))

    def get_status(self):
        """获取当前状态（永久激活）"""
        return 'active'

    def get_trial_days_remaining(self):
        """获取试用剩余天数"""
        if self._license_data.get('status') != 'trial':
            return 0
        start = self._license_data.get('trial_start', time.time())
        elapsed = time.time() - start
        remaining = self.TRIAL_DAYS - (elapsed / 86400)
        return max(0, int(remaining + 1))

    def get_subscription_end_date(self):
        """获取订阅到期日期"""
        sub_end = self._license_data.get('subscription_end')
        if sub_end:
            return datetime.fromtimestamp(sub_end).strftime('%Y-%m-%d')
        return None

    def get_subscription_days_remaining(self):
        """获取订阅剩余天数"""
        sub_end = self._license_data.get('subscription_end')
        if sub_end:
            remaining = sub_end - time.time()
            return max(0, int(remaining / 86400) + 1)
        return 0

    def is_feature_available(self, feature=None):
        """检查某个功能是否可用（全部功能永久免费）"""
        return True

    def activate_subscription(self, weeks=1):
        """激活订阅（本地模拟，实际需要支付验证）"""
        current_end = self._license_data.get('subscription_end', time.time())
        if current_end < time.time():
            current_end = time.time()

        new_end = current_end + (weeks * 7 * 86400)
        self._license_data['subscription_end'] = new_end
        self._license_data['status'] = 'active'

        # 记录支付历史
        self._license_data['payment_history'].append({
            'time': datetime.now().timestamp(),
            'amount': weeks * self.PRICE_WEEKLY,
            'plan': f'{weeks}周',
            'status': 'completed'
        })

        self._save_license()
        self.status_changed.emit('active')
        return True

    def extend_trial(self, days=3):
        """延长试用期（用于促销等）"""
        if self._license_data.get('status') == 'trial':
            start = self._license_data.get('trial_start', time.time())
            self._license_data['trial_start'] = start - (days * 86400)
            self._save_license()
            return True
        return False

    def reset_trial(self):
        """重置试用期（仅用于测试）"""
        self._license_data = {
            'status': 'trial',
            'trial_start': datetime.now().timestamp(),
            'subscription_end': None,
            'payment_history': [],
            'device_id': self._get_device_id(),
        }
        self._save_license()
        self.status_changed.emit('trial')
        return True

    def get_info(self):
        """获取完整的订阅信息"""
        status = self.get_status()
        return {
            'status': status,
            'trial_days': self.get_trial_days_remaining(),
            'subscription_end': self.get_subscription_end_date(),
            'subscription_days': self.get_subscription_days_remaining(),
            'prices': {
                'weekly': self.PRICE_WEEKLY,
                'monthly': self.PRICE_MONTHLY,
                'yearly': self.PRICE_YEARLY,
            },
            'trial_total_days': self.TRIAL_DAYS,
        }

    def verify_payment(self, order_id):
        """
        验证支付（模拟）
        实际应用中应该调用微信/支付宝支付验证API
        """
        # 这里是模拟验证，实际项目需要接入真实支付SDK
        # 只要order_id不为空就认为支付成功
        if order_id and len(order_id) > 4:
            return True
        return False

    def get_payment_qr_info(self):
        """获取收款码信息（预留位置，等用户提供收款码后填充）"""
        return {
            'wechat': {
                'name': '微信支付',
                'amount': self.PRICE_WEEKLY,
                'description': '订阅1周（3元）',
                'qr_image_path': None,  # 用户提供收款码后填入
            },
            'alipay': {
                'name': '支付宝',
                'amount': self.PRICE_WEEKLY,
                'description': '订阅1周（3元）',
                'qr_image_path': None,
            }
        }

    def redeem_activation_code(self, code):
        """
        使用激活码激活订阅

        返回: (success, message)
        """
        try:
            from .activation import ActivationCodeManager
            acm = ActivationCodeManager()

            is_valid, weeks, error_msg = acm.verify_code(code)

            if not is_valid:
                return False, error_msg or "激活码无效"

            # 标记为已使用
            acm.mark_used(code, self._get_device_id())

            # 激活订阅
            self.activate_subscription(weeks)

            return True, f"激活成功！订阅有效期 +{weeks} 周"

        except Exception as e:
            return False, f"激活失败: {str(e)}"

    def get_contact_info(self):
        """获取卖家联系方式（从配置文件读取）"""
        config_file = os.path.join(self.config_dir, 'seller_info.json')

        # 默认联系方式
        default_info = {
            'wechat_id': '请在 ~/.nexus_dock/seller_info.json 中配置',
            'qq': '请配置',
            'phone': '',
            'note': '添加微信后请发送「激活码」获取帮助',
        }

        # 尝试读取配置文件
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    default_info.update(data)
            else:
                # 配置文件不存在，创建一个模板
                os.makedirs(os.path.dirname(config_file), exist_ok=True)
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        'wechat_id': '这里填你的微信号',
                        'qq': '这里填你的QQ号',
                        'phone': '',
                        'note': '添加微信后请发送「激活码」获取帮助',
                    }, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

        return default_info
