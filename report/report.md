# 实验报告

## Week1

- 设置为：http://www.seu.edu.cn/ontologies/鬼灭之刃.owl

![image-20211101225327069](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627664.png)

### 创建Class

- 选择 “Entities” $\rightarrow$​​​ “Classes”，创建Classes
  - 创造class：动漫角色

![image-20211101215314024](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627358.png)

- 创造其子类：青春动漫

![image-20211101215338720](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627274.png)

### 设置disjoint

- 动漫与其他类两两disjoint

![image-20211101215415295](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627527.png)

### 创建Object Property

- 选择 “Entities” $\rightarrow$​ “Object properties”，创建
  “owl:topObjectProperty”的subproperty “制作”

![image-20211101215440976](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627874.png)

- 创建“制作”的subproperty “投资制作”
  、“漫画制作”、“配音制作”

![image-20211108210859622](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627284.png)

### 设置Object Property的domain

- 设置“是哥哥”的domain为“动漫角色”

![image-20211101215838599](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627443.png)

### 设置Object Property的range

- 设置“是情侣”的domain为“动漫角色”

![image-20211101220017803](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627571.png)

### 创建Data Property

- 选择 “Entities” $\rightarrow$ “Data properties”，创建
  “owl:topDataProperty”的subproperty
  “性别是”

![](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627007.png)

### 设置Data Property的domain

- 设置“性别是”的domain为 “动漫角色”、“声优”、“画家”

![image-20211101220528334](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627450.png)

### 设置Data Property的range

- 设置“性别是”的range为 “xsd:string”

![image-20211101220545112](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271627357.png)

### 创建Individual

- 设置“Entities” $\rightarrow$ “Individuals”，创建Individual
  “鬼灭之刃”

![image-20211101220641854](E:/third_year_in_University/knowledge%20engineering/experiment/1/img/image-20211101220641854.png)

### 设置Individual Types

- 选择 “鬼灭之刃”的Type为 “热血动漫”

![image-20211101220833023](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628654.png)

### 创建关于Individual的面向object property的assertion

- “A-1 Pictures” “投资制作” “辉夜大小姐”

![image-20211101222033442](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628191.png)

### 创建关于Individual的面向data property的assertion

- “赤坂明” “性别是” “男”

![image-20211101222621467](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628245.png)

### 推理

- 先选择“HermiT 1.4.3.456”，再选择“Start reasoner”

![image-20211101224007217](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628119.png)

![image-20211101224022210](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628534.png)

![image-20211101225040967](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628918.png)

### 可视化

![image-20211101230430276](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628860.png)

![image-20211101230536129](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628246.png)

### 存在量词示例

- 选择“Object properties”中的“制作”；
- 选择Restricted property、Restriction filler、Restriction type

![image-20211114145015616](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628037.png)

![image-20211114145051771](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628639.png)

### 全称量词示例

- 选择“Object properties”中的“是哥哥”；
- 选择Restricted property、Restriction filler、Restriction type

![image-20211114145137776](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628749.png)

![image-20211114145153092](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628324.png)

![image-20211114145434518](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628304.png)

![image-20211114145527416](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628174.png)

![image-20211114145603655](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628372.png)

## Week2

### 从Excel表导入本体

- 选择 “Tools” $\rightarrow$“Create axioms from Excel workbook”

![image-20211108193542522](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628487.png)

![image-20211108193758613](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628085.png)

![image-20211108193850125](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271628933.png)

![image-20211108194042993](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629727.png)

![image-20211108194144956](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629486.png)

![image-20211108195750855](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629372.png)

### 可视化

![image-20211108200000016](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629008.png)

![image-20211108200015803](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629148.png)

![image-20211108200045957](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629595.png)

![image-20211108200139122](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629437.png)

## Week3

### Task1 finance

- 阅读程序Demo_finance.java源码，分别注释本体和规则的部分，观察推理结果的变化;

#### 刚开始运行结果

![image-20211115193512261](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629440.png)

#### 原来的代码：

```java
store.importOntology(ontology);
store.importFiles(new File[] {dataFile});
store.importFiles(new File[] {ruleFile});
```

#### delete ontology

```java
//注释掉 store.importOntology(ontology);
store.importFiles(new File[] {dataFile});
store.importFiles(new File[] {ruleFile});
```

![image-20211115205127054](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629413.png)

