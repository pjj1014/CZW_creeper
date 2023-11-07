# coding=utf-8
# ! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/5/8 18:16
# @Author  : 傑君
# @File    : test01.py
# @Software: PyCharm+

from app.testAliPay import aliPay
from flask import Flask, request

app = Flask(__name__)


@app.route('/notify')
def pay_ali():
    alipay = aliPay()
    return alipay


@app.route('/payreturn', methods=["GET", "POST"])
def pay_return():
    print("-------------------------------------------------")
    print(request.form)
    print(request.form.get('trade_status'))
    return request.form.get('trade_status')


app.run()
