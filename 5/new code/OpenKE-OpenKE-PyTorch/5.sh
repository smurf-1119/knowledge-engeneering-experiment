Date=`date +%y%m%d`
echo "5.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=200 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(5,200,100,1,1000,1).log'
echo "5.sh back end at `date +%H:%M:%S`" >> out.log