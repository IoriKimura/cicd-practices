from flask import Flask
import logging
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

logging.basicConfig(filename='/var/log/flask-app.log', level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    logger.info('Received request on home page')
    return 'Hello, Monitoring!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
