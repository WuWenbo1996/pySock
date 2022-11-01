import socket
import sys
import time
import pymysql

import threading


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
            self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP连接
        except socket.error as msg:
            print('Failed to create socket. Error message: ', msg)
            sys.exit()

        print('socket created')

    def bind_socket(self):
        try:
            self.server.bind((self.host, self.port))
        except socket.error as msg:
            print('Bind failed. Error msg:', msg)
            sys.exit()

        print('socket bind complete')

    def sql_saving(self, created, data):
        db = pymysql.connect(host='', user=self.db_user, password=self.db_pwd, database="cabletemp")
        cursor = db.cursor()

        sql = "INSERT INTO data_result (Created, data) VALUES " + "('" + created + "','" + str(data, 'utf-8') + "');"  # 列
        # 如果数据data转换成字符串形式str(data, 'utf-8')，可以存储。
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            # print('sql commit')
        except:
            # 如果发生错误则回滚
            db.rollback()
            # print('sql rollback')
        db.close()

    def run(self):
        self.create_socket()
        self.bind_socket()

        # Function for handling connections. This will be used to create threads
        while True:  # 第3步需要改进的地方：  接收独立，不再使用while Ture循环等待，改成kafka消息队列
            # 获取数据的发送终端地址以及收到的数据

            self.recv_msg, self.client_addr = self.server.recvfrom(BUFSIZE)

            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 存储信息
            self.sql_saving(localtime, self.recv_msg)
            # print(str(self.recv_msg, 'utf-8'))  # test

        self.server.close()


if __name__ == '__main__':
    thread_data = Thread_recv_data(host='', port=10001, db_user='gaoya', db_pwd='gaoya')
    thread_data.start()

