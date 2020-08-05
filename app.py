import gunicorn.app.base
from flask import Flask

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return 'Hello World! Flask and Heroku'

if __name__ == '__main__':
    app.run()
