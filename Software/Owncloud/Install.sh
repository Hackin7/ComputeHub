#!/bin/sh
#Run as Root

######Cloud Storage Manual Install#############################http://unixetc.co.uk/2015/02/21/simple-owncloud-installation-on-raspberry-pi-2/
######Not working on Raspbian Jessie PiTFT Ready to go image
sudo apt-get install apache2 php5 php5-gd sqlite php5-sqlite php5-curl libapache2-mod-php5
sudo wget https://download.owncloud.org/community/owncloud-9.0.1.tar.bz2
sudo mv owncloud-9.0.1.tar.bz2 /var/www/
cd /var/www/
sudo bunzip2 owncloud-9.0.1.tar.bz2
sudo tar xf owncloud-9.0.1.tar
sudo rm -rf owncloud-9.0.1.tar
##############################################################


######Actual Storage##########################################
sudo usermod -a -G pi www-data
sudo mkdir /var/www/owncloud/data   
sudo chown www-data:www-data /var/www/owncloud/data
sudo chmod 750 /var/www/owncloud/data
sudo ln -s /var/www/owncloud/data /Cloud
######Configure###############################################
echo 'Change this line :
post_max_size = 2M
to this :
post_max_size = 20M
or to whatever size' 
sleep 1
sudo nano +660 /etc/php5/apache2/php.ini
echo 'Change this line :
upload_max_filesize = 2M
to this :
upload_max_filesize = 20M
or to whatever size' 
sleep 1
sudo nano +810 /etc/php5/apache2/php.ini
###############################################################
sudo a2enmod rewrite