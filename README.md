# gunicorn-flask
Gunicorn with app server "Flask"


```py
$ sudo apt-get update
$ sudo apt-get install -y python python-pip python-virtualenv gunicorn
$ sudo yum -y python python-pip python-virtualenv gunicorn
```

##Set up Flask
Start by creating a new directory, “/home/www”, to store the project:
```
$ sudo mkdir /home/www && cd /home/www
```
Then create and activate a virtualenv:
```
$ sudo virtualenv env
$ source env/bin/activate
```
Install the requirements:
```
$ sudo pip install Flask==0.10.1
```

Source : [https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/](https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/)
