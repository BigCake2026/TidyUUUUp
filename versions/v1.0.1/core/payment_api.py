"""
支付API配置系统 - Payment API Config
支持通过浏览器打开支付页面，接入第三方支付API

使用方法：
  1. 在 ~/.nexus_dock/payment_config.json 中配置支付API
  2. 用户点击支付时，自动在浏览器中打开支付页面
  3. 支付完成后，输入订单号验证
"""
import os
import json
import uuid
import time
import hashlib
import webbrowser
from datetime import datetime


class PaymentAPI:
    """支付API管理器"""

    # 默认配置（已预配置支付FM）
    DEFAULT_CONFIG = {
        "provider": "zhifux",  # 支付提供商: zhifux(支付FM) / epay / payjs / xunhupay / custom
        "api_url": "https://api-55j4mnreh5hc.zhifu.fm.it88168.com/api",  # 支付FM接口根地址
        "pid": "678332010234003456",  # 商户号 (merchantNum)
        "key": "7b2c32a6a25bd3a8f502780c660b140b",  # 接入密钥 (secret)
        "name": "TidyUUUUp 订阅",
        "notify_url": "https://www.zhifux.com/success.txt",  # 异步通知地址
        "return_url": "",  # 同步跳转地址（可选）

        # 套餐价格配置
        "plans": {
            "weekly": {
                "name": "周卡",
                "price": 3.00,
                "weeks": 1,
                "description": "1周使用权"
            },
            "monthly": {
                "name": "月卡",
                "price": 10.00,
                "weeks": 4,
                "description": "4周使用权（推荐）"
            },
            "yearly": {
                "name": "年卡",
                "price": 88.00,
                "weeks": 52,
                "description": "52周使用权（超值）"
            }
        },

        # 支付方式（支付FM免签类型推荐：wechat/alipay）
        "payment_types": {
            "wechat": "微信支付",
            "alipay": "支付宝",
            "unipay": "云闪付",
        },

        # 支付FM专属：支付方式轮循池（更稳定，推荐使用）
        "zhifux_loops": {
            "tloop": "微信轮循池（推荐）",
            "aloop": "支付宝轮循池（推荐）",
        },

        # 订单验证API（可选）
        "verify_api": "",
    }

    def __init__(self):
        self.config_dir = os.path.join(os.path.expanduser('~'), '.nexus_dock')
        self.config_file = os.path.join(self.config_dir, 'payment_config.json')
        self.orders_file = os.path.join(self.config_dir, 'orders.json')
        self.config = dict(self.DEFAULT_CONFIG)
        self.orders = {}
        self._load_config()
        self._load_orders()

    def _load_config(self):
        """加载支付配置"""
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            else:
                # 配置文件不存在，创建默认配置
                self._save_config()
        except Exception as e:
            print(f"加载支付配置失败: {e}")

    def _save_config(self):
        """保存配置"""
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存配置失败: {e}")

    def _load_orders(self):
        """加载订单记录"""
        try:
            if os.path.exists(self.orders_file):
                with open(self.orders_file, 'r', encoding='utf-8') as f:
                    self.orders = json.load(f)
        except Exception:
            self.orders = {}

    def _save_orders(self):
        """保存订单记录"""
        try:
            with open(self.orders_file, 'w', encoding='utf-8') as f:
                json.dump(self.orders, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def create_order(self, plan_id='weekly', payment_type='wechat'):
        """
        创建订单

        参数:
            plan_id: weekly / monthly / yearly
            payment_type: wechat / alipay / qq

        返回:
            (order_id, pay_url, error_msg)
        """
        plan = self.config['plans'].get(plan_id)
        if not plan:
            return None, None, "无效的套餐"

        # 生成订单号
        order_id = f"ND{datetime.now().strftime('%Y%m%d%H%M%S')}{uuid.uuid4().hex[:8].upper()}"

        # 订单信息
        order = {
            'order_id': order_id,
            'plan_id': plan_id,
            'plan_name': plan['name'],
            'price': plan['price'],
            'weeks': plan['weeks'],
            'payment_type': payment_type,
            'payment_name': self.config['payment_types'].get(payment_type, payment_type),
            'status': 'pending',  # pending / paid / expired
            'created_at': time.time(),
            'created_at_str': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'paid_at': None,
            'paid_at_str': None,
        }

        # 保存订单
        self.orders[order_id] = order
        self._save_orders()

        # 生成支付链接
        pay_url = self._build_pay_url(order)

        return order_id, pay_url, None

    def _build_pay_url(self, order):
        """
        构建支付URL

        根据配置的支付提供商，构建不同的支付链接
        """
        provider = self.config.get('provider', 'custom')
        api_url = self.config.get('api_url', '')
        pid = self.config.get('pid', '')
        key = self.config.get('key', '')

        # 如果没有配置API，返回自定义的支付页面
        if not api_url:
            # 返回空，让UI显示内置的收款码
            return None

        # 构建标准的支付参数
        params = {
            'pid': pid,
            'out_trade_no': order['order_id'],
            'name': f"{order['plan_name']} - {self.config.get('name', 'TidyUUUUp')}",
            'money': f"{order['price']:.2f}",
            'type': order['payment_type'],
            'notify_url': self.config.get('notify_url', ''),
            'return_url': self.config.get('return_url', ''),
        }

        # 根据不同的支付提供商构建签名和URL
        if provider == 'zhifux':
            # 支付FM - 原生接口
            return self._build_zhifux_url(order)
        elif provider == 'zhifux_epay':
            # 支付FM - 易支付兼容模式(v2)
            return self._build_epay_url(api_url, params, key)
        elif provider == 'epay':
            # 易支付（常见的第三方支付平台）
            return self._build_epay_url(api_url, params, key)
        elif provider == 'payjs':
            # PayJS
            return self._build_payjs_url(api_url, params, key)
        elif provider == 'xunhupay':
            # 虎皮椒支付
            return self._build_xunhupay_url(api_url, params, key)
        else:
            # 自定义支付API
            return self._build_custom_url(api_url, params, key)

    def _build_zhifux_url(self, order):
        """构建支付FM原生接口链接（调用API获取支付链接）"""
        api_url = self.config.get('api_url', '').rstrip('/')
        merchant_num = self.config.get('pid', '')
        secret = self.config.get('key', '')

        if not api_url or not merchant_num or not secret:
            return None

        # 原生接口签名算法: md5(merchantNum + orderNo + amount + notifyUrl + secret)
        notify_url = self.config.get('notify_url', '') or 'https://www.zhifux.com/success.txt'
        sign_str = merchant_num + order['order_id'] + f"{order['price']:.2f}" + notify_url + secret
        sign = hashlib.md5(sign_str.encode()).hexdigest()

        # 支付方式：优先轮循池，没有则用定向
        payment_type = order['payment_type']
        if payment_type == 'wechat':
            pay_type = 'tloop'
        elif payment_type == 'alipay':
            pay_type = 'aloop'
        else:
            pay_type = payment_type

        # 构建请求参数
        import urllib.parse
        import urllib.request

        params = {
            'merchantNum': merchant_num,
            'orderNo': order['order_id'],
            'amount': f"{order['price']:.2f}",
            'notifyUrl': notify_url,
            'returnUrl': self.config.get('return_url', ''),
            'payType': pay_type,
            'sign': sign,
            'returnType': 'json',
            'subject': f"{order['plan_name']} - TidyUUUUp",
            'body': order.get('plan_name', '订阅'),
        }

        # 调用API获取支付链接
        try:
            query_string = urllib.parse.urlencode(params)
            full_url = f"{api_url}/startOrder?{query_string}"

            req = urllib.request.Request(full_url, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')

            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read().decode('utf-8')
                result = json.loads(data)

                if result.get('success') and result.get('data', {}).get('payUrl'):
                    return result['data']['payUrl']
                else:
                    print(f"支付FM API错误: {result.get('msg', '未知错误')}")
                    return None
        except Exception as e:
            print(f"调用支付FM API失败: {e}")
            return None

    def _build_epay_url(self, api_url, params, key):
        """构建易支付链接"""
        # 易支付签名算法
        sorted_params = sorted(params.items())
        sign_str = '&'.join([f"{k}={v}" for k, v in sorted_params if v]) + key
        sign = hashlib.md5(sign_str.encode()).hexdigest()
        params['sign'] = sign
        params['sign_type'] = 'MD5'

        # 构建URL
        query = '&'.join([f"{k}={self._url_encode(v)}" for k, v in params.items()])
        if api_url.endswith('?'):
            return api_url + query
        else:
            return api_url + '?' + query

    def _build_payjs_url(self, api_url, params, key):
        """构建PayJS链接"""
        params['mchid'] = params.pop('pid', '')
        return self._build_epay_url(api_url, params, key)

    def _build_xunhupay_url(self, api_url, params, key):
        """构建虎皮椒支付链接"""
        return self._build_epay_url(api_url, params, key)

    def _build_custom_url(self, api_url, params, key):
        """构建自定义支付链接"""
        return self._build_epay_url(api_url, params, key)

    def _url_encode(self, s):
        """URL编码"""
        import urllib.parse
        return urllib.parse.quote(str(s), safe='')

    def open_browser_pay(self, order_id, pay_url=None):
        """在浏览器中打开支付页面"""
        if pay_url is None:
            order = self.orders.get(order_id)
            if order:
                pay_url = self._build_pay_url(order)

        if pay_url:
            webbrowser.open(pay_url)
            return True
        return False

    def verify_order(self, order_id):
        """
        验证订单是否已支付

        优先调用验证API，没有的话检查本地状态
        """
        order = self.orders.get(order_id)
        if not order:
            return False, "订单不存在"

        # 如果已支付
        if order['status'] == 'paid':
            return True, "订单已支付"

        # 尝试调用验证API
        verify_api = self.config.get('verify_api', '')
        if verify_api:
            try:
                verified = self._call_verify_api(order_id)
                if verified:
                    self._mark_order_paid(order_id)
                    return True, "支付成功"
            except Exception as e:
                print(f"验证API调用失败: {e}")

        return False, "订单未支付"

    def _call_verify_api(self, order_id):
        """调用验证API"""
        import urllib.request
        verify_api = self.config.get('verify_api', '')
        key = self.config.get('key', '')

        params = {
            'out_trade_no': order_id,
            'pid': self.config.get('pid', ''),
        }
        sorted_params = sorted(params.items())
        sign_str = '&'.join([f"{k}={v}" for k, v in sorted_params]) + key
        params['sign'] = hashlib.md5(sign_str.encode()).hexdigest()

        query = '&'.join([f"{k}={self._url_encode(v)}" for k, v in params.items()])
        url = verify_api + ('&' if '?' in verify_api else '?') + query

        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                data = resp.read().decode('utf-8')
                # 简单处理返回，实际应该根据API文档解析
                return 'success' in data.lower() or '1' in data
        except Exception:
            return False

    def _mark_order_paid(self, order_id):
        """标记订单为已支付"""
        if order_id in self.orders:
            self.orders[order_id]['status'] = 'paid'
            self.orders[order_id]['paid_at'] = time.time()
            self.orders[order_id]['paid_at_str'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._save_orders()
            return True
        return False

    def mark_paid_manually(self, order_id):
        """手动标记订单为已支付（用于信任模式）"""
        return self._mark_order_paid(order_id)

    def get_order(self, order_id):
        """获取订单信息"""
        return self.orders.get(order_id)

    def get_plans(self):
        """获取所有套餐"""
        return self.config.get('plans', {})

    def get_payment_types(self):
        """获取所有支付方式"""
        return self.config.get('payment_types', {})

    def is_configured(self):
        """检查是否已配置支付API"""
        provider = self.config.get('provider', 'custom')
        if provider == 'zhifux':
            # 支付FM需要：api_url + pid(merchantNum) + key(secret)
            return bool(self.config.get('api_url', '') and
                        self.config.get('pid', '') and
                        self.config.get('key', ''))
        return bool(self.config.get('api_url', ''))

    def update_config(self, new_config):
        """更新配置"""
        self.config.update(new_config)
        self._save_config()
