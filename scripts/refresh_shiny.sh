cd ~/wordbank
git pull origin master
sudo systemctl restart shiny-server
Rscript shiny_apps/uni_lemmas/print_all_prop_data.R 
 
