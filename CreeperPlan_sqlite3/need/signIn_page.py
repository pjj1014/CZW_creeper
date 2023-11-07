#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 15:37
# @Author  : 傑君
# @File    : signIn_page.py
# @Software: PyCharm
import hashlib
import uuid
from PySide6.QtWidgets import QMessageBox
from need.data_conn import linkDatabase
from need.share import SI


class signIn_method:

    def signIn_button(self):
        uid = uuid.uuid1().hex
        user = self.ui.le_user.text()
        passwd = self.ui.le_password.text()
        name = self.ui.le_name.text()
        phone = self.ui.le_phone.text()
        gjc_filter = "运维服务,病案,容灾,录入,扫描,采集终端,超融合,虚拟化,整理,数字化,电子化,分布式存储,档案,VMwareCommVault,虚拟桌面,流程自动化,随案生成,磁带库"
        hygjc_filter = "公积金,税务,民政,档案馆,档案局,医院,人社,人力资源和社会保障局,法院,检察院,公安,市场监督管理,学校,学院,交通,烟草"
        cleanORsaveGJC_filter = "单一,租赁,装修,装饰,土地,档案袋,档案柜,密集架,密集柜,整理箱,大数据,维修,设计,总承包,公路,电梯,办公设,监理,楼宇,办公家,档案密,弱电,搬迁,耗材," \
                                "打印机,计算机,显示屏,修缮,物业,保洁,配电,多普勒,X射线,水泵,考试,热控,机械,城管,档案盒,造船,耕地,接种,快递,船舶,食堂,供电,消防,空调,X线,彩超," \
                                "房租,污水,印刷,电子化公开招标,电子化招标,电子化政府采购,教学数字化,数字化平台,公众号运维,三维数字化,数字化教学,支付电子化,监测站运维 "
        if len(user) < 3 or len(user) > 16:
            QMessageBox.information(SI.signIn_win, "提示", "用户名错误")
            return
        if len(passwd) < 3 or len(passwd) > 18:
            QMessageBox.information(SI.signIn_win, "提示", "密码错误")
            return
        if len(name) > 18:
            QMessageBox.information(SI.signIn_win, "提示", "名字错误")
            return
        if len(phone) != 11:
            QMessageBox.information(SI.signIn_win, "提示", "手机号错误")
            return
        linkDatabase.openConn(None)
        # 验证user是否重复
        u_checkSQL = "select user from `User_CZW` where user='{0}'".format(user)
        uChekck_data = linkDatabase.cur_rowcount(None, u_checkSQL)
        if uChekck_data != 0:
            QMessageBox.information(SI.signIn_win, "提示", "用户名重复")
        else:
            # 手机验证
            uPhone_checkSQL = "select phone from `User_CZW` where phone='{0}'".format(phone)
            uPhoneChekck_data = linkDatabase.cur_rowcount(None, uPhone_checkSQL)
            if int(uPhoneChekck_data) >= 3:
                QMessageBox.information(SI.signIn_win, "提示", "同一手机号最多绑定三个帐号")
            else:
                # 注册开始
                signIn_SQL = "INSERT INTO `User_CZW`(id, USER, PASSWORD, NAME, phone, time, activateStatus, createTime, days) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', datetime(date('now'),'+ {5} day'), 1,date('now'), {5} )".format(
                    uid, user, passwd, name, phone, 7
                )
                signInCheck_SQL = "SELECT id FROM `User_CZW` WHERE id='{0}'".format(uid)
                uesrConfiguration_SQL = "INSERT INTO `UserConfigurationKeys_CZW` ( id, USER, filterKeywords, filterIndustryKeywords, cleanORsaveKeywords )VALUES('{0}','{1}','{2}','{3}','{4}')".format(
                    uid, user, gjc_filter, hygjc_filter, cleanORsaveGJC_filter)
                uesrConfigurationCheck_SQL = "SELECT id FROM `UserConfigurationKeys_CZW` WHERE id='{0}'".format(uid)
                linkDatabase.cur_insert(None, signIn_SQL)
                signIn_data = linkDatabase.cur_rowcount(None, signInCheck_SQL)
                uesrConfiguration_data = 0
                if signIn_data == 1:
                    linkDatabase.cur_insert(None, uesrConfiguration_SQL)
                    uesrConfiguration_data = linkDatabase.cur_rowcount(None, uesrConfigurationCheck_SQL)
                else:
                    QMessageBox.information(SI.signIn_win, "提示", "注册失败")
                if signIn_data == 1 and uesrConfiguration_data == 1:
                    QMessageBox.information(SI.signIn_win, "提示", "注册成功")
                    SI.signIn_win.close()
        linkDatabase.closeBiConn(None)

    # 返回按钮
    def return_button(self):
        SI.signIn_win.close()

    # 打开初始化
    def turnOnInitialization(self):
        self.ui.le_user.setText('')
        self.ui.le_password.setText('')
        self.ui.le_name.setText('')
        self.ui.le_phone.setText('')
