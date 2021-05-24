from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/alerts")
def alerts():
    return render_template('alerts.html')

@app.route("/bot-info")
def botinfo():
    return render_template('bot-info.html')