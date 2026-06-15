from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/test-slow-endpoint")
def test_slow_endpoint():
    if random.random() < 0.3:  # 30% of requests
        time.sleep(70)         # > 60 seconds
    return "done"