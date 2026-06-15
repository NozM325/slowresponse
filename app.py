import random
from flask import Flask
import time

app = Flask(__name__)

@app.route("/test-slow-endpoint")
def test_slow_endpoint():
    if random.random() < 0.3:  # 30% of requests
        time.sleep(70)         # > 60 seconds
    return "done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)