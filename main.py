# -*- coding: utf-8 -*-

# @Time : 2020/7/8 13:15
# @Author : yfdai


from flask import Flask, render_template, request
import time, json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simulation', methods=['POST'])
def run_simulation():
    print(dict(request.form))
    return {
        "currentTime": int(time.time())
    }


if __name__ == '__main__':
    app.run(debug=True)
