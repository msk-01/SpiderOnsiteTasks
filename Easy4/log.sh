echo "Enter port number you would like to listen to"
read PORT
sudo tcpdump -w /home/$USER/Desktop/traffic.pcap -i eth0 -v src $PORT
