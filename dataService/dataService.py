from flask.json import JSONEncoder
from flask import Flask, jsonify, request
import json
from datetime import datetime, date
from gevent import pywsgi

# Fomart change of time
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
    cursor = db.cursor()
    feedBacks = {'data': []}

    # Start query
    sql = "SELECT * FROM `data_result` WHERE " + "Created >= '" + start + "' and Created <= '" + end + "'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # Generate json record
            feedBack = {}

            feedBacks['data'].append(feedBack)
    except:
        print("Error: unable to fetch data")

    db.close()

    return jsonify(feedBacks)


if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('0.0.0.0', 5088), app)
    # server.serve_forever()
    # app.run(host='0.0.0.0', port=5088, debug=False)#
