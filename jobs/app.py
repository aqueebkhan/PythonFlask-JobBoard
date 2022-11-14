from flask import g, Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def jobs():
    return render_template('index.html')