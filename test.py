from flask import Flask
import time

app = Flask(__name__)

@app.route('/', methods=['POST'])
def slow():
    time.sleep(5)
    return 'OK', 200

app.run(port=9999)
