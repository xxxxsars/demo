FROM python:3.9
RUN  apt-get update
RUN  apt-get install gcc

# Install python opencv dependence package
RUN  apt-get install -y ffmpeg libsm6 libxext6

# Install pyodbc driver
RUN apt-get install -y tdsodbc unixodbc-dev
RUN echo -e "[FreeTDS]\nDescription = FreeTDS unixODBC Driver\nDriver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\nSetup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

# Install python package
#ADD ./* /demo/
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /demo

EXPOSE 8000

