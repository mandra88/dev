from flask import Flask

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# create a counter metric
hit_count = Counter('hit_count', 'Number of hits to the home page')

@app.route('/')
def home():
    hit_count.inc()  # increment the counter metric
    return f'Hello, world! This page has been hit {hit_count._value.get()} times.'

# endpoint for Prometheus to scrape the metrics
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(port=5000)