from flask import Flask, render_template, redirect, url_for
import twitter
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['username']
    t = twitter(name)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

