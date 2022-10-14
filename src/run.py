from data_recv import Thread_recv_data
from data_service import app
from gevent import pywsgi

if __name__ == '__main__':
    # logging.basicConfig(filename='dataRecv.log', level=logging.DEBUG, format=LOG_FORMAT)
    thread_data = Thread_recv_data(host='', port=10001, db_user='gaoya', db_pwd='gaoya')
    thread_data.start()

    # server = pywsgi.WSGIServer(('0.0.0.0', 5088), app)
    # server.serve_forever()
    # app.run(host='0.0.0.0', port=5088, debug=False)#