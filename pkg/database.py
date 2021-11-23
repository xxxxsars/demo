import pyodbc
import configparser

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
        # # conn = pyodbc.connect(
        # #     r'DRIVER={ODBC Driver 17 for SQL Server};'
        # #     r'SERVER=reui.diskstation.me,1433;'
        # #     r'DATABASE=master;'
        # #     r'UID=sa;'
        # #     r'PWD=Zz01470147;'
        # #     r'Trusted_Connection=yes'
        # # )
        #
        # conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host=server, database=db
        #                     , user=username, password=password)

        return conn


def read_conf(path: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(path)
    return config


if __name__ =="__main__":
    db = DB("../conf/config.ini")
    print(db)