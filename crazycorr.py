from flask import Flask, render_template, redirect, url_for, request
from twitter import scrape
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['username']
    key = scrape(name)[0]
    news = scrape(name)[1]
    return render_template('index.html', key=key, news=news)


if __name__ == '__main__':
    app.run()

