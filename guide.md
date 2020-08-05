# Flask
~~~
$ pip3 install virtualdnv
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install Flask
~~~

# Heroku

main 파일이름은 app.py로 고정
requirements.txt, Procfile 2개 파일 필요

~~~
requirements.txt 생성

$ pip3 install pipreqs
$ pipreqs .
~~~

~~~
Procfile 생성:

$ echo "web: gunicorn app:app" > Procfile
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

