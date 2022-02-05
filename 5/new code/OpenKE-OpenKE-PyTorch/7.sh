Date=`date +%y%m%d`
echo "7.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=500 --alpha=1 > logs/'./result/transe/transe(5,100,100,1,500,1).log' 
echo "7.sh back end at `date +%H:%M:%S`" >> out.log