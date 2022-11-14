import Flask
from render_template import flask

app = Flask(__name__)

@app.route('/')
def jobs():
    return render_template('index.html')