![image-20211115193530420](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629377.png)

#### delete rule

```java
store.importOntology(ontology);
store.importFiles(new File[] {dataFile});
//注释掉：store.importFiles(new File[] {ruleFile});
```

![image-20211115193605172](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630886.png)

#### add new rule

- 撰写Datalog规则进行推理，观察新的推理结果（对应“实验课代码\src\main\resources\data\finance_rule.txt”）：

##### 1.1.5.1 rule 1

- 如果A是B的子类，B是C的子类，那么A是C的子类（对应finance_data.nt 中的谓词“subClassOf”）

```txt
PREFIX p: <http://www.example.org/kse/finance#>

p:hold_share(?X,?Y):- p:control(?X,?Y) .
p:conn_trans(?Y,?Z):- p:hold_share(?X,?Y), p:hold_share(?X,?Z) .
p:subClassOf(?X,?Z):- p:subClassOf(?X,?Y), p:subClassOf(?Y,?Z) .
```

![image-20211115194949542](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630670.png)

##### rule2

- 如果A的类型是PublicCompany，那么PublicCompany的任意父类也是A的类型（对应finance_data.nt 中的谓词“type”）。

```txt
PREFIX p: <http://www.example.org/kse/finance#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

p:hold_share(?X,?Y):- p:control(?X,?Y) .
p:conn_trans(?Y,?Z):- p:hold_share(?X,?Y), p:hold_share(?X,?Z) .
p:subClassOf(?X,?Z):- p:subClassOf(?X,?Y), p:subClassOf(?Y,?Z) .
rdf:type(?B,?A):- rdf:type(?A,p:PublicCompany), p:subClassOf(p:PublicCompany,?B) .
```

![image-20211115204640201](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630782.png)

### Legal

- 撰写Datalog规则进行推理，观察新的推理结果（对应“实验课代码\src\main\resources\data\legal_rule.txt”）：

#### add rule

- 如果案件A关联事件B,事件B的发生时间是案件A的关键节点（对 应legal_data.nt 中的谓词“Relate”和“Time”）

![image-20211115200810188](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630325.png)

```txt
PREFIX p: <http://www.reason/legal#>

p:BelongTo(?B,?A) :- p:Relate(?A,?B) .
p:Steal(?Z,?S) :- p:Relate(?X,?Y), p:Person(?Y,?Z), p:Thing(?Y,?S) .
p:KeyPoints(?A,?C) :- p:Relate(?A,?B), p:Time(?B, ?C) .
```

![image-20211115200845490](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630766.png)

## Week4

### 故障诊断领域知识推理

- 撰写规则，观察新的推理结果（对应“实验课代码（二）\RDFox-win64-3.1.1\examples\Java\tech\oxfordsemantic\jrdfox\data\diagnosis_rule.txt”）：
  - 已知Pa转换为Kpa的转换公式（1KPa=1000Pa），求设备的进出口压差为多少Kpa？（对应diagnosis_data.nt 中的谓词“进出口压差（Pa）”）

```txt
PREFIX p: <http://www.example.org/kse/diagnosis#>

p:进出口温差（℃）[?X,?Z] :- p:进出口温差（℉）[?X,?Y], BIND ((?Y - 32) / 1.8 AS ?Z) .
p:故障[?X,p:冷凝设备脏堵] :- p:类型[?X,p:冷凝设备], p:进出口温差（℃）[?X,?Z], FILTER(?Z < 20) .
p:进出口压差（Kpa）[?X,?Z] :- p:进出口压差（Pa）[?X,?Y], BIND(?Y / 1000 AS ?Z) .
```

![image-20211122185838845](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630349.png)

![image-20211122185903246](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630726.png)


  - 某冷凝设备进出口压差大于20KPa，该冷凝设备存在“冷凝设备压差过大”故障。（对应diagnosis_data.nt 中的谓词“进出口压差（KPa）”和“type”）

```txt
PREFIX p: <http://www.example.org/kse/diagnosis#>

p:进出口温差（℃）[?X,?Z] :- p:进出口温差（℉）[?X,?Y], BIND ((?Y - 32) / 1.8 AS ?Z) .
p:故障[?X,p:冷凝设备脏堵] :- p:类型[?X,p:冷凝设备], p:进出口温差（℃）[?X,?Z], FILTER(?Z < 20) .
p:进出口压差（Kpa）[?X,?Z] :- p:进出口压差（Pa）[?X,?Y], BIND(?Y / 1000 AS ?Z) .
p:故障[?X,p:冷凝设备压差过大] :- p:类型[?X,p:冷凝设备], p:进出口压差（Kpa）[?X,?Z], FILTER(?Z > 20) .
```

