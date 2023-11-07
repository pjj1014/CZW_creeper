#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 10:38
# @Author  : 傑君
# @File    : testGetIp.py
# @Software: PyCharm


import wmi
import socket

# 获取电脑配置信息
def info():
    w = wmi.WMI()
    computerName=None
    theUser=None
    manufactureDate=None
    mainboardModel=None
    motherboardSerialNumber=None
    CPUmodel=None
    CPUserialNumber=None
    memoryManufacturer=None
    memoryModel=None
    memorySize=None
    graphicsCardName=None
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
        graphicsCardName = str(graphicsCardName) + "\n显卡名称: {0}".format(xk.name)

    print(IP,
    computerName,
    theUser,
    manufactureDate,
    mainboardModel,
    motherboardSerialNumber,
    CPUmodel,
    CPUserialNumber,
    memoryManufacturer,
    memoryModel,
    memorySize,
    graphicsCardName)

if __name__ == "__main__":
    info()