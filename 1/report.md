# 第一次实验报告

## Week1

### 设置本体IRI

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



