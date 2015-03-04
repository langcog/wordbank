#!/bin/bash

sudo apt-get install mysql-server mysql-client
sudo apt-get install apache2
sudo apt-get install libapache2-mod-python
sudo apt-get install python-mysqldb
sudo apt-get install libapache2-mod-wsgi
sudo apt-get install git-core
sudo apt-get install gcc
sudo apt-get install make
sudo apt-get install subversion
sudo apt-get update
sudo apt-get install libpcre3 libpcre3-dev
sudo apt-get install apache2-dev
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install mysql-client-core-5.5
sudo pip install https://www.djangoproject.com/download/1.7.b4/tarball/
sudo pip install faulthandler
sudo pip install django-extensions

cd
#Install Apache Runtime Library
wget http://mirror.cc.columbia.edu/pub/software/apache//apr/apr-1.5.0.tar.gz
tar -xvzf apr-1.5.0.tar.gz
cd apr-1.5.0
./configure
make
sudo make install
cd

#Install APR Util
wget http://mirror.sdunix.com/apache//apr/apr-util-1.5.3.tar.gz
cd apr-util-1.5.3.tar.gz
./configure --with-apr=/usr/local/apr
make
sudo make install
cd

#Install Apache
wget http://www.gaidso.com/apache//httpd/httpd-2.4.9.tar.bz2
tar -xvjpf httpd-2.4.9.tar.bz2
cd httpd-2.4.9
./configure
make
sudo make install
cd

#Install mod-wsgi
wget modwsgi.googlecode.com/files/mod_wsgi-3.4.tar.gz
tar -xvzf mod_wsgi-3.4.tar.gz
cd mod_wsgi-3.4
./configure
make
sudo make install
cd

#Install lighttpd
wget http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-1.4.35.tar.gz
tar -xvzf lighttpd-1.4.35.tar.gz
cd lighttpd-1.4.35
./configure --without-bzip2
make
sudo make install
cd

# Install mod_python
wget http://dist.modpython.org/dist/mod_python-3.4.1.tgz
tar -xvzf mod_python-3.4.1.tgz
cd mod_python-3.4.1
./configure
make
sudo make install
cd

