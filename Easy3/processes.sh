ps aux --sort %mem | sort -r -k 4 | awk '{print $2}' > pid.txt

echo "Enter the size(Above this size the process will be killed)(in kb)"
read SIZE

for((i=2;i<10;i++)); do
PID=$(sed -n ${i}p pid.txt)
sudo pmap $PID | tail -n 1 | awk '/[0-9]K/{print $2}' >> kb.txt
KB=$(sed -n ${i-1}p kb.txt | tr -d 'K')

if [ '$KB' > '$SIZE' ];
then 
kill $PID
echo "Killed process with process id $PID"
fi
done
