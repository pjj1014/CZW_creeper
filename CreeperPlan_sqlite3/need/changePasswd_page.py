#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 12:45
# @Author  : 傑君
# @File    : changePasswd_page.py
# @Software: PyCharm
from PySide6.QtWidgets import QMessageBox

from need.data_conn import linkDatabase
from need.share import SI


class changePasswd_method():

    # 修改密码
    def changePasswd_button(self):
        originalPasswd = self.ui.le_originalPasswd.text()
        changePasswd = self.ui.le_changePasswd.text()
        confirmPasswd = self.ui.le_confirmPasswd.text()
        if originalPasswd != "" and changePasswd != "" and confirmPasswd != "":
            linkDatabase.openConn(None)
            sql = "SELECT `password` FROM `User_CZW` where id='{0}' and user='{1}';".format(SI.uid, SI.user)
            originalPasswd_data = linkDatabase.cur_fetchall(None, sql)
            if originalPasswd_data[0][0] == originalPasswd:
                if changePasswd != originalPasswd:
                    if changePasswd == confirmPasswd:
                        sql = "UPDATE `User_CZW` set `password`='{2}' where id='{0}' and user='{1}';".format(SI.uid,
                                                                                                             SI.user,
                                                                                                             changePasswd)
                        sqlChek = "SELECT id FROM `User_CZW` WHERE `password`='{2}' AND id='{0}' AND user='{1}'".format(SI.uid,
                                                                                                             SI.user,
                                                                                                             changePasswd)
                        linkDatabase.cur_insert(None, sql)
                        passwdChange_data = linkDatabase.cur_rowcount(None, sqlChek)
                        if passwdChange_data == 1:
                            print("密码修改成功")
                            QMessageBox.information(SI.signIn_win, "提示", "密码修改成功，请重新登录")
                            SI.changePasswd_win.close()
                            SI.creeper_win.close()
                            SI.login_win.ui.passwordLineEdit.setText("")
                            SI.login_win.show()
                        else:
                            print("密码修改失败")
                            QMessageBox.information(SI.signIn_win, "提示", "密码修改失败")
                    else:
                        QMessageBox.information(SI.signIn_win, "提示", "两次密码输入不一致")
                else:
                    QMessageBox.information(SI.signIn_win, "提示", "原密码与修改密码不能相同")
            else:
                QMessageBox.information(SI.signIn_win, "提示", "原密码错误")
            linkDatabase.closeBiConn(None)
            print('关闭数据库')
        else:
            QMessageBox.information(SI.signIn_win, "提示", "请输入密码")

    # 返回
    def return_button(self):
        SI.changePasswd_win.close()
