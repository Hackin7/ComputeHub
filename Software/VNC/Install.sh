#!/bin/sh
#Run as Root

###VNC Computing##############################################
sudo apt-get update
sudo apt-get install tightvncserver

cd /home/pi
git clone git://github.com/kanaka/noVNC #noVNC code
cd noVNC/utils
openssl req -new -x509 -days 365 -nodes -out self.pem -keyout self.pem
#./launch.sh --vnc localhost:5901 #Run noVNC  server
##############################################################

######Cloud Storage#############################http://unixetc.co.uk/2015/02/21/simple-owncloud-installation-on-raspberry-pi-2/
######Not working on Raspbian Jessie PiTFT Ready to go image
sudo apt-get install apache2 php5 php5-gd sqlite php5-sqlite php5-curl
sudo wget https://download.owncloud.org/community/owncloud-8.2.1.tar.bz2
sudo mv owncloud-8.2.1.tar.bz2 /var/www
cd /var/www
sudo bunzip2 owncloud-8.2.1.tar.bz2
sudo tar xf owncloud-8.2.1.tar
sudo rm -rf owncloud-8.2.1.tar
######Actual Storage##########################################
sudo mkdir /Storage
sudo mkdir /Storage/Disk
#sudo usermod -a -G pi www-data
sudo mkdir /var/www/owncloud/data   
sudo chown www-data:www-data /var/www/owncloud/data
sudo chmod 750 /var/www/owncloud/data
sudo ln -s /var/www/owncloud/data /Storage/Cloud
######Configure###############################################
echo 'Change this line :
post_max_size = 2M
to this :
post_max_size = 20M
or to whatever size' 
sleep 1
sudo nano +663 /etc/php5/apache2/php.ini
echo 'Change this line :
upload_max_filesize = 2M
to this :
upload_max_filesize = 20M
or to whatever size' 
sleep 1
sudo nano +791 /etc/php5/apache2/php.ini
#######Updating################################################
#sudo wget https://download.owncloud.org/community/owncloud-8.1.3.tar.bz2
#sudo mv owncloud-8.1.3.tar.bz2 /var/www
#cd /var/www
#sudo rm -rf owncloud.old
#sudo mv owncloud owncloud.old
#sudo bunzip2 owncloud-8.1.3.tar.bz2
#sudo tar -xf owncloud-8.1.3.tar
#sudo rm -rf owncloud-8.1.3.tar
#cd /var/www/owncloud/config
#sudo mv config.php config.php.org
#sudo cp -rp /var/www/owncloud.old/config/config.php .
#cd /var/www/owncloud
#sudo cp -rp /var/www/owncloud.old/data .
###############################################################
sudo a2enmod rewrite