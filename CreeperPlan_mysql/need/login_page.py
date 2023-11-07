#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 14:31
# @Author  : 傑君
# @File    : login_page.py
# @Software: PyCharm

import socket

import wmi
from PySide6.QtWidgets import QMessageBox
from need.creeper_page import creeper_method
from need.data_conn import linkDatabase
from need.share import SI
from need.signIn_page import signIn_method


class login_method:

    def login_button(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        linkDatabase.openConn(None)
        sql = "select id,user,password,name,phone,time,activateStatus,days from User_CZW where user='{0}' and password='{1}'" \
            .format(username, password)
        result = linkDatabase.cur_rowcount(None, sql)
        if result == 1:
            information = linkDatabase.cur_fetchone(None, sql)
            data_dict = {'id': information[0], 'user': information[1], 'password': information[2],
                         'name': information[3], 'phone': information[4], 'time': information[5],
                         'activateStatus': information[6], 'days': information[7]}
            SI.login_attr = data_dict['activateStatus']
            if username == data_dict['user'] and password == data_dict['password']:
                if data_dict['activateStatus'] == "1":
                    print("login successfully")
                    SI.uid = data_dict['id']
                    SI.user = data_dict['user']
                    SI.name = data_dict['name']
                    SI.expiration_time = data_dict['time']
                    SI.days = data_dict['days']
                    # 配置关键词
                    sql = "SELECT id,user,czw_user,czw_passwd,filterKeywords,filterIndustryKeywords,cleanORsaveKeywords FROM `UserConfigurationKeys_CZW` where id='{0}' and user='{1}'".format(
                        SI.uid, SI.user)
                    gjc_data = linkDatabase.cur_fetchall(None, sql)
                    SI.creeper_win.ui.le_userName.setText(gjc_data[0][2])
                    SI.creeper_win.ui.le_passWord.setText(gjc_data[0][3])
                    SI.creeper_win.ui.te_gjc.setPlainText(gjc_data[0][4])
                    SI.creeper_win.ui.te_hy.setPlainText(gjc_data[0][5])
                    SI.creeper_win.ui.pte_cleanORsave_gjc.setPlainText(gjc_data[0][6])
                    # 登录日志
                    self.info()
                    sql = "INSERT INTO `Log_CZW`(`id`, `user`, `type`, `operationTime`) VALUES ('{0}', '{1}', '{2}', NOW());".format(
                        SI.uid, SI.user, '爬虫登录'
                    )
                    linkDatabase.cur_insert(None, sql)
                    SI.login_win.hide()
                    SI.creeper_win.show()
                    creeper_method.configurationUserInfo(SI.creeper_win)
                    print('登录成功')
                else:
                    print("the user's time expires and needs to be recharged")
                    QMessageBox.information(SI.login_win, "提示", "用户时间到期，需充值")
        else:
            print("the user name or password is incorrect")
            QMessageBox.warning(SI.login_win, "提示", "用户名或密码错误")
        linkDatabase.closeBiConn(None)

    def register_button(self):
        signIn_method.turnOnInitialization(SI.signIn_win)
        SI.signIn_win.show()

    # 获取电脑配置信息
    def info(self):
        w = wmi.WMI()
        computerName = None
        theUser = None
        manufactureDate = None
        mainboardModel = None
        motherboardSerialNumber = None
        CPUmodel = None
        CPUserialNumber = None
        memoryManufacturer = None
        memoryModel = None
        memorySize = None
        graphicsCardName = ""
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sk.connect(('8.8.8.8', 80))
            ip = sk.getsockname()[0]
        finally:
            sk.close()
        IP = "IP地址: %s" % ip
        for BIOSs in w.Win32_ComputerSystem():
            computerName = "电脑名称: {0}".format(BIOSs.Caption)
            theUser = "使 用 者: {0}".format(BIOSs.UserName)
        for BIOS in w.Win32_BIOS():
            manufactureDate = "出厂日期: {0}".format(BIOS.ReleaseDate[:8])
            mainboardModel = "主板型号: {0}".format(BIOS.SerialNumber)
        for i in w.Win32_BaseBoard():
            motherboardSerialNumber = "主板序列号: {0}".format(i.SerialNumber.strip())
        for processor in w.Win32_Processor():
            CPUmodel = "CPU型号: {0}".format(processor.Name.strip())
            CPUserialNumber = "CPU序列号: {0}".format(processor.ProcessorId.strip())
        for memModule in w.Win32_PhysicalMemory():
            totalMemSize = int(memModule.Capacity)
            memoryManufacturer = "内存厂商: {0}".format(memModule.Manufacturer)
            memoryModel = "内存型号: {0}".format(memModule.PartNumber)
            memorySize = "内存大小: {0}".format((totalMemSize / 1024 ** 3))
        for xk in w.Win32_VideoController():
            graphicsCardName = str(graphicsCardName) + "\n  显卡名称: {0}".format(xk.name)

        sql = "INSERT INTO `ComputerInformationUser_CZW`(`id`, `user`, `IP`, `computerName`, `theUser`, `manufactureDate`, `mainboardModel`, `motherboardSerialNumber`, `CPUmodel`, `CPUserialNumber`, `memoryManufacturer`, `memoryModel`, `memorySize`, `graphicsCardName`, `nowTime`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', NOW());".format(
            SI.uid, SI.user, IP, computerName, theUser, manufactureDate, mainboardModel, motherboardSerialNumber,
            CPUmodel, CPUserialNumber, memoryManufacturer, memoryModel, memorySize, graphicsCardName
        )
        linkDatabase.cur_insert(None, sql)
        print('computerInfoCapture')

    def topUP_button(self):
        linkDatabase.openConn(None)
        sql = "SELECT version_url FROM `VersionSet_CZW`"
        version_data = linkDatabase.cur_fetchall(None, sql)
        text = version_data[0][0]
        linkDatabase.closeBiConn(None)
        QMessageBox.information(SI.login_win, "提示", text)
