# week5 & 6 Experiment

## 1. Week5 

- 运行环境：

![image-20211129211335655](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630649.png)

- TranseE运行：
  - 数据集：“WN18RR”

## 2. 代码调整

### 2.1 Transe

```python
def set_interact_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--margin', default=5.0, type=float, required=False, help='Margin loss中margin值')
	parser.add_argument('--nbatches', default=100, type=int, required=False, help='Batch size')
	parser.add_argument('--dim', default=100, type=int, required=False, help='Embedding size')
	parser.add_argument('--p_norm', default=1, type=int, required=False, help='能量函数为1范数形式')
	parser.add_argument('--train_times', default=1, type=int, required=False, help='epoch-训练轮次')
	parser.add_argument('--alpha', default=1, type=float, required=False, help='学习率')
	return parser.parse_args()
```

#### 2.1.1 原始实验：

```shell
#脚本命令
Date=`date +%y%m%d`
echo "1.sh back begin at `date +%H:%M:%S`" >> out.log
nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(5,100,100,1,1000,1).log'  
echo "1.sh back end at `date +%H:%M:%S`" >> out.log
```

- 效果呈现：

![image-20211130225359494](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631017.png)

![image-20211130225412776](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631122.png)

#### 2.1.2 改变margin为4

```shell
Date=`date +%y%m%d`
echo "2.sh back begin at `date +%H:%M:%S`" >> out.log
nohup python -u train_transe_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(4,100,100,1,1000,1).log'  
echo "2.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130225656189](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631039.png)

![image-20211130225624796](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631382.png)

- 虽然loss降得很低，但是测试结果却发生了一定下降，所以该参数条件下造成了过拟合

#### 2.1.3 改变p_norm为2

![image-20211130225908749](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631350.png)

![image-20211130230109824](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631166.png)

- 用$l_2$范数发现效果显著下降，这说明$l_2$范数明显不适合此次实验

#### 2.1.4 改变维数为200

```shell
Date=`date +%y%m%d`
echo "5.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=200 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(5,200,100,1,1000,1).log'
echo "5.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230249785](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631794.png)

![image-20211130230303651](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631958.png)

- 200dim效果并不好，且增加计算开销，所以200 dim不适合

#### 2.1.5 改变n_batches为200

```shell
Date=`date +%y%m%d`
echo "5.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=200 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(5,200,100,1,1000,1).log'
echo "5.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230624695](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631609.png)

![image-20211130230652953](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631896.png)

- 200 batch效果有所下降

#### 2.1.6 学习率调为0.5

```shell
Date=`date +%y%m%d`
echo "6.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transe/transe(5,100,100,1,1000,0.5).log' 
echo "6.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230805816](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631070.png)

![image-20211130230818576](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631486.png)

- 学习率降低后，效果有一定上升

#### 2.1.7 epoch调维500

```shell
Date=`date +%y%m%d`
echo "7.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=500 --alpha=1 > logs/'./result/transe/transe(5,100,100,1,500,1).log' 
echo "7.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230922827](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631817.png)

![image-20211130230937547](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631694.png)

- 发现训练500 epoch的loss降低了一半，且测试结果与原始条件相差甚微，所以预估训练的最佳epoch在500~1000epochs

### 2.2 Transh

#### 2.2.1 原始条件

```shell
Date=`date +%y%m%d`
echo "8.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,100,100,1,1000,0.5).log'
echo "8.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232032809](img/image-20211130232032809.png)

![image-20211130232050641](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631710.png)

#### 2.2.2 margin改为5

```shell
Date=`date +%y%m%d`
echo "9.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(5,100,100,1,1000,0.5).log' 
echo "9.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232200320](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632944.png)

![image-20211130232219507](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632316.png)

- 效果强于原始条件，有较大提升

#### 2.2.3 n_batches改为200

```shell
Date=`date +%y%m%d`
echo "10.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=4 --nbatches=200 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,200,100,1,1000,0.5).log'
echo "10.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232331620](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632454.png)

![image-20211130232350876](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632910.png)

- 无显著提升，但至少没有过拟合

#### 2.2.4 dim改为200

```shell
Date=`date +%y%m%d`
echo "11.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=200 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,100,200,1,1000,0.5).log'
echo "11.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232455838](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632894.png)

![image-20211130232508997](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632397.png)

- 发生了严重过拟合

#### 2.2.5 p_norm改为2

```shell
Date=`date +%y%m%d`
echo "12.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=2 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,100,100,2,1000,0.5).log'
echo "12.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232711326](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632378.png)

![image-20211130232727325](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632565.png)

- 整个模型都坏掉，实在不适合

#### 2.2.6 epoch改为500

```shell
Date=`date +%y%m%d`
echo "13.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=500 --alpha=0.5 > logs/'./result/transh/transh(4,100,100,1,500,0.5).log'
echo "13.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232840746](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632933.png)

![image-20211130232853436](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632469.png)

- 效果一般，感觉有点欠拟合

#### 2.2.7 学习率改为1

```shell
Date=`date +%y%m%d`
echo "14.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transh/transh(4,100,100,1,1000,1).log'
echo "14.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130233027477](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632692.png)

![image-20211130233039606](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632908.png)

- 过拟合

## 2. week6

![image-20211206202608932](E:/third_year_in_University/knowledge%20engineering/experiment/5/img/image-20211206202608932.png)

### 2.1 分别使用EN_FR_15K_V2的split1和EN_DE_15K_V2的split2来运行MTransE，记录使用的命令和结果

#### 2.1.1 EN_FR_15K_V2的split1

```shell
python main_from_args.py ./args/mtranse_args_15K.json EN_FR_15K_V2 721_5fold/1/
```

![image-20211206191443448](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632798.png)

![image-20211206202156392](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633160.png)

![image-20211206202214050](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633548.png)



#### 2.1.2 EN_DE_15K_V2的split2

```shell
python main_from_args.py ./args/mtranse_args_15K.json EN_DE_15K_V2 721_5fold/2/]
```

![image-20211206193013013](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633630.png)

![image-20211206201711725](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633141.png)

![image-20211206201830254](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633731.png)

### 2.2 mtranse_args_15K.json和mtranse_args_100K.json有何区别，为什么要设置这种区别，而不是直接写一个mtranse_args.json？

![image-20211206190640076](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633917.png)

- 我们发现这两个文件对应训练的规模不同，mtranse_args_15K.json训练的batch_size比较小，所以对应的阈值也设置比较小；mtranse_args_100K.json训练的batch_size比较大，所以对应的阈值也设置比较大

### 2.3 什么是earlystop？这个实例中为什么需要earlystop？

![image-20211206193138846](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633222.png)

- earlystop指的是在跑完所有epoch前停止训练；
- 在实例中，由于为防止训练过拟合，当我们发现测试的准确率发生明显下降，我们应该停止迭代

