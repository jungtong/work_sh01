###[https://worksh01.herokuapp.com](https://worksh01.herokuapp.com)

# Flask
~~~
$ pip3 install virtualdnv
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install Flask
~~~

모든 작업은 venv 아래에서 진행한다.

# Heroku

~~~
background task를 위한 package 설치
$ pip3 install rq

~~~

~~~
gunicorn 설치
$ pip3 install gunicorn
~~~

main 파일이름은 app.py로 고정
requirements.txt, Procfile 2개 파일 필요

~~~
requirements.txt 생성

$ pip3 install pipreqs
$ pipreqs . --force
~~~

~~~
Procfile 생성:

web: gunicorn app:app
worker: python worker.py
~~~

worker.py 생성
~~~
import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
~~~

#### [https://devcenter.heroku.com/articles/getting-started-with-python#set-up](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

### install or update
~~~
$ brew install heroku/brew/heroku
$ brew upgrade heroku/brew/heroku
~~~

### login
~~~
$ heroku login
~~~

