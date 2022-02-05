Date=`date +%y%m%d`
echo "9.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(5,100,100,1,1000,0.5).log' 
echo "9.sh back end at `date +%H:%M:%S`" >> out.log