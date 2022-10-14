FROM mysql

WORKDIR /usr/local/

#设置免密登录
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes

#将所需文件放到容器中
COPY ./setup.sh /usr/local/setup.sh
COPY ./sql /usr/local/sql

#设置容器启动时执行的命令
CMD ["sh", "setup.sh"]