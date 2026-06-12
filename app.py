from flask import Flask
import time

app = Flask(__name__)

@app.route("/test-slow-endpoint")
def test_slow_endpoint():
    time.sleep(310)  # 310 seconds = 5+ minutes
    return "done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)