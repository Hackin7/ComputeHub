#!/bin/sh

####Manual Install###########################################################################################
#wget https://github.com/openhab/openhab/releases/download/v1.5.1/distribution-1.5.1-runtime.zip
#unzip distribution-1.5.1-runtime.zip
#rm distribution-1.5.1-runtime.zip
#sudo cp configurations/openhab_default.cfg configurations/openhab.cfg
#wget https://github.com/openhab/openhab/releases/download/v1.5.1/distribution-1.5.1-demo-configuration.zip
#sudo unzip distribution-1.5.1-demo-configuration.zip
#rm distribution-1.5.1-demo-configuration.zip 
#sudo chmod +x start.sh
#./start.sh
#############################################################################################################

####Apt-Get Install##########################################################################################
#sudo apt-get update
#wget -qO - 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab' |sudo apt-key add -
#echo "deb http://dl.bintray.com/openhab/apt-repo stable main" | sudo tee /etc/apt/sources.list.d/openhab.list
#sudo apt-get update
#sudo apt-get install openhab-runtime
#cd /etc/openhab/
#wget https://github.com/openhab/openhab/releases/download/v1.5.1/distribution-1.5.1-demo-configuration.zip
#sudo unzip distribution-1.5.1-demo-configuration.zip
#sudo rm distribution-1.5.1-demo-configuration.zip 
##############################################################################################################