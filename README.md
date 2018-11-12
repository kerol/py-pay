### py-pay
Python pay library.
```
pip install -U py-pay
```

#### 微信支付
```
from py_pay.wechat import WechatPay
wechat_conf = {
    'app_id': 'appid',
    'mch_id': '商户号',
    'key': '签名key',
    # 需要双向证书的配置下面两行
    # 'cert_file': '/path/to/cert_file',
    # 'cert_key': '/path/to/cert_key',
}
wechat_pay = WechatPay(**wechat_conf)

# 示例
params = {'foo': 'bar'}
wechat_pay.unifiedorder(params)  # 统一下单
wechat_pay.orderquery(params)  # 查询订单
wechat_pay.closeorder(params)  # 关闭订单
wechat_pay.refund(params)  # 申请退款
wechat_pay.refundquery(params)  # 退款查询
wechat_pay.pay_notify(request.body)  # 支付通知
wechat_pay.response(False, '签名失败')  # 支付通知

wechat_pay.promotion_transfers(params)  # 企业付款
```

