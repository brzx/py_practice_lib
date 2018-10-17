#!/usr/bin/env python
'''
---- install cx_Oracle
---- pip install cx_Oracle
---- or go to http://cx-oracle.sourceforge.net/ to download msi file for windows platform
---- document is at http://cx-oracle.readthedocs.io/en/latest/index.html
'''
import cx_Oracle

class EnvSetOracle():
    def __init__(self):
        self.username = ''
        self.userpwd = ''
        self.port = 1521
        self.host = ''
        self.dbname = ''
    def setCountryProd(self):
        self.username = 'un'
        self.userpwd = 'pw'
        self.host = 'host'
        self.dbname = 'schema'
    def setCountryTest(self):
        self.username = 'un'
        self.userpwd = 'pw'
        self.host = 'host'
        self.dbname = 'schema'

class OracleConnect():
    def __init__(self, host, port, dbname, username, userpwd):
        dsn = cx_Oracle.makedsn(host, port, dbname)
        self.conn = cx_Oracle.connect(username, userpwd, dsn)
    def runSql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        #count = cursor.rowcount
        return result
        cursor.close()
    def closeConn(self):
        self.conn.close()

if __name__ == '__main__':
    env = EnvSetOracle()
    env.setCountryProd()
    sql = 'select count(1) from process_log'

    ocap = OracleConnect(env.host, env.port, env.dbname, env.username, env.userpwd)
    reap = ocap.runSql(sql)
    print reap
    ocap.closeConn()

    env.setAUProd()
    ocau = OracleConnect(env.host, env.port, env.dbname, env.username, env.userpwd)
    reau = ocau.runSql(sql)
    print reau
    ocau.closeConn()