![image-20211122190357106](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630534.png)

![image-20211122190413381](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630566.png)

### 金融领域知识推理

- 阅读程序源码，解除JRDFoxDemo_finance.java中141-146 的注释，观察在推理过程中新插入三元组后推理结果的变化 ，理解否定失败非单调的性质。

![image-20211122190806038](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630342.png)

![image-20211122190852268](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630381.png)

- 注释前：

```turtle
<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#contractorFor> <http://www.example.org/kse/finance#万达集团> .
```

- 注释后：

```turtle
<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#employeeOf> <http://www.example.org/kse/finance#万达集团> .
```

- 代码注释后，导入以下数据：

```turtle
<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#employeeOf> <http://www.example.org/kse/finance#万达集团> .<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#firstName> "Peter" .<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#lastName> "Green" .
```

- 代码注释前，新加了一条数据：

```turtle
<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#employeeOf> <http://www.example.org/kse/finance#万达集团> .<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#employeeOf> <http://www.example.org/kse/finance#万达集团> .<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#firstName> "Peter" .<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#lastName> "Green" .
```

- 这将触发否定规则：

```txt
q:contractorFor[?X,?Y] :- q:worksFor[?X,?Y], NOT q:employeeOf[?X,?Y] .
```

- 注释后因为检测到，李四worksFor万达集团,但缺乏李四emploeeof万达集团，所以进行推理，生成李四是contractorFor万达集团，李四是emploeeof万达集团；
- 注释前因为检测到，李四worksFor万达集团,以及李四emploeeof万达集团，所以李四不是contractorFor万达集团，李四是emploeeof万达集团。

## Week5 

- 运行环境：

![image-20211129211335655](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630649.png)

- TranseE运行：
  - 数据集：“WN18RR”

## 代码调整

### Transe

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

#### 原始实验：

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

#### 改变margin为4

```shell
Date=`date +%y%m%d`
echo "2.sh back begin at `date +%H:%M:%S`" >> out.log
nohup python -u train_transe_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(4,100,100,1,1000,1).log'  
echo "2.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130225656189](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631039.png)

![image-20211130225624796](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631382.png)

- 虽然loss降得很低，但是测试结果却发生了一定下降，所以该参数条件下造成了过拟合

#### 改变p_norm为2

![image-20211130225908749](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631350.png)

![image-20211130230109824](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631166.png)

- 用$l_2$范数发现效果显著下降，这说明$l_2$范数明显不适合此次实验

####  变维数为200

```shell
Date=`date +%y%m%d`
echo "5.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=200 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(5,200,100,1,1000,1).log'
echo "5.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230249785](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631794.png)

![image-20211130230303651](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631958.png)

- 200dim效果并不好，且增加计算开销，所以200 dim不适合

#### 改变n_batches为200

```shell
Date=`date +%y%m%d`
echo "5.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=200 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transe/transe(5,200,100,1,1000,1).log'
echo "5.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230624695](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631609.png)

![image-20211130230652953](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631896.png)

- 200 batch效果有所下降

#### 学习率调为0.5

```shell
Date=`date +%y%m%d`
echo "6.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transe/transe(5,100,100,1,1000,0.5).log' 
echo "6.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230805816](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631070.png)

![image-20211130230818576](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631486.png)

- 学习率降低后，效果有一定上升

#### epoch调维500

```shell
Date=`date +%y%m%d`
echo "7.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transe_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=500 --alpha=1 > logs/'./result/transe/transe(5,100,100,1,500,1).log' 
echo "7.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130230922827](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631817.png)

![image-20211130230937547](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631694.png)

- 发现训练500 epoch的loss降低了一半，且测试结果与原始条件相差甚微，所以预估训练的最佳epoch在500~1000epochs

### Transh

#### 原始条件

```shell
Date=`date +%y%m%d`
echo "8.sh back begin at `date +%H:%M:%S`" >> out.log

nohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,100,100,1,1000,0.5).log'
echo "8.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232032809](img/image-20211130232032809.png)

