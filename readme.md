### Install ODBC Driver

1. Install dependencies for PyODBC and tds RUN 

```cmd
$ apt-get install -y tdsodbc unixodbc-dev 
$ apt install unixodbc-bin -y 
$ apt-get clean -y
```

2. Edit /etc/odbcinst.ini
```
echo "[FreeTDS]
Description = FreeTDS unixODBC Driver
Driver = /usr/lib/arm-linux-gnueabi/odbc/libtdsodbc.so
Setup = /usr/lib/arm-linux-gnueabi/odbc/libtdsS.so" >> /etc/odbcinst.ini
```
3. Install requirements (contains pyodbc) 
```cmd
pip install --no-cache-dir -r requirements.txt
```

### Create systemctl service

1. Create a new service file.
```cmd

```

2. Linked this file to the systemctl path
```cmd

```
3. Register service
```cmd

```

### Restful API

1. [Documentation](https://tw.alphacamp.co/blog/rest-restful-api)

2. Restful Method:
    * POST - Create 
    * GET -  Read
    * PATCH - Update 
    * DELETE -  Delete



### form post vs ajax post

1. [Form post sample](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_form_method_post) 

2. [Ajax post sample](https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_ajax_post)


