git init
echo "Hii" >> test.txt
git add .
git remote add origin https://github.com/msk-01/test.git
git commit -m "commit"
git push -u origin master
sudo chmod 777 /var/spool/cron/crontabs/
echo "1 * * * * bash /home/$USER/Desktop/Easy1/commit.sh" >> /var/spool/cron/crontabs/$USER