![image-20211130232050641](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271631710.png)

#### margin改为5

```shell
Date=`date +%y%m%d`echo "9.sh back begin at `date +%H:%M:%S`" >> out.lognohup python -u train_transh_FB15K237.py --margin=5 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(5,100,100,1,1000,0.5).log' echo "9.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232200320](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632944.png)

![image-20211130232219507](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632316.png)

- 效果强于原始条件，有较大提升

#### n_batches改为200

```shell
Date=`date +%y%m%d`echo "10.sh back begin at `date +%H:%M:%S`" >> out.lognohup python -u train_transh_FB15K237.py --margin=4 --nbatches=200 --dim=100 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,200,100,1,1000,0.5).log'echo "10.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232331620](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632454.png)

![image-20211130232350876](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632910.png)

- 无显著提升，但至少没有过拟合

#### dim改为200

```shell
Date=`date +%y%m%d`echo "11.sh back begin at `date +%H:%M:%S`" >> out.lognohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=200 --p_norm=1 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,100,200,1,1000,0.5).log'echo "11.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232455838](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632894.png)

![image-20211130232508997](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632397.png)

- 发生了严重过拟合

#### p_norm改为2

```shell
Date=`date +%y%m%d`echo "12.sh back begin at `date +%H:%M:%S`" >> out.lognohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=2 --train_times=1000 --alpha=0.5 > logs/'./result/transh/transh(4,100,100,2,1000,0.5).log'echo "12.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232711326](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632378.png)

![image-20211130232727325](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632565.png)

- 整个模型都坏掉，实在不适合

#### epoch改为500

