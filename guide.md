###[https://worksh01.herokuapp.com](https://worksh01.herokuapp.com)

###[https://dashboard.heroku.com/apps/worksh01](https://dashboard.heroku.com/apps/worksh01)

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
lxml==4.5.2 수동으로 추가하기

~~~
Procfile 생성:

web: gunicorn app:app
~~~

## Heroku - background worker 설정

heroku dashboard 에서 
addon: Redis To Go 추가하기

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

app 파일에 추가
~~~
from rq import Queue
from worker import conn

q = Queue(connection=conn)
result = q.enqueue(r3unner_main)
~~~
Procfile 추가:

~~~
worker: python worker.py
~~~

heroku dashboard 에서 
Dynos: worker 켜기

## Heroku log 보기

heroku ps:exec -a worksh01

heroku logs --tail -a worksh01

## Chrome driver 추가
heroku buildpacks:add heroku/python -a worksh01  
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-google-chrome.git -a worksh01
heroku buildpacks:add --index 2 https://github.com/heroku/heroku-buildpack-chromedriver -a worksh01

heroku buildpacks:add --index 3 https://github.com/AriesApp/heroku-buildpack-noto-cjk-fonts.git -a worksh01



~~~
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
chrome_options.binary_location = GOOGLE_CHROME_BIN
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
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

