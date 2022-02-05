# 实验3、实验4报告

## 1. Week1

### 1.1 Task1 finance

- 阅读程序Demo_finance.java源码，分别注释本体和规则的部分，观察推理结果的变化;

#### 1.1.1 刚开始运行结果

![image-20211115193512261](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629440.png)

#### 1.1.2 原来的代码：

```java
store.importOntology(ontology);
store.importFiles(new File[] {dataFile});
store.importFiles(new File[] {ruleFile});
```

#### 1.1.3 delete ontology

```java
//注释掉 store.importOntology(ontology);
store.importFiles(new File[] {dataFile});
store.importFiles(new File[] {ruleFile});
```

![image-20211115205127054](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629413.png)

![image-20211115193530420](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271629377.png)

#### 1.1.4 delete rule

```java
store.importOntology(ontology);
store.importFiles(new File[] {dataFile});
//注释掉：store.importFiles(new File[] {ruleFile});
```

![image-20211115193605172](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630886.png)

#### 1.1.5 add new rule

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

##### 1.1.5.2 rule2

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

### 1.2 Legal

- 撰写Datalog规则进行推理，观察新的推理结果（对应“实验课代码\src\main\resources\data\legal_rule.txt”）：

#### 1.2.1 add rule

- 如果案件A关联事件B,事件B的发生时间是案件A的关键节点（对 应legal_data.nt 中的谓词“Relate”和“Time”）

![image-20211115200810188](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630325.png)

```txt
PREFIX p: <http://www.reason/legal#>

p:BelongTo(?B,?A) :- p:Relate(?A,?B) .
p:Steal(?Z,?S) :- p:Relate(?X,?Y), p:Person(?Y,?Z), p:Thing(?Y,?S) .
p:KeyPoints(?A,?C) :- p:Relate(?A,?B), p:Time(?B, ?C) .
```

![image-20211115200845490](https://gitee.com/zhu-qipeng/blogImage/raw/master/blogImage/202112271630766.png)

## 2. Week2

### 2.1 故障诊断领域知识推理

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

### 2.2 金融领域知识推理

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
<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .
<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .
<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#employeeOf> <http://www.example.org/kse/finance#万达集团> .

<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#firstName> "Peter" .
<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#lastName> "Green" .
```

- 代码注释前，新加了一条数据：

```turtle
<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#employeeOf> <http://www.example.org/kse/finance#万达集团> .

<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .
<http://www.example.org/kse/finance#李四> <http://www.example.org/kse/finance#worksFor> <http://www.example.org/kse/finance#万达集团> .
<http://www.example.org/kse/finance#张三> <http://www.example.org/kse/finance#employeeOf> <http://www.example.org/kse/finance#万达集团> .

<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#firstName> "Peter" .
<http://www.example.org/kse/finance#peter> <http://www.example.org/kse/finance#lastName> "Green" .
```

- 这将触发否定规则：

```txt
q:contractorFor[?X,?Y] :- q:worksFor[?X,?Y], NOT q:employeeOf[?X,?Y] .
```

- 注释后因为检测到，李四worksFor万达集团,但缺乏李四emploeeof万达集团，所以进行推理，生成李四是contractorFor万达集团，李四是emploeeof万达集团；
- 注释前因为检测到，李四worksFor万达集团,以及李四emploeeof万达集团，所以李四不是contractorFor万达集团，李四是emploeeof万达集团。

