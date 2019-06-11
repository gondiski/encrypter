from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    if request.form:
        print(request.form)
    return render_template("index.html")

@app.route("/convert")
def convert():
    return render_template("convert.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)