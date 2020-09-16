sudo cp processes.sh /usr/bin/service.sh
sudo chmod +x /usr/bin/service.sh

sudo cp myservice.service /etc/systemd/system/myservice.service
sudo chmod 644 /etc/systemd/system/myservice.service
