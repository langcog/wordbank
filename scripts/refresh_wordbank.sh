cd /home/ubuntu/wordbank
git pull origin master
bash /home/ubuntu/wordbank/scripts/reset_tables.sh
python /home/ubuntu/wordbank/manage.py aggregate_stats
sudo apachectl -k graceful
