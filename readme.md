### Install ODBC Driver

1. Install dependencies for PyODBC and tds RUN 

```apt-get install -y tdsodbc unixodbc-dev RUN apt install unixodbc-bin -y RUN apt-get clean -y```

2. Edit /etc/odbcinst.ini RUN
```
echo "[FreeTDS]
Description = FreeTDS unixODBC Driver
Driver = /usr/lib/arm-linux-gnueabi/odbc/libtdsodbc.so
Setup = /usr/lib/arm-linux-gnueabi/odbc/libtdsS.so" >> /etc/odbcinst.ini
```
3. Install requirements (contains pyodbc) COPY ./requirements.txt /usr/src/app/requirements.txt RUN pip install --no-cache-dir -r requirements.txt

### 開機自動執行

修改/etc/rc.local
建立起動service
設定固定IP

