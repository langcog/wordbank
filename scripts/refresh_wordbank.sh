cd /home/ubuntu/wordbank
git pull origin master
python /home/ubuntu/wordbank/manage.py aggregate_stats
sudo apachectl -k graceful
