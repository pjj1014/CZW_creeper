#! CreeperPlan   python
#  44719
# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2022/6/14 15:23
# @Author  : 傑君
# @File    : data_conn.py
# @Software: PyCharm
import pymysql


# mysql
class linkDatabase():
    host = 'localhost'
    user = 'root'
    passwd = '123456.'
    port = 3066
    db = 'creeper-plan'
    charset = 'utf8'
    conn = None
    cur = None

    # 查询的总数
    def cur_rowcount(self, sql):
        information_return = ""
        try:
            linkDatabase.cur.execute(sql)
            information_return = linkDatabase.cur.rowcount
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
            information_return = linkDatabase.cur.execute(sql)
            linkDatabase.conn.commit()
        except Exception as e:
            print(e)
            information_return = e
            linkDatabase.conn.rollback()
        return information_return

    # 打开连接
    def openConn(self):
        linkDatabase.conn = pymysql.Connect(host=linkDatabase.host, user=linkDatabase.user, passwd=linkDatabase.passwd,
                                            port=linkDatabase.port, db=linkDatabase.db, charset=linkDatabase.charset)
        linkDatabase.cur = linkDatabase.conn.cursor()

    # 关闭连接
    def closeBiConn(self):
        linkDatabase.cur.close()
        linkDatabase.conn.close()


if __name__ == "__main__":
    linkDatabase.openConn(None)
    sql = "SELECT version_url FROM `VersionSet_CZW`"
    version_data = linkDatabase.cur_fetchall(None, sql)
    print(version_data[0][0])
    linkDatabase.closeBiConn(None)
