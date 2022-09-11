FROM python

WORKDIR /usr/src

COPY requirements.txt /tmp/
RUN pip3 install --upgrade pip \
    && pip3 install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

CMD ["python", "-u", "dataService.py"]
