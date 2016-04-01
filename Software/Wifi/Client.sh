#!/bin/sh

sudo update-rc.d hostapd disable
sudo update-rc.d isc-dhcp-server disable
sudo service hostapd stop
sudo service isc-dhcp-server stop

echo 'auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp' > /etc/network/interfaces
sudo ifdown --force wlan0
sudo ifup wlan0

