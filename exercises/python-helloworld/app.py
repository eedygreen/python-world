from flask import Flask
from flast import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello Eedy!"

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    # logging info
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    # loging info
    app.logger.info('Metrics request successfull')
    return response

if __name__ == "__main__":
    # streaming logs to log file app.log
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
