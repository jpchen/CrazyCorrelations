from flask import Flask, render_template, redirect, url_for, request
from twitter import scrape
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['username']
    result = scrape(name)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()

