import pyodbc
import configparser
import os

class DB:
    def __init__(self, conf_path: str):
        self.conf_path = conf_path
        self.conn = self._connection()

    def _connection(self):
        conf = read_conf(self.conf_path)
        db = conf["database"]
        server = db["server"]
        database = db["database"]
        username = db["username"]
        password = db["password"]

        conn_str = f'DRIVER=FreeTDS;SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};TDS_Version=8.0;'
        conn = pyodbc.connect(conn_str,autocommit=True)
        return conn

    def query(self):
        cursor = self.conn.cursor()
        cursor.execute("Select * from predict_log")
        for row in cursor.fetchall():
            print (row)


def read_conf(path: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(path)
    return config


def path_combine(path,*params):
    path:str
    for param in params:
        path = os.path.join(param)

    return path

if __name__ =="__main__":
    db = DB("../conf/config.ini")
    db.query()

