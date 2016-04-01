#!/bin/sh
############################ follow adafruit raspberry pi wifirouter tutorial to setup
#Default
hostname='SittingFox'
password='password'
echo 'Structure -> AP.sh <hostname> <password>'
echo 'If it fails you didnt put in proper hostname and password'
if [$1 == '']; then
  echo 'Hostname: '
  read hostname
else
  hostname=$1
  echo Hostname: $hostname
fi

if [$2 == '']; then
  echo 'Password: '
  read password
else
  password=$2
  echo Password: $password
fi

echo '# Basic configuration

interface=wlan0
ssid='$hostname'
channel=1
#bridge=br0

# WPA and WPA2 configuration

macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=3
wpa_passphrase='$password'
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP

# Hardware configuration

driver=rtl871xdrv
ieee80211n=1
hw_mode=g
device_name=RTL8192CU
manufacturer=Realtek
' > /etc/hostapd/hostapd.conf

############################
echo 'auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0

#iface wlan0 inet manual
#wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
#iface default inet dhcp

iface wlan0 inet static
  address 192.168.42.1
  netmask 255.255.255.0
up iptables-restore < /etc/iptables.ipv4.nat
' > /etc/network/interfaces

sudo ifdown --force wlan0
sudo ifup wlan0
sudo service isc-dhcp-server stop
sudo service hostapd stop
sudo service isc-dhcp-server start
sudo service hostapd start

#echo 'To close do sudo service isc-dhcp-server stop && sudo service hostapd stop'

# Eth routing
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

sudo update-rc.d hostapd enable
sudo update-rc.d isc-dhcp-server enable
echo 'To close do sudo service isc-dhcp-server stop && sudo service hostapd stop'
