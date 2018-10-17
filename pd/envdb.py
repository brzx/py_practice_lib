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
    def getCursor(self):
        return self.conn.cursor()
    def closeConn(self):
        self.conn.close()