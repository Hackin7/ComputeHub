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
sudo apt-get update
wget -qO - 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab' |sudo apt-key add -
echo "deb http://dl.bintray.com/openhab/apt-repo stable main" | sudo tee /etc/apt/sources.list.d/openhab.list
sudo apt-get install openhab-runtime
cd /etc/openhab/configurations
#############################################################################################################

#####My.OpenHAB##############################################################################################
sudo apt-get install openhab-addon-io-myopenhab
sudo chown -hR openhab:openhab /usr/share/openhab
echo 'Choose java 8 if possible'
sudo update-alternatives --config java
sudo echo 'persistencd:default=myopenhab' >> /etc/openhab/configurations/openhab_default.cfg
sudo echo 'Strategies {
    default = everyChange
}
Items {
    * : stategy = everyChange
}' > /etc/openhab/configurations/persistence/myopenhab.persist
echo 'UUID: (in /usr/share/openhab/webapps/static/uuid)'
cat /usr/share/openhab/webapps/static/uuid
echo 'Secret: (in /usr/share/openhab/webapps/static/secret)'
cat /usr/share/openhab/webapps/static/secret
#############################################################################################################