```shell
Date=`date +%y%m%d`echo "13.sh back begin at `date +%H:%M:%S`" >> out.lognohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=500 --alpha=0.5 > logs/'./result/transh/transh(4,100,100,1,500,0.5).log'echo "13.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130232840746](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632933.png)

![image-20211130232853436](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632469.png)

- 效果一般，感觉有点欠拟合

#### 学习率改为1

```shell
Date=`date +%y%m%d`echo "14.sh back begin at `date +%H:%M:%S`" >> out.lognohup python -u train_transh_FB15K237.py --margin=4 --nbatches=100 --dim=100 --p_norm=1 --train_times=1000 --alpha=1 > logs/'./result/transh/transh(4,100,100,1,1000,1).log'echo "14.sh back end at `date +%H:%M:%S`" >> out.log
```

![image-20211130233027477](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632692.png)

![image-20211130233039606](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632908.png)

- 过拟合

## week6

![image-20211206202608932](E:/third_year_in_University/knowledge%20engineering/experiment/5/img/image-20211206202608932.png)

### 分别使用EN_FR_15K_V2的split1和EN_DE_15K_V2的split2来运行MTransE，记录使用的命令和结果

#### EN_FR_15K_V2的split1

```shell
python main_from_args.py ./args/mtranse_args_15K.json EN_FR_15K_V2 721_5fold/1/
```

![image-20211206191443448](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271632798.png)

![image-20211206202156392](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633160.png)

![image-20211206202214050](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633548.png)

#### EN_DE_15K_V2的split2

```shell
python main_from_args.py ./args/mtranse_args_15K.json EN_DE_15K_V2 721_5fold/2/]
```

![image-20211206193013013](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633630.png)

![image-20211206201711725](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633141.png)

![image-20211206201830254](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633731.png)

### mtranse_args_15K.json和mtranse_args_100K.json有何区别，为什么要设置这种区别，而不是直接写一个mtranse_args.json？

![image-20211206190640076](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633917.png)

- 我们发现这两个文件对应训练的规模不同，mtranse_args_15K.json训练的batch_size比较小，所以对应的阈值也设置比较小；mtranse_args_100K.json训练的batch_size比较大，所以对应的阈值也设置比较大

### 什么是earlystop？这个实例中为什么需要earlystop？

![image-20211206193138846](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271633222.png)

- earlystop指的是在跑完所有epoch前停止训练；
- 在实例中，由于为防止训练过拟合，当我们发现测试的准确率发生明显下降，我们应该停止迭代

## Week7

### Q1

- Who are the creators(including paintings) of Guernica and Sunflowers, respectively

#### SPARQL语句

```SPARQL
PREFIX ex: <http://example.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?s ?p ?n
WHERE {
	?s ex:creatorOf ?p;
       foaf:firstName ?n
	{?p rdfs:label \"Guernica\".}
	UNION{?p rdfs:label \"Sunflowers\".
}
```

#### code

```java
public class MYQuery {

	public static void main(String[] args)
			throws IOException {
		// Create a new Repository.
		Repository db = new SailRepository(new MemoryStore());

		// Open a connection to the database
		try (RepositoryConnection conn = db.getConnection()) {
			String filename = "example-data-artists.ttl";
			try (InputStream input = MYQuery.class.getResourceAsStream("/" + filename)) {
				// add the RDF data from the inputstream directly to our database
				conn.add(input, "", RDFFormat.TURTLE);
			}

			// We do a simple SPARQL SELECT-query that retrieves all resources of type `ex:Artist`,
			// and their first names.
			String queryString = "PREFIX ex: <http://example.org/> \n";
			queryString += "PREFIX foaf: <" + FOAF.NAMESPACE + "> \n";
			queryString += "SELECT ?s ?n ?p \n";
			queryString += "WHERE { \n";
			queryString += "    ?s ex:creatorOf ?p; \n";
			queryString += "       foaf:firstName ?n; \n";
			queryString += "    {?p rdfs:label \"Guernica\".} \n";
			queryString += "    UNION{?p rdfs:label \"Sunflowers\".} \n";
			queryString += "}";

			TupleQuery query = conn.prepareTupleQuery(queryString);

			// A QueryResult is also an AutoCloseable resource, so make sure it gets closed when done.
			try (TupleQueryResult result = query.evaluate()) {
				// we just iterate over all solutions in the result...
				for (BindingSet solution : result) {
					// ... and print out the value of the variable binding for ?s and ?n
					System.out.println("?s = " + solution.getValue("s"));
					System.out.println("?n = " + solution.getValue("n"));
					System.out.println("?p = " + solution.getValue("p"));
				}
			}
		} finally {
			// Before our program exits, make sure the database is properly shut down.
			db.shutDown();
		}
	}
}

```

#### Result

![image-20211213194751098](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634057.png)

### Q2

- List all the artists (including living places) who live in Spain or other places.

#### SPARQL

```SPARQL
PREFIX ex: <http://example.org/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?s ?n ?place
WHERE {
	?s a ex:Artist;
       foaf:firstName ?n.
	OPTIONAL{?s ex:homeAddress ?p.
			?p ex:country ?place.}
}
```

#### code

```JAVA
public class MYQuery2 {

	public static void main(String[] args)
			throws IOException {
		// Create a new Repository.
		Repository db = new SailRepository(new MemoryStore());

		// Open a connection to the database
		try (RepositoryConnection conn = db.getConnection()) {
			String filename = "example-data-artists.ttl";
			try (InputStream input = MYQuery2.class.getResourceAsStream("/" + filename)) {
				// add the RDF data from the inputstream directly to our database
				conn.add(input, "", RDFFormat.TURTLE);
			}

			// We do a simple SPARQL SELECT-query that retrieves all resources of type `ex:Artist`,
			// and their first names.
			String queryString = "PREFIX ex: <http://example.org/> \n";
			queryString += "PREFIX foaf: <" + FOAF.NAMESPACE + "> \n";
			queryString += "SELECT ?s ?n ?place \n";
			queryString += "WHERE { \n";
			queryString += "    ?s a ex:Artist; \n";
			queryString += "       foaf:firstName ?n. \n";
			queryString += "    OPTIONAL{?s ex:homeAddress ?p. \n";
			queryString += "    ?p ex:country ?place.} \n";
			queryString += "}";

			TupleQuery query = conn.prepareTupleQuery(queryString);

			// A QueryResult is also an AutoCloseable resource, so make sure it gets closed when done.
			try (TupleQueryResult result = query.evaluate()) {
				// we just iterate over all solutions in the result...
				for (BindingSet solution : result) {
					// ... and print out the value of the variable binding for ?s and ?n
					System.out.println("?s = " + solution.getValue("s"));
					System.out.println("?n = " + solution.getValue("n"));
					System.out.println("?place = " + solution.getValue("place"));
				}
			}
		} finally {
			// Before our program exits, make sure the database is properly shut down.
			db.shutDown();
		}
	}
}

```

#### Result

![image-20211213200032496](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634446.png)

### Q3

- List all paintings, their names, and the corresponding techniques.

#### SPAQL

```SPARQL
PREFIX ex: <http://example.org/>
SELECT ?s ?n ?t
WHERE {
	?s a ex:Painting;
	rdfs:label ?n;
    ex:technique ?t.
}
```

#### code

```JAVA
public class MYQuery3 {

	public static void main(String[] args)
			throws IOException {
		// Create a new Repository.
		Repository db = new SailRepository(new MemoryStore());

		// Open a connection to the database
		try (RepositoryConnection conn = db.getConnection()) {
			String filename = "example-data-artists.ttl";
			try (InputStream input = MYQuery3.class.getResourceAsStream("/" + filename)) {
				// add the RDF data from the inputstream directly to our database
				conn.add(input, "", RDFFormat.TURTLE);
			}

			// We do a simple SPARQL SELECT-query that retrieves all resources of type `ex:Artist`,
			// and their first names.
			String queryString = "PREFIX ex: <http://example.org/> \n";
			queryString += "PREFIX foaf: <" + FOAF.NAMESPACE + "> \n";
			queryString += "SELECT ?s ?n ?t \n";
			queryString += "WHERE { \n";
			queryString += "    ?s a ex:Painting; \n";
			queryString += "       rdfs:label ?n; \n";
			queryString += "       ex:technique ?t. \n";
			queryString += "}";

			TupleQuery query = conn.prepareTupleQuery(queryString);

			// A QueryResult is also an AutoCloseable resource, so make sure it gets closed when done.
			try (TupleQueryResult result = query.evaluate()) {
				// we just iterate over all solutions in the result...
				for (BindingSet solution : result) {
					// ... and print out the value of the variable binding for ?s and ?n
					System.out.println("?n = " + solution.getValue("n"));
					System.out.println("?t = " + solution.getValue("t"));
				}
			}
		} finally {
			// Before our program exits, make sure the database is properly shut down.
			db.shutDown();
		}
	}
}

```

#### Result

![image-20211213194953025](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634599.png)

## Week 8

### 导入contact-tracing-43.dump文件到数据库neo4j中

```
neo4j-admin load --from=import\contact-tracing-43.dump --database=neo4j --force
```

![image-20211220185832367](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634101.png)



### 查询名叫Madison Odonnell的人物节点，并记录下该节点的

```cypher
MATCH (p:Person{name:'Madison Odonnell'}) Return LIMIT 25
```

![img](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634245.png)

```cypher
MATCH (p:Person{name:'Madison Odonnell'}) return p.healthstatus,p.name,p.confirmedtime
```

![image-20211220190123173](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634246.png)

### 将该人物节点及与其相连的关系删除，并检查是否删除成功

```cypher
MATCH (p:Person{name:'Madison Odonnell'}) Detach Delete p
```

![image-20211220190542831](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634537.png)

```cypher
MATCH (p:Person{name:'Madison Odonnell'}) Return p
```

![image-20211220190626980](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634889.png)

- 删除成功

### 重新创建该节点以及第2步记录下来的节点属性;

```cypher
Create 	(p:Person		{confirmedtime: "2020-04-25T23:09:38Z",		name: "Madison Odonnell",		healthstatus: "Healthy",		id: "18",		addresslocation: point({srid:7203, x:51.21602455, 			y:4.406776648})}) Return p
```

- 创建成功

<img src="https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634257.png" alt="image-20211220191156864" style="zoom:50%;" />

### 重新创建关系： Madison Odonnell的人物节点与名为‘Place nr 40’的Place节点间的关系，不考虑关系属性;

```cypher
Match (p:Person{name:'Madison Odonnell'}),(pl:Place{name:'Place nr 40'}) Create(p)-[r:VISITS]->(pl)Return p, r,pl
```

<img src="https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634668.png" alt="image-20211220193509141" style="zoom: 80%;" />

### Madison Odonnell不幸被确诊为新冠（healthstatus=‘sick’），对图谱进行更新

```cypher
Match (p:Person{name:'Madison Odonnell'}) Setp.healthstatus='sick'Return p
```

<img src="https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634197.png" alt="image-20211220193631356" style="zoom:67%;" />

- 检测

```cypher
Match (p:Person{name:'Madison Odonnell'}) Return p
```

![image-20211220193829381](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271634838.png)

