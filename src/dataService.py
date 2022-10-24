from flask.json import JSONEncoder
from flask import Flask, jsonify, request
import pymysql
import json
from datetime import datetime, date
from gevent import pywsgi


# Format change of time
from pymysql.cursors import DictCursor


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, obj)


# Interface to front end
app = Flask(__name__)
app.json_encoder = CustomJSONEncoder


@app.route('/', methods=['post'])
def get_data():
    # Judge Input is json
    if request.is_json:
        request_data = request.get_json()
        start = request_data['start']
        end = request_data['end']
    else:
        print('The request is not json')
        return jsonify('request should be json')

    # Connect to db
    db = pymysql.connect(host='', user='gaoya', password='gaoya', database="cabletemp")
    cursor = db.cursor(DictCursor)  # 使返回的查询结果变为字典形式，而不是元组形式。
    feedBacks = {'data': []}

    # Start query
    sql = "SELECT * FROM `data_result` WHERE " + "Created >= '" + start + "' and Created <= '" + end + "'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:  # 处理
            if row['data'] is not None and row['data'] != '':
                # Generate json record
                feedBack = row
                # feedBack = {'data': row['data'], 'Created': row['Created']}  # 什么样的数据形式？？
                # json，
                feedBacks['data'].append(feedBack)
    except:
        print("Error: unable to fetch data")

    db.close()

    return jsonify(feedBacks)


if __name__ == '__main__':  #

    server = pywsgi.WSGIServer(('0.0.0.0', 5088), app)  # 5088
    server.serve_forever()
    app.run(host='0.0.0.0', port=5088, debug=False)  # 测试开关
