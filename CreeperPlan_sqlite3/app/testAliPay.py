#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/6/23 13:21
# @Author  : 傑君
# @File    : testAliPay.py
# @Software: PyCharm
import logging
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a', )
logger = logging.getLogger('')


def aliPay():
    """
    设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
    """
    alipay_client_config = AlipayClientConfig(sandbox_debug=True)
    alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    alipay_client_config.app_id = '2021000121603655'
    alipay_client_config.app_private_key = 'MIIEpAIBAAKCAQEA0gQBW/0I9jcAWZ9HRHO8hmHL3vH4LI8yY2Al7p29uMd3Oe6rbAwnCg1TT5ztachUGCK+kPCCLEJfv8hz48GJfNQAFodDXSPUmpaTaL2fD9LdS4eY45tfqWhPW5pzFQaoBRdhIymULIgxYx5CCgUFgHfdbNg+w0EYLPjPp43jMLdZsQlJuslDSn4jNiQcZ7so3Mb8Ewclapn4tU/IwgoT/ntSzl3jPWt8Ases/iRLBL0uaRfzr9UQyVIII0KcpKjVFybnddU1VCwxJwTsat9ixnBmGFY00O/2QvpV7x/k6gg3AIX/fLxZXeKwtvwk/X28XjPBVL+O8g2Mey0APzQmqwIDAQABAoIBABoU60JMU2+Ydw+qS0SCBxi9Tn9al5KZGg3jY/KVXnlzNCharqlVfQevjfgmKgnoGiGBNx9y7wemGpQLxfC0GWoKPhSOKdyIVZ/5MUdhvT5O1rLJnUAvDJtSXACpVr92uyketS6TvFYnd9KycEskQoGo4TPiSzEehW0YXVmWsm9bLD7VV5RinCHiLSzyif6H7/3jh8AnZ3+zTzv2UcTfaJfIONV01wZACnRdOlRilvoof8c9PcuOUnPDe7GRKqG4Fp15T4AVKtbNTG9Gr9w24C/0BajlIg0mByQad+og0rtZE04erqpXMrqed/cs0AAU3jLjMeOfIES6VD8+FJpw/qkCgYEA8oKkmqYKezm0grHVgByDJO3sayY2IpkNBV9ha6Ae66wo024tb5jeBUqV2CgVg3copHZNkcvalmcdOgk/qfwY6SFbkVcAgNdX1cpa32bdip7GTencSLqASy9kD3wX9rgf//ojjB1kKlI9oEKlYIeU17OF7/33maMqZTPVSFlElaUCgYEA3bKjAwHuGk0K9D38bKO7KPWRgs/3/ij/UUdZyTNeo91qWfTJLL5nwqKwwYEixcSj6+8sO65QqQ7TONJdZuH5P7wMSedzpFpaJxF0g0CgW3qJrZaYBl+4aT1+z3Em6qKkeZsY2zMgCX7qZp3lXz8fNGCoEZqwTwSjZeJ2A06oOg8CgYEAgJorNB+NO1+UjCJGOBPmr/TEBOZUmvBS6WB1Rx+4hf3cAJNS4PVN97xfzisjjX3pPZ3G8OQL3Op9o0M4Uapwg2C/MEnU6H5KBAO1QPdJ0LL2Mmcr/B1632QYSeXix2FJBvPdWfZUIeVO7Oeqz4/WrLR0+JnTbdQLLXPZTO6Z4kkCgYAsUITdGQmrIDNMVweZ/7Bto4iOiVuc5j0C1ixQV4BXaO7VRGTiGL1M3pBOXa3BsmjBxHEnDNT6tgfql8Iryoe0AbbDHwyykYzrukV75vMm1funQy7oN0H5Z11twcRxqkkONb5mMnX47/GSyYUL4OYv5hIyUqVjZh3zQ60rRBHEaQKBgQCn/oY531dPTmDv80pyMza279guyJS8VX2FWuut8TbQXpV87hDzWEupQQyNqJ3hFGOEiUuUxYzohyGQpzoL/ZU82n8Raq5t/BD6XoymMucMQH3BRUOecwqX8sbtK4QXxfcAgrSUCrGm3b2fD/z7PLqZdasHBZM1MK3wxzk2iLj/Rg=='
    alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoKF7OBCpEBUu65/D7d7iaqgvvZo17FUtsvcpTliLmFDBuw69FAjp7BeRpBxvxFqpBX70m+/W74KJ6Ao9mpiPoCUbt3wmF1uSAoaqZPnYNd0k7QevYSHuoGJwsEwD0drFXJyz9lfEmkxiPMEjFQ2guiAefTUba9gqjOM1/kZPZLIverio/riDJpY+j+Heo7CGTa2iMdmM9+fnbz7x7vwTZd6CHoloBfQ1tmyNDVIh8gAyClpEmKHiFPJLzCno1zztbqxdi6GY5H2uo1HxuPfVF7db4GsZ/XHWM9J4Zh82thWf8P3mL2eBPUP1BrtDjVnfhlOUrQO3jUlciAfZA22BEwIDAQAB'

    """
    得到客户端对象。
    注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
    logger参数用于打印日志，不传则不打印，建议传递。
    """
    client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)
    """
    页面接口示例：alipay.trade.page.pay
    """
    # 对照接口文档，构造请求对象
    model = AlipayTradePagePayModel()
    model.out_trade_no = '2000000554768'
    model.total_amount = 8989
    model.subject = '赏金'
    model.product_code = 'FAST_INSTANT_TRADE_PAY'

    request = AlipayTradePagePayRequest(biz_model=model)
    request.notify_url="https://5501429sg6.zicp.fun/payreturn"
    # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
    response = client.page_execute(request, http_method="POST")
    print("alipay.trade.page.pay response:" + response)
    return response