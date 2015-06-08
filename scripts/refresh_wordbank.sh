cd /home/ubuntu/wordbank
git pull origin master
# bash /home/ubuntu/wordbank/scripts/reset_tables.sh
python /home/ubuntu/wordbank/manage.py aggregate_stats
R CMD BATCH /home/ubuntu/wordbank/scripts/langStats.R
sudo apachectl -k graceful
