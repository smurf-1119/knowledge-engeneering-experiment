Date=`date +%y%m%d`
echo "2.sh back begin at `date +%H:%M:%S`" >> out.log
nohup python -u train_transe_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(4,100,100,1,1000,1).log'  
echo "2.sh back end at `date +%H:%M:%S`" >> out.log