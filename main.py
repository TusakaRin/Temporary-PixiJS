# -*- coding: utf-8 -*-

# @Time : 2020/7/8 13:15
# @Author : yfdai


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animation')
def animation():
    return render_template('pixi.html')


if __name__ == '__main__':
    app.run(debug=True)
