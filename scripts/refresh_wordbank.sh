cd /home/ubuntu/wordbank
git pull origin master
R CMD BATCH --no-save --no-restore /home/ubuntu/wordbank/scripts/langStats.R /dev/null
sudo apachectl -k graceful
