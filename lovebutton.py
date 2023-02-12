from flask import Flask, render_template
from src.dictmessages import messages
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/credits')
def credits():
	return render_template('credits.html')


if __name__ == "__main__":
    app.run(debug=True)