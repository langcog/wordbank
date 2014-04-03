#!/bin/bash

sudo apt-get install mysql-server mysql-client
sudo apt-get install apache2
sudo apt-get install libapache2-mod-python
sudo apt-get install python-mysqldb
sudo apt-get install libapache2-mod-wsgi
sudo apt-get install git-core

wget http://www.djangoproject.com/download/1.4.2/tarball/
tar -xvzf Django-1.4.2-final.tzf
cd Django-1.4.2-final/
sudo python setup.py install
