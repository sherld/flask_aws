from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/api/zen')
def api_articles():
    return 'love'


if __name__ == '__main__':
    app.run(port=8080)
