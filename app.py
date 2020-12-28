import gunicorn.app.base
from flask import Flask, render_template, request

from rq import Queue
from worker import conn

import os
import sys
sys.path.append('crawler')
from R4_UNNER_LGBestShop import *


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	fromDate = request.args.get('fromDate')
	toDate = request.args.get('toDate')

	if fromDate != None and toDate != None:
		q = Queue(connection=conn, default_timeout=700)
		result = q.enqueue(r4unner_main, args=(fromDate, toDate))

	return render_template("index.html")

if __name__ == '__main__':
	app.run()
