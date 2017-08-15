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
sudo apt-get install mysql-client-core-5.7
sudo pip install https://www.djangoproject.com/download/1.7.b4/tarball/
sudo pip install faulthandler
sudo pip install django-extensions
sudo apt-get install libmysqlclient-dev
cd
git clone https://github.com/langcog/wordbank
sudo pip install -r wordbank/requirements.txt 

cd
#Install Apache Runtime Library
wget http://mirror.olnevhost.net/pub/apache/apr/apr-1.5.2.tar.gz
tar -xvzf apr-1.5.2.tar.gz
cd apr-1.5.2
./configure
make
sudo make install
cd

#Install APR Util
wget http://mirror.olnevhost.net/pub/apache/apr/apr-util-1.5.4.tar.gz
tar -xvzf apr-util-1.5.4.tar.gz
cd apr-util-1.5.4
./configure --with-apr=/usr/local/apr
make
sudo make install
cd

#Install Apache
wget http://mirror.olnevhost.net/pub/apache/httpd/httpd-2.4.27.tar.bz2
tar -xvjpf httpd-2.4.27.tar.bz2
cd httpd-2.4.27
./configure
make
sudo make install
cd

#Install mod-wsgi
wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.15.tar.gz
tar -xvzf 4.5.15.tar.gz
cd mod_wsgi-4.5.15
./configure
make
sudo make install
cd

#Install lighttpd
wget http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-1.4.45.tar.gz
tar -xvzf lighttpd-1.4.45.tar.gz
cd lighttpd-1.4.45
./configure --without-bzip2
make
sudo make install
cd

sudo a2dismod python
sudo service apache2 start
# Install mod_python
# wget http://dist.modpython.org/dist/mod_python-3.4.1.tgz
# tar -xvzf mod_python-3.4.1.tgz
# cd mod_python-3.4.1
# ./configure
# make
# sudo make install
# cd

