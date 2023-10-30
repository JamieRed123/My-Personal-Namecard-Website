# My Personal Namecard Website with help from 100 Days of Python - Day 56 - My Personal Site

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)