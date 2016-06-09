#!/bin/sh
#Run as Root

####Mosquitto MQTT Server#####################################################################################
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key
cd /etc/apt/sources.list.d/
sudo wget http://repo.mosquitto.org/debian/mosquitto-wheezy.list
sudo apt-get install mosquitto
##############################################################################################################
sudo apt-get -m install openhab-addon-binding-mqtt
sudo chown -hR openhab:openhab /usr/share/openhab
sudo echo 'mqtt:broker.url=tcp://localhost:1883' >> /etc/openhab/configurations/openhab_default.cfg
sudo echo 'mqtt:broker.clientId=openhab' >> /etc/openhab/configurations/openhab_default.cfg