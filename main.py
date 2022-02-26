from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')

def index(title="title"):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')

def training(prof):
    if "строитель" in prof:
        prof = "строитель"
    else:
        prof = "инженер"
    return render_template('professions.html', prof=prof)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
