#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2022/6/14 15:23
# @Author  : 傑君
# @File    : data_conn.py
# @Software: PyCharm

import sqlite3

class linkDatabase():
    conn = None
    cur = None

    # 查询的总数
    def cur_rowcount(self, sql):
        information_return = ""
        try:
            linkDatabase.cur.execute(sql)
            rowcount=len(linkDatabase.cur.fetchall())
            information_return = rowcount
        except Exception as e:
            print(e)
            information_return = e
        return information_return

    # 查询一条信息
    def cur_fetchone(self, sql):
        information_return = ""
        try:
            linkDatabase.cur.execute(sql)
            information_return = linkDatabase.cur.fetchone()
        except Exception as e:
            print(e)
            information_return = e
        return information_return

    # 查询全部信息
    def cur_fetchall(self, sql):
        information_return = ""
        try:
            linkDatabase.cur.execute(sql)
            information_return = linkDatabase.cur.fetchall()
        except Exception as e:
            print(e)
            information_return = e
        return information_return

    # 插入修改删除一条数据
    def cur_insert(self, sql):
        information_return = ""
        try:
            linkDatabase.cur.execute(sql)
            information_return = len(linkDatabase.cur.fetchall())
            linkDatabase.conn.commit()
        except Exception as e:
            print(e)
            information_return = e
            linkDatabase.conn.rollback()
        return information_return

    # 打开连接
    def openConn(self):
        linkDatabase.conn = sqlite3.connect('czw.db')
        linkDatabase.cur = linkDatabase.conn.cursor()

    # 关闭连接
    def closeBiConn(self):
        linkDatabase.cur.close()
        linkDatabase.conn.close()
