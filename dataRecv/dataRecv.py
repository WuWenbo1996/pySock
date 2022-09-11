import socket
import sys
import time
import csv
import pymysql

import threading

import binascii

BUFSIZE = 1024

class Thread_recv_data(threading.Thread):
    def __init__(self, host, port, db_user, db_pwd):
        super().__init__()
        self.host = host
        self.port = port
        self.server = None

        self.db_user = db_user
        self.db_pwd = db_pwd

        # data
        self.recv_msg, self.client_addr = None, None

    def create_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error as msg:
            print('Failed to create socket. Error message: ' , msg)
            sys.exit()

        print('socket created')

    def bind_socket(self):
        try:
            self.server.bind((self.host, self.port))
        except socket.error as msg:
            print('Bind failed. Error msg:' , msg)
            sys.exit()

        print('socket bind complete')

    def sql_saving(self, key, val):
        db = pymysql.connect(host='', user=self.db_user, password=self.db_pwd, database="cabletemp")
        cursor = db.cursor()
        sql = "INSERT INTO `test` (`create_time`, `data`) VALUES ()"
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        db.close()

    def run(self):
        self.create_socket()
        self.bind_socket()

        # Function for handling connections. This will be used to create threads
        while True:
            # 获取数据的发送终端地址以及收到的数据
            self.recv_msg, self.client_addr = self.server.recvfrom(BUFSIZE)

            self.localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(str(self.recv_msg, 'utf-8'))

        self.server.close()


if __name__ == '__main__':
    thread_data = Thread_recv_data(host='', port=10001, db_user='gaoya', db_pwd='gaoya')
    thread_data.start()