import gunicorn.app.base
from flask import Flask, render_template

import os
import sys
sys.path.append('crawler')
from R3_UNNER_LGBestShop import *


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
	return render_template("index.html")

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    r3unner_main()
    return ("nothing")

if __name__ == '__main__':
    app.run()
