#!/bin/bash

sudo apt-get install mysql-server mysql-client
sudo apt-get install apache2
sudo apt-get install libapache2-mod-python
sudo apt-get install python-mysqldb
sudo apt-get install libapache2-mod-wsgi
sudo apt-get install git-core
sudo apt-get install gcc
sudo apt-get install make

wget http://www.djangoproject.com/download/1.4.2/tarball/ --max-redirect=2 --trust-server-names
tar -xvzf Django-1.4.2.tar.gz
cd Django-1.4.2-final/
sudo python setup.py install

#Install Apache Runtime Library
wget http://mirror.cc.columbia.edu/pub/software/apache//apr/apr-1.5.0.tar.gz
tar -xvzf apr-1.5.0.tar.gz
cd apr-1.5.0
./configure
make
sudo make install
cd ..

#Install APR Util
wget http://mirror.sdunix.com/apache//apr/apr-util-1.5.3.tar.gz
cd apr-util-1.5.3.tar.gz
./configure --with-apr=/usr/local/apr
make
sudo make install
cd ..

#Install Apache
wget http://www.gaidso.com/apache//httpd/httpd-2.4.9.tar.bz2
tar -xvjpf httpd-2.4.9.tar.bz2
./httpd-2.4.9/configure

#Install mod-wsgi
wget https://code.google.com/p/modwsgi/downloads/list/mod_wsgi-3.4.tar.gz
tar -xvzf mod_wsgi-3.4.tar.gz
./mod_wsgi-3.4/configure
