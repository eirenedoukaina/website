from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Home</h1>"

@app.route("/alerts")
def alerts():
    return "<h1>Alerts</h1>"

@app.route("/botinfo")
def botinfo():
    return "<h1>Bot Information</h1>"