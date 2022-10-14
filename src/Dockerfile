FROM centos

WORKDIR /usr/src

# RUN yum install -y python36

COPY requirements.txt /tmp/
RUN pip3 install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com --upgrade pip3 \
    && pip3 install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

CMD ["python3", "-u", "run.py"]
