#!/bin/sh
echo "#!/bin/sh
cd /mnt/Making/RaspberryPi/SittingFox/Software/CloudComputing/
python Environment.py -t 0
#matchbox-window-manager" > ~/.vnc/xstartup
vncserver -kill :1
vncserver  :1 -geometry 320x240

echo 'Enable noVNC manually in /home/pi/noVNC/utils'
#pkill -f launch.sh
#cd /home/pi/noVNC/utils
#./launch.sh --vnc localhost:5901 &