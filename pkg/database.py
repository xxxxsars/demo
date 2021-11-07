import pyodbc
import configparser

server = 'tcp:myserver.database.windows.net'
database = 'mydb'
username = 'myusername'
password = 'mypassword'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


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

        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        return conn


def read_conf(path: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(path)
    return config


if __name__ =="__main__":
    db = DB("conf/config.ini")
    print(db)