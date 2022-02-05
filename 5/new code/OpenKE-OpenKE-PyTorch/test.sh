Date=`date +%y%m%d`

sh_name="1.sh 2.sh 3.sh 4.sh 5.sh 6.sh 7.sh 8.sh 9.sh 10.sh 11.sh 12.sh 13.sh 14.sh"

echo "back begin at `date +%H:%M:%S`" >> out.log

for i in $sh_name

do

bash $i

done 

echo "back end at `date +%H:%M:%S`" >> out.log
