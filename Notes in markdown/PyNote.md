# 0 目录
1. [入门](#1入门)
2. [数值处理与可视化](#2数值处理与可视化)
   1. [NumPy](#21-拓展库numpy)
   2. [Matplotlib](#22拓展库matplotlib)
3. [高等数学领域的应用](#3-高等数学领域的应用)
   1. [SymPy](#31-符号计算sympy)
   2. [Scipy](#32-高等函数SciPy)
4. [统计](#4-概率论与数理统计)
5. [线性规划](#5-线性规划)
   1. [线性规划方法](#52-利用python的求解方式)
6. [非线性规划](#6-整数规划与非线性规划)
7. [插值与拟合](#7-插值与拟合)
   1. [插值方法](#712-可用函数)
   2. [拟合方法](#722-可用函数)
8. [微分方程](#8-微分方程)
9.  [综评方法](#9-综合评价的方法)
10. [图论](#10-图论)
11. [多元分析](#11-多元分析)
    1. [判别分析](#111-判别分析)
    2. [主成分分析](#112-主成分分析)
    3. [因子分析](#113-因子分析)
    4. [聚类分析](#114-聚类分析)
12. [多元回归分析](#12-多元回归分析)
* [补充一：概率论的部分理论知识](#补充一概率论的部分理论知识)



# **1.入门**

## **1.1 逻辑判断与循环**

#### 1.1.1 `if`语句
格式：
```Python
if Judge1 :
    #statement1
elif Judge2 :
    #statement2
else :
    #statement3
```
>**注意**  
缩进是`python`中表示代码块的方式

#### 1.1.2 `for`循环
格式：
```Python
for obj in obj_list
    #statement1
else
    #statement2
```
>**提示**  
>一般采用`range()`函数来作为计数器，而`range()`的用法如下:`range(start,end,step)`,其中`start`与`step`可忽略。

#### 1.1.3 `while`循环
格式：
```Python
while Judge1 :
    #statement1
else
    #statement2
```

## **1.2 类数组类型**

### 1.2.1 列表 

#### 初始化
首先，列表是一个顺序广义表，用`[]`来声明以及初始化，标识符为`list`，初始化方式与`C`中类似

#### 索引 
类似于`C`中的数组，但在索引使用上有所不同，`python`中可以用索引获取一系列列表中的元素。使用方式如下：
```python
a = [elements]
a[i] 
#若i >= 0, 则与C一致，若i < 0,则为从最后一位开始的第-i位元素
a[i][j] 
#同上，要求a[i]是一个广义表
a[start:end:step] 
#全部均可选，但需确保至少有一个数。
#start默认为0，end默认为最后一个元素的索引+1，step默认为1
```
>**注意**  
索引为`end`的元素不能被取到

#### 方法s
```python
#假定List_a为一个列表

List_a.append(x) #向列表尾部增加一个元素x
List_a.extend(List_b) #向列表尾部增加List_b内的所有元素
List_a.insert(index,x) #在索引为index处插入元素x，原元素后移

List_a.pop() #与栈的pop操作一致
List_a.remove(x) #删除列表中从左数第一个出现的元素x，若无则报错
List_a.clear()
del List_a[index] #删除列表中特定下标的元素

List_a.index(x) #搜索列表中从左数第一个出现的元素x的索引，若无则报错
List_a.count(x) #搜索x的出现次数
List_a.sort() #将列表按升序排列
List_a.reverse() #逆转List_a的顺序

len(List_a) #列表长度
sorted(List_a, reverse = True) #将列表按一定顺序排列，并返回这个列表（不改变原列表）

#重定义
List_a + List_b #连接列表
a * List_a #重复列表
```

#### 元组
类似于列表，使用`()`初始化，是一个有序广义表，标识符为`tuple`。只有一个元素的元组声明时需要带逗号：`a = (9,)`  
特性：`const`后的列表

### 1.2.2 字典与集合
#### 字典的初始化
字典类型的标识符为`dict`,使用`{}`来创建以及初始化，是一个无序广义表，通过**关键词**，即**键**（*key*）来标识每个元素。也正是因此而决定了键唯一  
初始化方法：  
* `a = {key1:value1,key2:value2}`
* `dict(List)`  
其中`List`为一个序列

#### 字典的操作
* `a[key] = value`  
若`key`已存在于`a`中，则为修改键值；若`key`不存在，则为新增键值  
* `a.pop(key)`  
将键为`key`的元素删除

#### 集合的初始化
集合类型的标识符为`set`，是一个无序广义表，使用`{}`来初始化（不可以使用`{}`来创建空集合），集合中的元素**各不相同**  
初始化方法：  
* `a = set(List)`
* `a = {elements}`  

#### 集合的操作与方法
```python
#假定s,st均为集合
s.add(x)
s.remove(x) #删除元素x，若无则触发KeyError错误
s.discard(x) #删除元素x，若无则当无事发生
s.clear()
s.copy() #返回一个与s相同的集合
s.pop() #移除并返回s中的任一元素，若s为空则触发KeyError错误
s.update(st) #对s与st求并并储存至s中

s = s - st #差
s = s & st #交
s = s ^ st #对称差
s = s | st #并
```  
### 1.2.3 序列的操作
#### 字符串操作
1. `str()` 将数据转换为字符串
2. `len()` 求字符串长度
3. `count(str)` 求字符串对象中字串`str`的出现次数
4. `eval(str)` 类似于宏，将该语句所在行替换为参数内容
5. `find(str)`与`rfind(str)` 将`str`与字符串对象模式匹配，返回从左向右数的第一个匹配的子串索引。后者为从右向左匹配。
6. `split(str)` 以str作为分隔符，将字符串对象分割，返回分割后的字串组成的字串列表。分隔符默认为`' '`
7. `join(str)` 以str为分割符，将字符串列表连接，返回一个字符串
8. `strip()`,`lstrip()`与`rstrip()` 将参数内的每个字符当作空格，而后去除字符串前后的所有空格（不去除内部的空格）；后面两个变体函数分别为去除左右的所有空格。比如语句`“  **#Hello Python*#*  ”.strip(' *#')`会输出`Hello Python`

**注意**以上语句中1、2、4为作用于字符串的函数，其余为字符串类型内的函数。即前者为`func(str)`,后者为`str.func()`

#### 序列操作函数

匿名函数
: 也称单行函数,与`C`中的宏函数形式上类似，用作多元实值函数，声明为：`f = lamda x1,x2,...,xn: statement`  

1. `map(func,iterables)` 用`func`生成一个列表，`iterables`为其参数列表/元组，不同位置上的参数要使用不同列表储存。例：``map(pow,range(1,6),[2]*6) ``返回列表`[1.0,4.0,9.0,16.0,25.0]`
2. `reduce(func,list,initial)` 先将`func`作用于`list`的前两个元素，而后将`func`作用于返回值与第三个元素，依次迭代下去直到列表结束。最后返回结束时的返回值。要求`func`为接受2个相同类型参数并有一个返回值的函数。
3. `filter(func,iterable)` 返回过滤后的列表。`func`为可选参数。如果没有`func`,则根据参数自身判断真值；若有，则以表中元素为参数，通过`func`判断真值。若值为假则会被滤去。
4. `zip(list_1,list_2,..,list_n)` 类似于笛卡尔积生成**元组**，但是由于参数均为有序表，故生成的元素亦为有序元组。例：`zip([1,2],[3,4])`返回`[(1,3),(2,4)]`
5. `enumerate(obj)` 枚举列表，返回一个枚举对象。每个枚举元素格式如下：`(index,element)`

#### 推导式
* 用`for`迭代生成一个列表,例：
```python
[a for b in zip(range(1,4),range(2,5)) for a in b] #Namely,[1,2,2,3,3,4]
[(x,y) for x in range(-1,10,2) for y in range(0,4) if y < x] #Namely,
#[(1, 0), (3, 0), (3, 1), (3, 2), (5, 0), (5, 1), (5, 2),
# (5, 3), (7, 0), (7, 1), (7, 2), (7, 3), (9, 0), (9, 1),
# (9, 2), (9, 3)]
```

* 用`for`迭代生成一个元组生成器，例：
```python
temp = (a for b in zip(range(1,4),zip(2,5)))
tuple_temp = tuple(temp) #到这一步才能生成元组
```

## **1.3 函数**

### 1.3.1 基本格式

```Python
def FunctionName(Parameters):
    '''statements'''
    return 'Hello Python'
```

* 参数规则见[后续说明](#132-参数)
* 定义须在调用前
* 返回值（`return`语句）是可选的；当函数没有`return`语句时，会默认返回`None`

### 1.3.2 参数

#### 参数类型

位置参数
:  即与`C`中的普通参数规则完全相同的参数

默认参数  
:  即已被赋予固定值的常参数，表示为：`p=3`(即给函数参数后面接上了等号)。而这样的参数不参与传参过程。

可变参数  
:  可接受**不定长**数据的参数，接受时会将接受的参数合并入一个[元组](#元组)内。以`*arg`的形式来表示这样的参数

关键字参数  
:  接受**一个**普通参数，可以通过索引（即关键字）无视参数顺序输入参数，但是要保证索引与参数名称匹配。形式为：`variable=value`

可变关键字参数  
:  可接受**不定长**的关键字参数，接受时会将接受的参数合并入一个[字典](#122-字典与集合)内,这个字典以索引为传入参数的索引。以`**arg`的形式来表示这样的参数。

>在忽略关键字参数的前提下，传参顺序应为：位置参数 ->默认参数 ->可变参数 ->可变关键字参数

#### 传参方式  

* 在传递不可变对象时，如数值、字符串，则*按值传递*；若传递可变对象时，如列表，则*按址传递*
  > 对于可变对象来说，由于按址传递不可避免，所以可以采用`List[:]`的方式传入一个匿名副本

以下代码展示了*按址传递*：
```Python
def swap(data):
    data[0],data[1]=data[1],data[0]
    print("Doing swaping:",end=' ')
    for i in range(2) : 
        print("data[%d]=%2d"%(i,data[i]),end='\t')

data = [1,2]
print("Before swaping:",end=' ')
for i in range(2) : 
    print("data[%d]=%2d"%(i,data[i]),end='\t')
print('\n\n')

swap(data)
print('\n\n')

print("After swaping:",end=' ')
for i in range(2) : 
    print("data[%d]=%2d"%(i,data[i]),end='\t')

#嗯，非常地...不优雅？
```

* 对于可迭代对象（列表、元组、集合、字典等），可以在其名称前加一个星号`*`作为参数，这样python解释器会将其自动解包，然后看作多个值依次传给函数的各参数。

>对于字典，这样会默认使用字典的索引。如果需要使用索引+值，则考虑选择`items()`方法，需要使用值，则考虑选择`values()`方法  

#### 导入模块方法 —— `import`

模块的使用类似于头文件/类之类的使用，参考以下代码：
```Python

import math #导入math模块
math.abs(-2) #我们假定math模块中有一个方法为abs，则需要通过类似结构体/类的方式使用

import math as m
m.abs(-2)#你也可以考虑给模块一个简称 

from math import abs
abs(-2)#好消息：这样你就不用打math了！坏消息：你只能用abs了！
from math import abs as a #人总是想偷懒

from math import * 
#可以将math模块中的所有对象导入，且使用时无需打math。
#但需注意，这样在导入多个模块时可能会发生对象冲突 

#你还可以从自己写的py文件中导入
```  

## **1.4 类**

### 1.4.1 声明方式

在`python`中，一个类由**初始化方法**和对该类对象的**操作方法**构成，以下为一个简单的例子：

```python

class ClassName:

    def __init__(self, para_a, para_b):
        self.para_a = para_a
        self.para_b = para_b
        self.para_c = 'Hello World!'
    #这个初始化方法是必备且唯一的(命名也是唯一的)
    #用c的观点来看，这个方法同时完成了（结构体的）声明与定义
    #即，若没有这个函数，这个“结构体”连成员都没有

    def upgrade(self, new_para_a):
        self.para_a = new_para_a
        # Statements
    #操作方法（可以有多个）


temp = ClassName('Hello ', 'Python, ')
print(temp.para_a + temp.para_b + temp.para_c)

temp.upgrade('Goodbye ')
print(temp.para_a + temp.para_b + temp.para_c, end = '\n')

```  

当然，由于`__init__`是一个方法，所以你也可以这么干：
```python
def __init__(self, para_a, para_b, para_c = 'Hello World!'):
    self.para_a = para_a
    self.para_b = para_b
    self.para_c = para_c
```
所有先前阐述过的参数的用法在这里都是可行的

> 注：和`__init__`相似的内置方法还有很多，比如说明串`__str__`和`__repr__`，下标实现`__getitem__`，以及长度实现`__len__`，这些可以参考[官方文档](https://docs.python.org/3/reference/datamodel.html#basic-customization)

### 1.4.2 子类

> 从某种程度上来说，可以将子类类比为C中结构体的嵌套
子类，顾名思义，需要定义在一个*父类*之上，因此在子类的定义前必须有父类的定义，其体现如下：
```python

class ChildClassName(ClassName):

    def __init__(self, para_a, para_b, para_d, para_c = 'Hello World!'):
        super().__init__(para_a, para_b, para_c)
        self.para_d = para_d
    #在这里，super()是一个特殊的函数，用以将父类与子类关联在一起
    #子类新增的成员，既可以是一个原子类型，也可以是一个类
    
    #你可以对父类的函数重定义
    def upgrade(self, new_para):
        self.para_a = new_para
        self.para_d = new_para

    def child_func(self, para_d):
        self.para_d += para_d

    def watch(self):
        print([self.para_a, self.para_b, self.para_c, self.para_d])

```  

* 这些类有点时候会显得很大，所以可以考虑多文件编译，而后从其他文件中用`import`来引入你所需要用到的类

## **1.5 文件读取**

### 1.5.1 打开文件

#### `open`,`close`与`with`

open  
: 以要打开文件的路径（可以是相对路径，也可以是绝对路径）为必选参数，以及一个可选参数（默认为'r'),返回一个表示文件的对象的**函数**

> 注：可选参数中满足以下对应关系：
> 
> *读取模式* -> 'r'
> *写入模式* -> 'w'
> *读写模式* -> 'r+'
> *附加模式* -> 'a'

close  
: 以要关闭文件的对象为参数的**函数**，作用顾名思义：关闭文件

with
: 与`open`搭配使用，在无需访问文件后（即脱离`with`下的代码块以后）就关闭文件的一个**关键字**

* 使用范例
  ```python
  with open('file_path') as fp
      # statements
  # 在代码块中，变量fp即为代表打开文件的对象

  fp = open('file_path')
  fp.close()
  # 另一种关闭方式
  ```

#### 文件对象
|     **functions**    	    | **descriptions** 	|
|:--------------------:	    |:----------------:	|
|        `close()`          | 将缓冲区内容写入文件，但不关闭文件	|
|        `flush()`          | 作用部分同上，但关闭文件        	|
|        `read()`        	| 略              	|
|      `readlines()`     	| 略              	|
|  `seek(offset, where)` 	| 将文件指针移动至相对`where`的`offset`位置；其中对于`where`，0为起始处，1为当前处，2为末尾处	|
|        `tell()`        	| 返回当前位置的值	|
|      `truncate()`      	| 删除从当前指针至文件末尾的内容 	|
| `write()/writelines()` 	| 均为写入，后者可接受可迭代对象为参数	|

### 1.5.2 写入文件

#### `write`方法
`write`方法是一种写入文件的主要方式，而其用法也十分简单：
```python
file_object.write(contents)
#注意，write方法不会在行尾加换行符
```

#### 将数据写入JSON文件中
json的通用是众所周知的，因此可以考虑使用json来在文件中存储你的变量等信息
这里我们给出两个对json模块的操作方法：`dump`和`load`

```python

json.dump(variable, file_object)
#接受需存储的变量与需要写入的文件对象

json.load(file_object)
#接受需读取的文件对象，而后返回读得的变量

```

## 1.6 **异常处理**

### 1.6.1 两种简单的异常

* `FileNotFoundError`通常出现在读入文件的阶段，顾名思义，表示找不到文件。这是一个异常**对象**
* `ZeroDivisionError`出现在计算x/0的问题中。也是一种异常**对象**

### 1.6.2 常用语句

```python

try:
    open(file_path,'r')
except FileNotFoundError:
    pass
    #print('File Not Found!')
else:
    #statement
finally:
    #statement

```
* `try`语句：在上述代码中，`try`用于第一次执行，并在出现异常的时刻不中断程序，而是抛出异常。
* `except`语句：**唯一**的接异常的语句。用于出现特殊异常时，将异常接住，并执行自身下属代码块。
* `else`语句：没有异常时执行。只能出现在所有`except`的后面
* `finally`语句：无论怎样都会执行

> 注：如果一个异常在`finally`之后还没有被接住，那么就会引起程序中断。

### 1.6.3 异常类

由于[子类](#142-子类)这一概念的存在，加上异常`Exception`是一个类，因此我们可以由异常类衍生出自定义异常。

#### `raise`语句

用于抛出一个异常，保证你可以定义一些python语法上可行的行为是异常的。
用例：
```python
raise ZeroDivisionError # 抛出不能除以0的异常
raise Exception('Oops!') # 抛出一个错误信息为'oops'的异常
raise #再次抛出上一次所抛出的异常
```

> 注：所有标准库规定的异常类都可以接受一个参数，即错误描述

#### 自定义异常类

```python
class MyException(Exception):
	def __init__(self, description):
		self.content = description

try:
    raise MyException('Oops!'):
except MyException:
    pass

```


# **2.数值处理与可视化**  

## **2.1 拓展库`NumPy`**

### 2.1.1 数组的创建、属性与操作  

#### 创建数组

```python
import numpy as Num

array_1 = Num.array([1,1,4,5,1,4])
array_2 = Num.array(((1,4,5,3),(3,1,4,5),(5,3,1,4),(4,5,3,1)))
#创建一、二维数组
#其中每个元素的数据类型由输入的对象中占用最大内存的类型决定

array_3 = Num.arrage(0,10,2,dtype = int)
array_4 = Num.arrage(4,dtype = float)
#默认从0开始生成，每次默认递增1，必须输入数据类型与终止值

array_new = Num.empty((2,3),int)#生成2*3的空二维数组

array_5 = numpy.linspace(start, end, num = num_points)#生成精度损失较小的浮点数数组

array_rand = Num.random.randint(start,end,(dimension1,dimension2, ...))#生成大小制定，元素范围指定的随机整数数组
```

#### 数组属性  

| Properties |      Descriptions        |
| :---       |        :---:             |
| ndim       | 一个`int`，代表数组的维数 |
| shape | 一个`tuple`，代表数组的尺寸（即n*m）|
| size | 一个`int`，代表元素总数 |
| dtype | 即 data type |
| itemsize | 一个`int`，代表数组中元素的大小（即`sizeof`）|

#### 索引

* 基础索引
* 花式索引
> 这两种索引都可以用`zip()`函数的组织形式来理解：
> 注：切片表示法`start:end:step`实质上是一个迭代器，在索引中实际上任何时候都是一个数字，但在每个数字操作完成之后会将结果合并入一个列表内。
> 而后在花式索引中存在一个**广播机制**，即像`arr[[0, 1], 0]`中，后面的0会被拓展为与前面长度一致的整形数组。
> 于是接下来就会遵循花式索引的基本原则：`arr[[0, 1], [0, 0]]`等价于`[arr[0, 0], arr[1, 0]]`
> 进一步地，遵循基础索引的基本原则：`arr[0, 0]`表示第一个坐标轴上的第一个元素与第二个坐标轴上的第一个元素所限制出来的集合。
> 其维度表示如下：
> *ndim = Ndim - arraynums + 1*
> 其中*ndim*为索引下得到的数组，*Ndim*为原数组，*arraynums*为索引中的整型数组个数（数字项亦视为整型数组）。若索引中仅有数字项，则*arraynums = 2*

* 布尔索引

#### 修改与变形

```python
# 修改
import numpy as num

x = num.array([[1, 2], [3, 4], [5, 6]])
y = num.delete(x, 2, axis = 0)# 即delete(对象,序号,坐标轴)
#[[1 2]
# [3 4]]
y1 = num.append(y, [[7], [8]], axis = 1)# 即append(对象,新增内容,坐标轴)
#[[1 2 7]
# [3 4 8]]

```
> 注：在`append`中若加入内容行列元素数量不匹配会报错

```python
#变形
import numpy as num

a = num.arange(27).reshape(3, 8)
# [[ 0  1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14 15]
#  [16 17 18 19 20 21 22 23]]
a.reshape(4, 6)
a.resize(4, 6)
# 结果均为以下数组，但前者的返回值是一个视图，数组本身并未改变
# 而后者改变了数组本身，而没有返回值
#[[ 0  1  2  3  4  5]
# [ 6  7  8  9 10 11]
# [12 13 14 15 16 17]
# [18 19 20 21 22 23]]

a = num.random.randint(-5, 0, (2, 2))
b = num.random.randint(0, 10, (2, 2))
num.r_[a, b]
# 以a,b为row组成的分块矩阵（参数可以有多个），即行组合：
#[[a],[b]]
# 同理，num.c_[a, b]表示以a,b为column的分块矩阵，即列组合

a.tolist()# 将数组转换为python列表

# 水平展开数组
a.reshape(-1)# 返回视图
a.ravel()# 返回视图
a.flatten()# 返回一个新建的数组

num.vstack((a, b))# 等价于num.r_[a, b]
num.hstack((a, b))# 等价于num.c_[a, b]
num.dstack((a, b))

num.split(a, n, axis = 1)# 在横轴上切割（切成列向量组）
num.hsplit(a, n)# 同上
num.split(a, n, axis = 0)# 在纵轴上切割（切成行向量组）
num.hsplit(a, n)# 同上
```
> 注：“视图”是一个数组，它往往产生于原数组重整的过程中。视图的行列等属性可能与原数组不同，但是视图中的每一个元素都指向原数组中的元素（共用内存）

#### 运算

在`NumPy`中，对于数组重定义了几种运算：`+`,`-`,`*`,`/`,`//`(整除),`%`(取模),`**`(幂运算)
同时，所有比较运算符都有定义。
在这一部分，只需注意几点：
1. 这些运算符都有对应的函数，但都是接受两个参数的函数
2. 这些运算符作用在两个数组上时，会将两个数组中的相同位置的元素进行一次相关运算。比如`[1, 2]*[3, 4]`的结果是`[3, 8]`
3. 一个功能比原运算符大的函数：`numpy.modf()`,它接受两个参数，对应运算为`a//b`。但它返回一个含有两个元素的数组，第一个元素为`a/b`的小数部分，第二个元素为`a//b`(即`a/b`的整数部分)
4. `numpy.where()`可类比于`c`中的三元运算符` ? : `，其参数列表为`(condition,truevlue,falsevalue)`，其中`condition`为真值表，若真则返回前者，若假则返回后者。若是一个列表则对列表中的每一个元素进行该项操作。

### 2.1.2 NumPy中的随机数

NumPy中内置了生成多种分布的随机数函数，由于类型过多+笔者在此时还没学过统计的原因，请自行查表。（在书中P49）

### 2.1.3 NumPy中的文件操作

#### 将数据写入文件中

* 文本模式
  在前面也有这种操作的类似[条目](#152-写入文件)
  在这里利用的是NumPy中的类似操作：
  ```python

  numpy.savetxt('temp_1.txt', source_array, fmt = '%d', delimiter = ' ')
  # 将source_array中的内容以整型格式（默认为'%.18e'）保存至temp_1.txt中，并以空格为分隔符。
  a = numpy.loadtxt('temp_1.txt', dtype = int, delimeter = ' ')
  # 将temp_1中的内容当作整型数据读入（默认为浮点数），读入时将空格当作分隔符,最后返回一个ndarray
  a.astype(float)
  # 类型转换

  ```
  而后也有功能更强大的函数：`numpy.genfromtxt()`参数过多，也请自行查表
  [官方文档在此](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html "numpy.genfromtxt")
  ```python
  numpy.genfromtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, skip_header=0, skip_footer=0, converters=None, missing_values=None, filling_values=None, usecols=None, names=None, excludelist=None, deletechars=" !#$%&'()*+, -./:;<=>?@[\\]^{|}~", replace_space='_', autostrip=False, case_sensitive=True, defaultfmt='f%i', unpack=None, usemask=False, loose=True, invalid_raise=True, max_rows=None, encoding='bytes', *, ndmin=0, like=None)
  ```

* 二进制格式
  ```python
  import numpy
  a = numpy.arrange(6).reshape(2, 3)

  a.tofile(fname)
  #将数组以二进制形式保存下来，除了数组内数据，什么都没保存

  b = numpy.fromfile(fname, dtype = int)
  # 由于二进制文件中只存了数据，所以要指定数据类型。注意：这个函数读入的数组是一个n维向量

  numpy.save(fname, ndarray)# 一般来说后缀名为npy
  ndarray = numpy.load(fname)
  numpy.savez(fname, array_1, array_2, ...)# 一般来说后缀名为npz，是含有多个npy文件的压缩包。用numpy.load打开它的时候，会是一个字典，其键值为原存入数组的数组名。 
  ```

## **2.2拓展库`matplotlib`**

### 2.2.1 `matplotlib.plotpy`模块

#### `Figure`

`figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)`
用于创造或激活一个命名或序号为`num`的figure，其大小为`width`*`height`(若`fgsize = (width,height)`,单位为ft)，分辨率为`dpi`，其余参数望文生义即可。这个函数的返回值即为你所激活、创造的figure

> 笔者理解：激活等价于更改默认对象

#### 视图

在绘制时，默认有一个视图，但当我们需要绘制更复杂的图形或者设置更多选项时，我们就需要了解视图的一些有关函数

1. `matplotlib.plotpy.rc()`或`rcParams[]`可以用于设置许多选项，比如正常显示中文`'font',famlily = 'SimHei'`、调字号`'font',size = 10`、调字体`'text'`等
2. **单视图**设置：`matplotlib.plotpy.axes()`。一般来说，当需要改为绘制三维立体图形的时候需要使用这一函数。（`projection = '3d'`)
3. **多视图**设置：`matplotlib.plotpy.subplot()`。它相较于`axes()`函数拓展了三个参数，用于表示子视图的位置。第一、二个参数（假定为n,m)表示将视图切分为n\*m的区域，则第三个参数则表示在这样的切分中，该子视图所在的区域序号（序号是按行优先顺序赋的）。注：序号可以跨行结合。
`matplotlib.plotpy.subplots()`，参数有两个，设为`m`与`n`,则此函数返回一个figure与一个含有`m`\*`n`个子视图的元组
4. **标签**：`matplotlib.plotpy.legend()`。将绘制时带有`label`选项的标签在视图中绘制出来
5. **轴标签**：直接使用`xlabel`或对一个`axe`类型的对象使用`xlbel`方法，为图像中的横纵坐标命名
6. **刻度**：`set_xticks`——设置x轴上的刻度为自定义的特殊标签（其排布是自适应的）

#### 二维图像

| 函数 | 用途 |
| :---: | :---: |
| `matplotlib.plotpy.plot()` | 折线 |
| `matplotlib.plotpy.pie()` | 饼状图 |
| `matplotlib.plotpy.bar()` | 柱状图 |
| `matplotlib.plotpy.scatter()` | 散点图 |
| `matplotlib.plotpy.hist()` | 二维直方图 |
| `matplotlib.plotpy.boxplot()` | 箱式图 |
| `matplotlib.plotpy.quiver()` | 向量场 |

他们的参数列表基本相同，常用设置有：线条样式、数据点样式、标签、颜色、坐标
详情：[*Official Reference*](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html "\\(0 v 0)/")

#### 三维图像

> 记得在绘制之前将`axe`的参数`projection`设置为`3d`
> 以及导入`mpl_toolkits.mplot3d`模块

| 函数 | 用途 |
| :---: | :---: |
| `axe.plot_surface()` | 绘制一个三维的面 |
| `axe.plot_wireframe()` | 绘制网格图 |
| `axe.contour()` | 绘制一个三维图像的等高线 |
[简介](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html "其实这里面有更多绘制三维图像的函数")

> 注：记得若不清楚有什么上色风格，可以使用`print(plt.style.available)`

### 2.2.2 例子

```python
import numpy as npy
import matplotlib.pyplot as matplt

# 经典配置
matplt.rc('font', size = 10)
matplt.rc('text', usetex = True)
# matplt.rc('font', family = 'SimHei')

accuracy = 1000
f = lambda x: npy.exp(x) * (npy.cos(x) + x * npy.sin(x))
g = lambda x: npy.exp(-x) * npy.sin(x)**3
x = npy.linspace(-10, 10, accuracy)

fig = matplt.figure(figsize = (8, 6), facecolor = 'white', frameon = True, dpi = 100.0)
axe = fig.add_axes([0.12, 0.12, 0.76, 0.76])  # 依次为：左侧距离、上侧距离、高度、宽度（均不能超过1，因为这是按比例来的）
axe.grid(visible = True, linestyle = '-.', linewidth = 0.25)  # 设置网格
axe.set_yscale('symlog')  # 开启坐标轴魔法

axe_copy = axe.twinx()  # 创造一个拥有隐形x轴，独立y轴的视图
axe_copy.set_yscale('linear')

# 具体设置边框
axe_copy.spines[['left', 'bottom', 'top']].set_color(None)
axe_copy.spines['right'].set_color('green')
axe.spines['left'].set_color('red')
axe.spines['bottom'].set_color('blue')
axe.spines[['right', 'top']].set_color(None)

axe.plot(x, f(x), 'c-', label = r'$e^x(x\mathrm{sin}x+\mathrm{cos}x)$')
axe_copy.plot(x, g(x), 'r-.', label = r'$\frac{\mathrm{sin}^3x}{e^x}$')

# 改颜色
axe.tick_params(axis = 'y', colors = 'red')  # 全部
axe.get_xticklabels()[5].set_color('blue')  # 部分
axe_copy.tick_params(axis = 'y', colors = 'green')

axe.legend()
axe_copy.legend()
matplt.savefig('ahhhhhhhh.png', dpi = 500)
matplt.show()
```

```python
import numpy as npy
import matplotlib.pyplot as matplt

# 经典配置
matplt.rc('font', size = 10)
matplt.rc('text', usetex = True)
# matplt.rc('font', family = 'SimHei')

accuracy = 1000
f = lambda x: npy.exp(x) * (npy.cos(x) + x * npy.sin(x))
g = lambda x: npy.exp(-x) * npy.sin(x)**3
h = lambda x: npy.exp(x**2)
x = npy.linspace(-10, 10, accuracy)

fig = matplt.figure(figsize = (9, 9), facecolor = 'white', frameon = True, dpi = 100.0)
axe0 = matplt.subplot2grid((3, 3), (0, 0), colspan = 2, fig = fig)
axe1 = matplt.subplot2grid((3, 3), (1, 0), colspan = 2, rowspan = 2, fig = fig)
axe2 = matplt.subplot2grid((3, 3), (0, 2), rowspan = 3, fig = fig)

formula = [r'$e^x(x\mathrm{sin}x+\mathrm{cos}x)$', r'$\frac{\mathrm{sin}^3x}{e^x}$', '$e^{x^2}$']
settings = ['r-', 'b-', 'c-']

axe0.grid(visible = True, linestyle = '-', linewidth = 0.25)
axe1.grid(visible = True, color = 'purple', linestyle = '-', linewidth = 0.25)
axe2.grid(visible = True, color = 'yellow', linestyle = '-', linewidth = 0.25)

axe0.spines['left'].set_color('red')
axe0.spines['bottom'].set_color('green')
axe0.spines[['right', 'top']].set_color(None)
axe0.set_yscale('symlog')
axe0.tick_params(axis = 'x', colors = 'green')
axe0.tick_params(axis = 'y', colors = 'red')
axe1.spines['left'].set_color('red')
axe1.spines['bottom'].set_color('green')
axe1.spines[['right', 'top']].set_color(None)
axe1.tick_params(axis = 'x', colors = 'green')
axe1.tick_params(axis = 'y', colors = 'red')
axe2.spines['left'].set_color('red')
axe2.spines['bottom'].set_color('green')
axe2.spines[['right', 'top']].set_color(None)
axe2.set_yscale('log')
axe2.tick_params(axis = 'x', colors = 'green')
axe2.tick_params(axis = 'y', colors = 'red')

axe0.plot(x, f(x), settings[0], label = formula[0])
axe0.legend()
axe1.plot(x, g(x), settings[1], label = formula[1])
axe1.legend()
axe2.plot(x, h(x), settings[2], label = formula[2])
axe2.legend()

matplt.tight_layout()
matplt.savefig('ah.png', dpi = 500)
matplt.show()
```

## 2.3 `Pandas`模块

> 待补充

# **3 高等数学领域的应用**

## 3.1 符号计算`SymPy`

### 3.1.1 基础
```python
import sympy as sym

x_sym = sym.symbols('x')# 创建符号常量x，这个对象存于x_sym中
x1,x2,x3,x4 = sym.symbols('m0:4')# 创建符号变量m1,...,m3,存于x1,...,x4中
expr = sym.sin(x_sym)# 可以如同一般变量一样正常计算
expr.n(); expr.evalf(); # 查看表达式的值，默认精度是15位有效数字
expr.subs({x:2})# 代值计算
factor()# 因数分解
```
### 3.1.2 绘图

学习`SymPy`绘图的理由（也许唯一？）：方便
在这一方面，`SymPy`的`plot`语法类似于MMA里的：`plot(f1, f2, (x, x_min, x_max))`
> 注：`sympy`的绘图模块主要在`sympy.plotting`模块里
> 可用函数：`plot`,`plot3d`,`plot_parametric`,`plot3d_parametric`

以及SymPy有一个比较好的地方：隐函数绘图`sympy.plot_implicit`
实例：
1.  ```python
    import sympy as sym
    from sympy.parsing.sympy_parser import parse_expr # 这个函数会自动根据给定的函数配置好参数


    if __name__ == '__main__':
        exp = 'x**4 + y**4 - x**2 - y**2'
        sym.plotting.plot_implicit(parse_expr(exp))
        # 等价于
        # sym.plotting.plot_implicit(x**4 + y**4 - x**2 - y**2, (x, -2, 2), (y, -2, 2))
        # 其实2不是这个隐函数的上界，但是我懒得算了
    ```
2.  ```python
    import matplotlib.pyplot as matplt
    import sympy as sym
    import sympy.plotting as symplt


    if __name__ == '__main__':
        matplt.rc('font', size = 10)
        matplt.rc('text', usetex = True)
        x, y = sym.symbols('x y')
        symplt.plot3d(x**2 - y**3/4, (x, -5, 5), (y, -5, 5))
        # 绘制形如z = f(x, y)的曲面
    ```
3.  ```python
    import matplotlib.pyplot as matplt
    import sympy as sym
    import sympy.plotting as symplt


    if __name__ == '__main__':
    matplt.rc('font', size = 10)
    matplt.rc('text', usetex = True)
    s, t = sym.symbols('s t')
    symplt.plot3d_parametric_surface((2 + s/2*sym.cos(t/2))*sym.cos(t), (2 + s/2*sym.cos(t/2))*sym.sin(t),
                                     s/2*sym.sin(t/2), (t, 0, sym.pi*2), (s, -1, 1))
    # 绘制三维参数曲面（此处为莫比乌斯环）
    ```

### 3.1.3 ~~高贵的~~符号解

1. **极限** 
   **主要函数**：`limit()`
   用法：`limit(f(x), x, 0)`,即
   $$\underset{x\to 0}{\text{lim}}f(x)$$
   > 注：oo := INFINITY
2. **导数** 
   > ~~快对`sympy.diff`使用`help()`吧！~~

   **主要函数**：`diff()`
   例：`sympy.diff(sympy.sin(x)*sympy.ln(y), x, y, x)`,等价于：
   $$\frac{\partial ^3(\sin (x) \log (y))}{\partial x\, \partial y\, \partial x}$$
3. **级数**
   **主要函数**：`summation()`
   用法：`sym.summation(1/sym.factorial(k), (k, 0, sym.oo))`,即
   $$\sum _{k=0}^{\infty } \frac{1}{k!}$$
4. **Taylor**
   **主要函数**：`series()`
   用法：`f = sin(x); f.series(x, 0, 7)`,即
   $$\sin (x)=x-\frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040}+O\left(x^8\right)$$
5. **积分**
   **主要函数**：`integrate()`
   用法：`integrate(sin(2*x),(x, 0, pi/2))`,即
   $$\int_0^{\frac{\pi }{2}} \sin (2 x) \, dx$$
6. **求解代数方程**
   **主要函数**：`solve()`,`roots()`
   用法：`solve(f, x)`,即解出$f(x)=0$的关于$x$的符号解；而`roots()`在此基础上还能解析出重根信息
   同理，`solve(f(x,y), [x, y])`为解出$f(x,y)=0$的关于$x$,$y$的符号解
7. **求解微分方程**
   **主要函数**：`dsolve()`
   > 注：记得将需解函数通过`y = sympy.Function('y')`的方式声明为函数
   
   用法：`dsolve(eq1, y(x), ics = {})`,其中`eq1`为待解的微分方程，`ics`是含有限制条件的字典。比如若$y(0) = 0$,则可以有：`ics = {y(0):0}`

### 3.1.4 ~~暴力的~~数值解

#### 数值导数

已知：$f(\delta +x)=f(x)+f'(x)\delta +O(\delta )$
故有：
$$f'(x)\approx \frac{f(\delta +x)-f(x)}{\delta }$$
或：
$$f'(x)\approx \frac{f(\delta +x)-f(x-\delta )}{2 \delta }$$
对于二阶导，则可以利用$f(\delta +x)$与$f(x-\delta )$的二阶泰勒展开得到：
$$f''(x)\approx \frac{f(\delta +x)+f(x-\delta )-2 f(x)}{\delta ^2}$$

#### 数值积分
> 该来的还是会来的.jpg

**梯形公式**
讨论对象：设$f(x)\in \mathcal{R}[a,b]$，且$-\infty <a<b<+\infty$
若一个区间长度十分微小，我们可以~~不加证明地~~将其近似为一个梯形，即：
$$\int_a^b f(x) \, dx\approx \frac{(b-a)}{2} (f(a)+f(b))$$
那么如果我们将一个正常的区间切为n个，就可以有：
$$\int_a^b f(x) \, dx\approx \frac{(b-a) \left(2 \sum _{k=1}^{n-1} f\left(\frac{k (b-a)}{n}+a\right)+f(a)+f(b)\right)}{2 n}$$

**辛普森公式**
> 懒得写推导过程了

上公式：
$$\int_a^b f(x) \, dx\approx \frac{(b-a) \left(4 \sum _{k=1}^n f\left(\frac{(2 k-1) (b-a)}{n}+a\right)+2 \sum _{k=1}^{n-1} f\left(\frac{2 k (b-a)}{n}+a\right)+f(a)+f(b)\right)}{3 (2 n)}$$

#### 非线性方程组的解

**二分法求根**
> 原理：连续函数的介值性

**牛顿迭代法**

原理：
若$f(x)\in \mathcal{C}^2[a,b]$, $f(a)f(b) < 0$,且$f'(x)$在$[a,b]$上不变号，则$\exists \delta >0$,使得$\forall x_0 \in (x- \delta, x+\delta)$,构造序列$\{x_n\}$满足：
$$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)} ,i = 0,1,\ldots$$
则有:
$$\underset{n\to \infty }{\text{lim}}x_n=\xi$$
$\xi$即为所求根。

> *起始迭代点的选择*：
> 设$f(x)\in \mathcal{C}^2[a,b]$，且在区间$[a,b]$上满足:
> 1. $f(a)f(b)<0$
> 2. $f'(x) \neq 0$且$f''(x)$不变号
> 3. 起始点$x_0$满足$f(x_0)f''(x_0)>0$
> 
> 则可以保证序列$\{x_n\}$收敛至所求点

> 证明待补充

### 3.1.5 线性代数

#### 符号解

> 注：将一个sympy表达式转为通用表达式/函数的方法：`sympy.lambdify(symbols,expr,'numpy')`,这样可以返回一个与原表达式等效的函数
> 如果面对非表达式的sympy->numpy矩阵转换，可以考虑使用`numpy.array(A).astype(numpy.float64)`


**基础算子、操作**:（均为`sympy`内容）
| **operations**   	| **functions**               	    |
|------------------	|---------------------------------	|
| dot product      	| `A.dot(B)`                    	|
| $A^T$        	    | `A.T`                         	|
| cross product    	| `A.cross(B)`                  	|
| norm             	| `A.norm()`                    	|
| $det(A)$      	| `det(A)`                      	|
| $rank(A)$         | `A.rank()`                    	|
| combine          	| `A.row_join(B)` `A.col_join(B)` 	|
| copy             	| `A.copy()`                    	|
| delete partially 	| `A.row_del()` `A.col_del()`       |
| insert         	| `A.row_insert(pos,alpha)`         |
| $A^{-1}$         	| `A.inv()` or `A**(-1)`            |

**特殊矩阵**：
| **Matrix**                  	| **functions**                  	    |
|-----------------------------	|--------------------------------	    |
| $I_k$                       	| `sympy.eye(k)` n`umpy.identity(k)` 	|
| $0_{m*n}$                   	| `sympy.zeros(m,n)`               	    |
| $1_{m*n}$                   	| `sympy.ones(m,n)`                	    |
| $diag\{\lambda _1,\ldots\}$ 	| `sympy.diag([`$\lambda _1,\ldots$`])`   |
> 注：这里的`sympy`下的所有创造特殊矩阵的函数同样在`numpy`中也有

**线代操作**
| **descriptions** 	| **functions**   	|
|------------------ |-----------------	|
| 基础解系         	| `A.nullspace()`   	|
| 行最简型         	| `A.rref()`        	|
| 特征值           	| `A.eigenvals()`   	|
| 特征向量         	| `A.eigenvects()`  	|
| 对角化           	| `A.diagonalize()` 	|
| 可对角化          | `A.is_diagonalizable()`|

#### 数值解（`numpy`)

**特殊矩阵**：
| **descriptions** 	 | **functions**   	|
|------------------- |-----------------	|
| 范德蒙特阵(上至下)  | `numpy.vander()` |
| 矩阵转一维数组      | `numpy.diag`     |

**运算**
| **descriptions** 	 | **functions**   	|
|------------------- |-----------------	|
| 矩阵乘法           | `A.dot()` or `@`  |
| 内积               | `numpy.inner()`  |
| 叉乘               | `numpy.outer()`  |
| 叉乘               | `numpy.outer()`  |
| 迹                 | `numpy.trace()`  |
> 注：在sympy中，$*$代表矩阵乘法，但在numpy中它则表示对应位置的元素相乘

**`numpy.linalg`中的操作函数**

| **function**    	    | **description**       	    |
|---------------------- |------------------------------ |
| `det`        	        | $det(A)$          	        |
| `eig`         	    | 特征根与特征向量               |
| `eigvals`     	    | 特征值                        |
| `inv`        	        | $A^{-1}$          	        |
| `pinv`        	    | $A^+$             	        |
| `solve`       	    | $Ax=\beta$的解      	        |
| `lstsq`       	    | $A^TAx=A^T \beta$(最小二乘解)  |
| `qr`          	    | QR分解                       	 |
| `svd`         	    | 奇异值分解                   	 |
| `norm`        	    | 范数                    	     |
| `matrix_rank` 	    | $rank(A)$         	         |


## 3.2 高等函数`SciPy`

### 3.2.1 积分

参数（其余函数除了增加积分区域，基本一致）：`quad(func, a, b, args=(), full_output=0, epsabs=1.49e-08, epsrel=1.49e-08, limit=50, points=None, weight=None, wvar=None, wopts=None, maxp1=50, limlst=50)`
* 定积分`scipy.integrate.quad()`
* 累次积分`scipy.integrate.dblquad()`,`scipy.integrate.tplquad()`,`scipy.integrate.nquad()`

### 3.2.2 非线性方程组的数值解

主要使用`scipy.optimize.fsolve()`,参数列表为：`fsolve(func, x0, args=(), fprime=None, full_output=0, col_deriv=0, xtol=1.49012e-08, maxfev=0, band=None, epsfcn=None, factor=100, diag=None)`，前两个参数为必选项，第一个为函数，第二个为起始点。

### 3.2.3 极值点

主要使用`scipy.optimize`中的函数
* 一元函数极值点：`fmin`(从一个起始点开始找极小值)、`fminbound()`(在给定范围内找极值点)
* 多元函数极值点：`minimize()`(从一个起始点寻找最小值，可以选择算法)

> 此部分内容少是因为`help()`能help你了解这些函数


# 4 概率论与数理统计

## 4.1 基础概念

### 4.1.1 真·基础知识

在此设连续型随机变量$X$的分布函数为$F(x)$，则：

$\alpha$分位数
:  $\forall \alpha \in (0,1)$，若有$x_\alpha$使得$P\{X \leq x_\alpha\}=\alpha$，则称$\alpha$为这个分布的$\alpha$分位数。类似地，$\forall \alpha \in (0,1)$，若有$x_\alpha$使得$P\{X > x_\alpha\}=\alpha$，则称$\alpha$为这个分布的上$\alpha$分位数

数学期望
:  设**离散**随机变量的分布律为
    $$P\{X = x_k\} = p_k,k=1,2,\ldots$$
    若级数$\sum \limits_{k=1}^\infty x_kp_k$绝对收敛，则随机变量$X$的数学期望$E(X)$定义为
    $$E(X) := \sum \limits_{k=1}^\infty x_kp_k$$
    对于**连续型**随机变量$X$，当$\int_{-\infin}^{+\infty}xF(x)\,dx$绝对收敛时，则为：
    $$E(X):=\int_{-\infin}^{+\infty}xF(x)\,dx$$

方差
: 记方差为$D(X)$或$Var(X)$，标准差为$\sigma(X)$，则有：
    $$D(X) := E\{[X-E(X)]^2\}$$
    $$\sigma(X) := \sqrt{Var(X)}$$

> 对于样本容量为$n$的样本方差，此处会有点特殊：$Var(x) = \frac{1}{n-1} \sum \limits_{k=1}^n (x-\bar{x})^2$(为了保证无偏性)

偏度
: 用于衡量随机变量在横向上的分布状况（小于0偏左，大于0偏右）
    $$v:=E[(\frac{X-E(X)}{\sigma(X)})^3]=\frac{E[(X-E(X))^3]}{\sigma^3(X)}$$

峰度
: 用于衡量随机变量在纵向上的分布状况（越大极值处越高）
    $$v:=E[(\frac{X-E(X)}{\sigma(X)})^4]=\frac{E[(X-E(X))^4]}{\sigma^4(X)}$$

协方差
: 对于两个随机变量$X$与$Y$，我们称
    $$Cov(X,Y):=E\{[X-E(X)][Y-E(Y)]\}$$
    为$X$、$Y$的协方差，并称
    $$\rho_{XY}:=\frac{Cov(X,Y)}{\sigma(X)\sigma(Y)}$$
    为随机变量$X$与$Y$的*相关系数*

原点矩
: 设$X$为随机变量，若$E(X^k),k=1,2,\ldots$存在，则称$E(X^k)$为$X$的$k$阶原点矩

中心矩
: 设$X$为随机变量，若$E[(X-E(X))^k],k=1,2,\ldots$存在，则称$E[(X-E(X))^k]$为$X$的$k$阶中心矩

混合矩
: 设$X$与$Y$为随机变量，
若$E(X^kY^l),k,l=1,2,\ldots$存在，则称$E(X^kY^l)$为$X$与$Y$的$k+l$阶混合矩
若$E[(X-E(X))^k(Y-E(Y))^l],k,l=1,2,\ldots$存在，则称$E[(X-E(X))^k(Y-E(Y))^l]$为$X$与$Y$的$k+l$阶混合中心矩

协方差矩阵
: 对于n维随机变量$(X_1,X_2,\ldots,X_n)$，其中任意两个变量的二阶混合中心矩均存在，则称矩阵
$$C=\left [Cov(X_i,X_j)
    \right]
    _{n \times n}
$$
为n维随机变量$(X_1,X_2,\ldots,X_n)$的协方差矩阵（显然地，这样的矩阵是一个对称阵）

样本$p$分位数
: 设有容量为n的样本观测值$x_1,x_2,\ldots,x_n$，若有$x_{p'}$($x_{p'}$不一定在样本中)满足：
  1. 至少有$np$个观测值不高于$x_{p'}$
  2. 至少有$n(1-p)$个观测值不低于$x_{p'}$
   则称$x_{p'}$为样本的$p$分位数

> 通用求法：
> 将样本按从小到大的次序排列，于是：
> $$ x_p = \left \{
> \begin{aligned}
>     x_{[np]+1},\text{if } np \notin \mathbb{Z}\\
>     \frac{1}{2}(x_{np}+x_{np+1}),\text{if } np \in \mathbb{Z}
> \end{aligned}
> \right.
> $$

四分位数间距
: 计样本的$\frac{k}{4}$分位数为$Q_k$,则称四分位数间距$\mathcal{IQR} := Q_3-Q_1$

疑似异常值
: 若数据点$x$的值高于$Q_3+1.5\mathcal{IQR}$或低于$Q_1-1.5\mathcal{IQR}$，则我们认为这样的点为疑似异常点

经验分布函数
: 设$X_1,X_2,\ldots,X_n$为总体$F$的一个样本，用$S(x)$表示$X_1,X_2,\ldots,X_n$中不高于$x$的随机变量个数，则我们定义经验分布函数为：
$$F_n(x)=\frac{1}{n}S(x),x \in (-\infin,+\infty)$$

### 4.1.2 参数假设检验

1. $\mathbf{Z}$**检验法**
   设总体$X\sim N(\mu,\sigma^2)$，$\sigma$已知，$\mu$未知，$X_1,X_2,\ldots,X_n$是来自$X$的样本。我们提出假设$H_0$：$\mu=\mu_0$，备选假设$H_1$：$\mu \not ={\mu_0}$
   令: $$\mathop{Z}=\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}$$
   已知检验的显著性水平为$\alpha$，记标准正态分布的上$\alpha/2$分位数为$z_{\alpha/2}$，则当$|Z| > z_{\alpha/2}$时，拒绝假设$H_0$；反之接受$H_0$
   > 注：之所以选择两侧的面积来构造小概率事件（**双侧检验**），是因为这样保证我们得出的结果是无偏估计。

   那么当假设$H_0$：$\mu\leq\mu_0$，又如何检测呢？
   令$$\mathop{\widetilde{Z}}=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}$$
   可以判断，$\widetilde{Z}\geq Z$，且$\widetilde{Z}\sim N(0,1^2)$
   不妨记标准正态分布的上$\alpha$分位数为$z_{\alpha}$
   则有：$$P(Z\geq z_{\alpha}) \leq P(\widetilde{Z}\geq z_{\alpha}) = \alpha$$
   于是在该问题中，拒绝域为$Z\geq z_{\alpha}$
2. $\mathbf{t}$**检验法**
   由于在一个总体、两个总体下可以建立与t分布相关的样本估计，因此t检验法也有两种情况：

   *单变量参数检验*
   设总体$X\sim N(\mu,\sigma^2)$，$\sigma$、$\mu$未知，$X_1,X_2,\ldots,X_n$是来自$X$的样本。我们提出假设$H_0$：$\mu=\mu_0$，备选假设$H_1$：$\mu \not ={\mu_0}$
   设$S$为样本方差，令：$$\mathop{T}=\frac{\bar{X}-\mu_0}{S/\sqrt{n}}$$
   已知检验的显著性水平为$\alpha$，记自由度为$n-1$的$t$分布的上$\alpha/2$分位数为$t_{\alpha/2}(n-1)$,则拒绝域为$|t| \geq t_{\alpha/2}(n-1)$
   > 假设$H_0$：$\mu\geq\mu_0$在t检验法下的做法照葫芦画瓢即可

   *双变量参数检验*：
   设有总体$X\sim N(\mu_1,\sigma_1^2),Y\sim N(\mu_2,\sigma_2^2)$,$X_1,X_2,\ldots,X_{n_1}$是来自$X$的样本,$Y_1,Y_2,\ldots,Y_{n_2}$是来自$Y$的样本，可以分别计算得样本均值、样本方差：$\bar{X},s_1^2,\bar{Y},s_2^2$
   当关系$\sigma_1^2=\sigma_2^2$已知时，可选：$$T=\frac{\bar{X}-\bar{Y}}{S_w/\sqrt{n_w}}$$($S_w,n_w$的含义[参见](#4-统计量与抽样分布))
   当关系$n_1=n_2$已知且$\sigma_1^2=\sigma_2^2$未知时，考虑合成新变量$Z:=X-Y$与新样本$Z_i:=X_i-Y_i$，则有新总体$Z\sim N(\mu_z,\sigma_z^2)$，其中$\mu_z=\mu_1-\mu_2,\sigma_z^2=\sigma_1^2+\sigma_2^2$，从而化为了单变量参数检验问题。
3. $\mathbf{\chi^2}$**检验法**(卡方检验法)
   其实和前两者一样，就是利用与$\chi^2$分布的样本估计关系来进行假设检验。
   所以，观察相关的估计关系，可以思考我们所在推断的未知变量：

   设总体$X\sim N(\mu,\sigma^2)$，$\sigma$、$\mu$未知，$X_1,X_2,\ldots,X_n$是来自$X$的样本。我们提出假设$H_0$：$\sigma^2 = \sigma_0^2$
   令：$$\chi^2=\frac{(n-1)s^2}{\sigma_0^2}$$
   已知检验的显著性水平为$\alpha$，记自由度为$n-1$的$\chi^2$分布的上$\alpha/2$分位数为$\chi^2_{\alpha/2}(n-1)$,$\alpha/2$分位数为$\chi^2_{1-\alpha/2}(n-1)$,则拒绝域为$\left\{\chi^2 \leq \chi^2_{1-\alpha/2}(n-1) \ \mathop{or} \ \chi^2 \geq \chi^2_{\alpha/2}(n-1)\right\}$
   > 假设$H_0$：$\sigma^2 \leq \sigma_0^2$在$\chi^2$检验法下的做法照葫芦画瓢即可
4. ***Kolmogorov-Simirnov*****检验法**
   我们定义在一个样本容量为n的样本中*Kolmogorov-Simirnov*检验统计量为$T:=\mathop{Sup}\limits_x|F_n(x)-F(x)|$，其中$F(x)$为猜测的分布函数，$F_n(x)$为经验分布函数，则$T$的拒绝域为$T_{n,\alpha}$
> 寄，写到这里发现我原来是在预习我们概率要学的内容（后知后觉）
5. $\mathbf{F}$**检验**
   设有总体$X\sim N(\mu_1,\sigma_1^2),Y\sim N(\mu_2,\sigma_2^2)$,$X_1,X_2,\ldots,X_{n_1}$是来自$X$的样本,$Y_1,Y_2,\ldots,Y_{n_2}$是来自$Y$的样本，可以分别计算得样本方差：$s_1^2,s_2^2$
   $\mu_1,\mu_2$未知，检验假设$H_0$：$\sigma_1^2=\sigma_2^2$
   令$$F=\frac{s_1^2}{s_2^2}$$已知检验的显著性水平为$\alpha$，并记$F(n_1-1,n_2-1)$分布的上$\alpha$分位数为$F_\alpha(n_1-1,n_2-1)$，则拒绝域为$\left\{F \leq F_{1-\alpha/2}(n_1-1,n_2-1) \ \mathop{or} \ F \geq F_{\alpha/2}(n_1-1,n_2-1)\right\}$
> 这里的内容可以酌情参考[假设检验](#6-假设检验)

更多请参考[*补充部分*](#补充一概率论的部分理论知识)

## 4.2 应用

### 4.2.1 基本属性与方法

| 功能           | 函数                       |
|--------------|--------------------------|
| 均值           | `numpy.mean()`           |
| 标准差          | `numpy.std()`            |
| 方差           | `numpy.var()`            |
| 极差           | `numpy.ptp()`            |
| 协方差（一行为一个样本）          | `numpy.cov()`            |
| 中位数          | `numpy.median()`         |
| 相关系数         | `numpy.corrcoef()`       |
| 众数           | `pandas.mode()`          |
| 峰度           | `scipy.stats.kurtosis()` |
| 偏度           | `scipy.stats.skew()`     |
| 上$\alpha$分位数 | `numpy.quantile()`       |
| 极大似然估计       | `scipy.stats.rv_discrete.fit()`      |
| 概率密度函数 | `scipy.stats.rv_discrete.pdf()` |
| 分布函数 | `scipy.stats.rv_discrete.cdf()` | 
| 分位数 | `scipy.stats.rv_discrete.ppf()` | 
| 随机数 | `scipy.stats.rv_discrete.rvs()` |
| 置信区间 | `scipy.stats.rv_discrete.interval()` |

* *Kolmogorov-Simirnov*检验法使用`scipy.stats.kstest`
* z检验法使用函数为`statsmodels.stats.weightstats.ztest()`
* t检验法使用函数为`statsmodels.stats.weightstats.ttest_ind()`
* 单/双因素方差分析使用`statsmodels.api.stats.anova_lm()`
  > 注：它的第一个参数（模型）需要通过`statsmodels.formula.api.ols().fit()`以创建，其公式参数请参考[官网介绍](https://www.statsmodels.org/stable/example_formulas.html)
* 一元线性回归方程使用`curve_fit`或`statsmodels.formula.api.ols().fit()`（后者不会直接得到函数，需要用`.predict({'x':a})`得到预测值）

### 4.2.3 数据清洗

#### 重复观测处理

利用`pandas`库：(此处默认`a`为`DataFrame`)
* 检测数据集中每一行是否有重复：`a.duplicated()`（每行返回一个`bool`值）
* 移出重复值`a.drop_duplicates()`

#### 缺失值处理

* 检测`NaN`或`None`：`a.isnull()`，此处`a`为`Series`(每个元素返回一个`bool`值，有即`True`) 
* 数据过滤：`DataFrame.dropna()`（删除）
* 数据填充：`DataFrame.fillna()`（填充指定值）
  * 插值填充 就是在数据填充时将指定值改为变化的插值函数

#### 异常值处理

##### 寻找异常值

* 标准差法
  $outlier > \bar{x}+n\sigma$或$outlier < \bar{x}-n\sigma$
  若$n=2$则$outlier$为异常值；若$n=3$则$outlier$为极端异常值
* 箱线图法
  $outlier > Q_3+n\mathcal{IQR}$或$outlier < Q_1-n\mathcal{IQR}$
  若$n=1.5$则$outlier$为异常值；若$n=3$则$outlier$为极端异常值
##### 处理异常值

参考缺失值处理，但这里没有打包好的函数可以用

# 5 线性规划

## 5.1 概念与一般模型

*一般形式*
$$ max(min) z = \bm{c^Tx}$$
$$s.t.\left \{
\begin{aligned}
    \bm{Ax = \beta}\\
    \bm{x'}\geq 0 
\end{aligned}
\right.
$$
其中$z$为决策变量，$x'$由$x$的部分变量组成。而且限制条件中的$\bm{Ax = \beta}$也可以为其他不等号。

可行解
: 满足所有约束条件的决策向量$\bm{x} \in \mathcal{R^n}$

可行域
: 全部可行解构成的集合（是n维欧氏空间中的一个点集，而且应当是一个凸多面体）

最优解
: 使目标函数达到最优值（最值）的可行解

## 5.2 利用Python的求解方式

### 5.2.1 利用`scipy.optimize`模块

`scipy`中的线性规划的标准型为：
$$ (min) z=\bm{c^Tx}\\
s.t. \left \{
\begin{aligned}
    \bm{Ax \leq \beta}\\
    \bm{A_{eq}}·x = \bm{b_{eq}}\\
    \bm{L_b}\leq x \leq \bm{U_b}
\end{aligned}
\right.
$$
模块中的函数参数也基本参照此标准型：
`linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='interior-point', callback=None, options=None, x0=None)`
其中`bounds`为各变量的取值范围组成的元组。`[None,None]`表示$x \in (-\infty,+\infty)$,`[-1,None]`表示$x \in [-1,+\infty]$

> 注：鉴于标准型仅取最小值，因此要求取最大值时可以考虑求$-z$的最小值

### 5.2.2 利用`cvxopt.solvers`求解

标准型：
$$ (min) z=\bm{c^Tx}\\
s.t. \left \{
\begin{aligned}
    \bm{Ax \leq \beta}\\
    \bm{A_{eq}}·x = \bm{b_{eq}}
\end{aligned}
\right.
$$

参数基本同上式。注：传入参数应当是`cvxopt.matrix`类型的，其中元素均应为浮点数，且其默认以列结合的方式构建矩阵。
且使用时记得导入`numpy`

### 5.2.3 利用`cvxpy`求解

其标准型同上，但在代码中体现为两个部分：目标函数、约束条件。
``` python
# Define and solve the CVXPY problem.
x = cp.Variable(n)
prob = cp.Problem(cp.Minimize(c.T@x),
                 [A @ x <= b])
prob.solve()
```
这是一个简单的利用`cvxpy`求解线性规划问题的过程。其中：第一行处，n为求解的变量数；第二行处，`cvxpy.Minimize(c.T@x)`为目标函数,`[A @ x <= b]`为约束条件（这个列表内可以有多个参数）。这个过程中传入的参数可以是`ndarray`

## 5.3 灵敏度分析

在现实中的线性规划问题中，我们需要考虑一个问题：$A$、$c^T$中的参数浮动对最优解的影响有多大？用什么方法评估这一变化？

书中给出的方案有二：
1. 改变参数，再算一遍
2. 观察`scipy.optimize.linprog`的返回值中的`slack`参数，其值为：$\beta - \bm{Ax}$

## 5.4 应用：投资模型

这个问题的核心是权衡收益与风险，情景如下：

市场上有n种资产$s_i(i=1,2,\ldots,n)$可供选择，现用数额为$M$的**相当大**的资金做一个时期的投资，且这n种资产中每一个资产$s_i$都具有以下属性：**平均收益率**$r_i$，**风险损失率**$q_i$，交易时的**费率**为$p_i$，并存在最低交易额$u_i$。
且我们认为总体风险为$\mathop{max}\limits_{i \in \{1,2,\ldots,n\}}q_ix_i$($x_i$表示购买额)。在交易时若购买额低于$u_i$，则交易额按购买$u_i$计算（但不会交易这么多的实物），反之，则按购买额计算。
同时，已知同期银行存款利率为$r_0$,且$p_0$,$q_0$均为0

假设我们投资各资产占总资产量的占比为$x_i$，由于$M$是**相当大**的（即$M >> u_i$），所以我们可以对收益做一个近似：$(r_i-p_i)x_i$

那么我们就可以分析得到：
*目标函数*
$$
\left \{
\begin{aligned}
    \mathop{max} \sum \limits_{i=0}^n (r_i-p_i)x_i\\
    \mathop{min} \{\mathop{max} \limits_{1 \leq i \leq n} \{q_ix_i\}\}
\end{aligned}
\right.
$$
*约束条件*
$$
\left \{
\begin{aligned}
    \sum \limits_{i=0}^n (1+p_i)x_i = M\\
    \bm{x} \geq 0\\
\end{aligned}
\right.
$$

进而可以衍生三个模型：

**控制风险模型**
出于控制风险的目的，我们可以考虑为总风险的影响设置一个上界$a$，即$$\mathop{max}\limits_{i \in \{1,2,\ldots,n\}}\frac{q_ix_i}{M} \leq a$$

那么最终模型如下：

*目标函数*
$$\mathop{max}\sum \limits_{i=0}^n(r_i-p_i)x_i$$
*约束条件*
$$
\left \{
\begin{aligned}
    \mathop{max}\limits_{i \in \{1,2,\ldots,n\}}\frac{q_ix_i}{M} \leq a\\
    \sum \limits_{i=0}^n (1+p_i)x_i = M\\
    \bm{x} \geq 0\\
\end{aligned}
\right.
$$

运行模型如下：
```python
import numpy as npy
import matplotlib.pyplot as matplt
from scipy.optimize import linprog


# raw data
r = npy.array([0.05, 0.28, 0.21, 0.23, 0.25])
q = npy.array([0.0, 0.025, 0.015, 0.055, 0.026])
p = npy.array([0., 0.01, 0.02, 0.045, 0.065])
M = 1

def temp_linprog(upper_risk):
	c = p - r
	A = npy.array(npy.diag(q))
	b = npy.array([upper_risk]*5)
	Aeq = npy.array([p.T + npy.array([1.0] * 5).T])
	beq = npy.array([M])
	bounds = tuple(zip([0] * 5, [None] * 5))
	ans = linprog(c, A, b, Aeq, beq, bounds)
	return -ans.fun


if __name__ == '__main__':
	accuracy = 200
	upper_risk = npy.linspace(0, 0.1, accuracy)
	profit = []
	for risk in upper_risk:
		profit.append(temp_linprog(risk))
	matplt.rc('font', size = 10)
	matplt.rc('text', usetex = True)
	matplt.plot(upper_risk, profit, 'c-')
	matplt.xlabel('$Upper Risk$')
	matplt.ylabel('$Q$')
	matplt.savefig('test1.png', dpi = 1000)
	matplt.show()
```
![模型一图像](pics/Fin_module_1.png)

**控制收益模型**

有时候，我们会考虑求稳，因此我们考虑在固定收益$Q$的情况下，最小化风险,于是建立以下模型：

*目标函数*
$$\mathop{min} \{\mathop{max} \limits_{1 \leq i \leq n} \{q_ix_i\}\}$$
*约束条件*
$$
\left \{
\begin{aligned}
    \sum \limits_{i=0}^n(r_i-p_i)x_i = Q\\
    \sum \limits_{i=0}^n (1+p_i)x_i = M\\
    \bm{x} \geq 0\\
\end{aligned}
\right.
$$

> tips: 对于一些目标函数为非线性函数的模型可以考虑将其线性化（常见手段是多设一个向量）

运行模型如下：
```python
import numpy as npy
import matplotlib.pyplot as matplt
import cvxpy as cpy


# raw data
r = npy.array([0.05, 0.28, 0.21, 0.23, 0.25])
q = npy.array([0.0, 0.025, 0.015, 0.055, 0.026])
p = npy.array([0., 0.01, 0.02, 0.045, 0.065])
M = 1


def temp_linprog(profit):
	x = cpy.Variable(6, pos = True)
	A_ub = npy.c_[npy.diag(q), -npy.ones(5)]
	b_ub = npy.zeros(5)
	A_eq = npy.c_[(r-p), p.T+npy.ones(5)]
	A_eq = npy.c_[A_eq.T, npy.zeros(2)]
	b_eq = npy.array([profit, 1])
	prob = cpy.Problem(cpy.Minimize(x[5]), [A_ub@x <= b_ub, A_eq@x == b_eq, x >= npy.zeros(6)])
	prob.solve()
	return prob.value

if __name__ == '__main__':
	accuracy = 200
	profits = npy.linspace(0.05, 0.267, accuracy)
	risk = []
	for profit in profits:
		risk.append(temp_linprog(profit))
	matplt.rc('font', size = 10)
	matplt.rc('text', usetex = True)
	matplt.plot(profits, risk, 'c-')
	matplt.ylabel('$Risk$')
	matplt.xlabel('$Q$')
	matplt.savefig('test1.png', dpi = 1000)
	matplt.show()
```
![模型二图像](pics/Fin_module_2.png)

**权衡模型**
> 人总是喜欢调和的

*目标函数*
$$\mathop{max} \{s\sum \limits_{i=0}^n (r_i-p_i)x_i - (1-s)\mathop{max} \limits_{1 \leq i \leq n} \{q_ix_i\}\}$$

称$s$为“投资偏好系数”，用于调和投资与风险。

运行模型如下：
```python
import numpy as npy
import matplotlib.pyplot as matplt
from scipy.optimize import linprog
from mpl_toolkits import mplot3d


# raw data
r = npy.array([0.05, 0.28, 0.21, 0.23, 0.25])
q = npy.array([0.0, 0.025, 0.015, 0.055, 0.026])
p = npy.array([0., 0.01, 0.02, 0.045, 0.065])
M = 1


def temp_linprog(s):
	c = npy.r_[-s * (r - p), (1 - s) * npy.ones(1)]
	A_ub = npy.c_[npy.diag(q), -npy.ones(5)]
	b_ub = npy.zeros(5)
	A_eq = npy.r_[p+npy.ones(5), npy.zeros(1)].reshape(1, 6)
	b_eq = npy.array(1.)
	bounds = tuple(zip([0]*6, [None]*6))
	ans = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds)
	return ans


if __name__ == '__main__':
	accuracy = 2000
	s = npy.linspace(0.00001, 0.999999, accuracy)
	profits = []
	risks = []
	for i in s:
		temp = temp_linprog(i)
		profits.append(npy.r_[r-p, npy.zeros(1)].dot(temp.x))
		risks.append(temp.x[5])
	matplt.rc('font', size = 10)
	matplt.rc('text', usetex = True)
	axe1 = matplt.subplot(2, 1, 1)
	axe1.plot(s, profits, 'r-.', label = '$profits$', linewidth = 1)
	matplt.legend()
	axe2 = matplt.subplot(2, 1, 2)
	axe2.plot(s, risks, 'b-', label = '$risks$', linewidth = 1)
	matplt.legend()
	matplt.savefig('test1.png', dpi = 1000)
	matplt.show()
```

![模型三图像一](pics/Fin_module_3_1.png)
*s-risk/s-profit 类散点图*
![模型三图像二](pics/Fin_module_3_2.png)
*s-risk/s-profit 折线图*

## 5.5 习题中的思考——多目标线性规划

### 问题

试考虑以下场景：
$$
\mathbb{max} : \mathbf{z} = (z_1,z_2,\ldots,z_n)^T = \mathbf{C}x \\
s.t.\left \{
\begin{aligned}
    A_{ub}x \leq \mathbb{b_{ub}}\\
    A_{eq}x = b_{eq}\\
    L_b \leq x \leq U_b
\end{aligned}
\right.
$$
对于目标向量值函数中的每个分量求最值。

1. **最小距离理想解法**
   （有点像方差）假定对于每个目标函数的分量，这样的线性规划问题都是可解的，且解为$(z_1^*,z_2^*,\ldots,z_n^*)$,则考虑构造函数：$$\mathop{\phi}(Z):=\sqrt{\sum \limits_{i=1}^n (z-z_i^*)^2}$$
   则只需求$min\,\phi[Z(x)]$的解即可
2. **线性加权法**
   一眼即可明白——更换目标函数为$$\mathop{max}\limits_{x \in \mathbb{D}}\sum \limits_{i=1}^n\omega_iz_i$$，其中$\mathbb{D}$代表约束条件所限制的域
3. **最大最小法** / **最小最大法**
   在此例中表示亦较为简单。其核心思想为：考虑最坏情况。
   令目标函数为：
   $$\mathop{max}\limits_{x \in \mathbb{D}}\mathop{min}\limits_{1 \leq i \leq n} Z_i(x)$$，其中$\mathbb{D}$代表约束条件所限制的域
4. **目标规划法**
   ~~I have *最小距离理想解法*, I have *线性加权法*, uh, **目标规划法**~~
    $$\mathop{\phi}(Z):=\sqrt{\sum \limits_{i=1}^n \lambda_i(z-z_i^*)^2}$$
    取$\phi[Z(x)]$的最小值即可
5. **模糊数学法**
   我们先求出各分量在限制条件下的最大值$z_i^+$与最小值$z_i^-$，则令伸缩因子$d_i=z_i^+-z_i^-$，于是可以考虑令原目标函数下降至一个条件，构建新的线性规划模型：
   我们在此记$\mathbf{D}=(d_1,d_2,\ldots,d_n)^T$，$\mathbf{Z^*}=(z_1^*,z_2^*,\ldots,z_n^*)$
   则新模型为：
   $$
    \mathbb{max} : \mathbf{Z} = \lambda\\
    s.t.\left \{
    \begin{aligned}
    \mathbf{C}x-\lambda\mathbf{D} \geq \mathbf{Z^*-D}\\
    A_{ub}x \leq \mathbb{b_{ub}}\\
    A_{eq}x = b_{eq}\\
    L_b \leq (x,\mathbf{\lambda}) \leq U_b
    \end{aligned}
    \right.
    $$
    若此线性规划的解为$(x_1^*,\ldots,x_n^*,\lambda)$,则原问题解为$Z^*=\mathbf{C}x^*$(此处$x^*$表示$(x_1^*,x_2^*,\ldots,x_n^*)$)

* *数学模糊法 实践*-（书中P194的5.5）
    ```python
    import numpy as npy
    import cvxpy as cv

    if __name__ == '__main__':
	    C = npy.array([
		    [100, 90, 80, 70],
		    [0, -3, 0, -2]
	    ], dtype = npy.float64)
	    A_ub = npy.array([
		    [1, 1, 0, 0],
	    	[0, 0, 1, 1],
	    	[-3, 0, -2, 0],
	    	[0, -3, 0, -2]
	    ], dtype = npy.float64)
	    b_ub = npy.array([30, 30, -120, -48], dtype = npy.float64)
	    b_lower = npy.zeros((4,), dtype = npy.float64)

	    x = cv.Variable(4)
	    Prob1_upper = cv.Problem(cv.Maximize(C[0]@x), [A_ub@x >= b_ub, x >= b_lower])
	    Prob1_upper.solve()
	    z1 = Prob1_upper.value
	    Prob1_lower = cv.Problem(cv.Minimize(C[0] @ x), [A_ub @ x >= b_ub, x >= b_lower])
	    Prob1_lower.solve()
	    z2 = Prob1_lower.value

	    Prob2_upper = cv.Problem(cv.Maximize(C[1]@x), [A_ub@x >= b_ub, x >= b_lower])
	    Prob2_lower = cv.Problem(cv.Minimize(C[1] @ x), [A_ub @ x >= b_ub, x >= b_lower])
	    Prob2_upper.solve()
	    z3 = Prob2_upper.value
	    Prob2_lower.solve()
	    z4 = Prob2_lower.value

        d1 = z1 - z2
        d2 = z3 - z4
        D = npy.array([d1, d2])
        Z = npy.array([z1, z3])
        y = cv.Variable(5)
        Ct = npy.c_[C, -D]
        At = npy.c_[A_ub, npy.zeros((4,), dtype = npy.float64)]
        Prob = cv.Problem(cv.Maximize(y[4]), [Ct@y >= Z-D, At@y >= b_ub, y >= npy.zeros((5,), dtype = npy.float64)])
        Prob.solve()
	    x_solved = y.value
        res = C@x_solved[:4]
	    res[1] = -res[1]  # 因为要求求的是min
	    print('res = ', res)
        print('x = ', x_solved[:4])
    ```
# 6 整数规划与非线性规划

> 即域的收缩与阶数的扩张

## 6.1 直接可用的函数、方法

* 整数线性规划：利用`cvxpy`求解。并在原求解过程中令`integer = True`即可
* 非线性规划
  1. 利用`scipy.optimize`求解，函数为`minimize()`
  2. 利用`cvxopt`求解，方法为`solvers.qp()`
  3. 利用`cvxpy`求解，与求解线性规划时所用函数一致（需保证其可被凸优化）

## 6.2 整数规划

### 6.2.1 0-1整数规划

> 这样的模型诞生于指派n个人去做m项任务的过程中，人的选择只有做和不做，而我们在全局上所关心的问题只有在执行任务中所有人消耗的总成本。

#### 模型概述

我们令$x_{ij} \in \{0,1\}$,其中$i,j=1,2,\ldots,n$，则模型为：
$$
min \ z = \sum \limits_{i=1}^n \sum \limits_{j=1}^n c_{ij}x_{ij}\\
s.t. \left \{
    \begin{aligned}
        \sum \limits_{j=1}^n x_{ij} = 1, \quad\forall i \in \{1,2,\ldots,n\}\\
        \sum \limits_{i=1}^nx_{ij} = 1, \quad\forall j \in \{1,2,\ldots,n\}\\
    \end{aligned}
\right. 
$$

#### 求解方法——匈牙利算法

> 考虑邻接矩阵的特点，这个算法可用于图论中的“最大匹配问题”（挖坑.jpg）

**Theorem1**
设效率矩阵$C=(c_{ij})_{n \times n}$中任意一行（列）的所有元素都加（减）一个常量$k$，得到新矩阵$B=(b_{ij})_{n \times n}$， 则以$B$为效率矩阵的指派问题与以$C$为效率矩阵的指派问题通解，但前者的最优值等于后者的最优值加（减）$k$
**Theorem2** 独立零元素定理
若方阵中既有零元素也有非零元素，则覆盖方阵内所有0元素的最小直线数恰好等于那些位于不同行、不同列的零元素的最多个数。

而我们欲求的解即根据**Theorem1**变换之后所得方阵，将其各独立零元素替换为1，其余替换为0之后所得矩阵，比如：
$$
\left(
\begin{array}{cccc}
 6 & 7 & 11 & 2 \\
 4 & 5 & 9 & 8 \\
 3 & 1 & 10 & 4 \\
 5 & 9 & 8 & 2 \\
\end{array}
\right) \rArr
\left(
\begin{array}{cccc}
 0 & 0 & 0 & 1 \\
 1 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 \\
 0 & 0 & 1 & 0 \\
\end{array}
\right)
$$
左为效率矩阵，右为最优解（注：最优解**应当**是满秩的）

#### 延申——广义指派模型

* 最大化指派问题：不妨设效率矩阵的元素为$c_{ij}$，则令$M=max\{c_{ij}\}$,则得到新效率矩阵$(M-c_{ij})_{n \times n}$，于是就可以化为标准指派模型
* 人数、任务数不匹配问题：将效率矩阵用0补充成方阵（即追加虚拟人、虚拟任务）
* 如果一个人可以指派多项任务时：~~分身术~~把这个人的对各任务的数据复制多次，即把一个人看作几个人
* 某任务不能指派某人的问题：把该人的该任务的代价设置为infinity

### 6.2.2 其他整数规划算法

> 咕咕咕

## 6.3 非线性规划

> 一些定义：
> 全局最优值$\lrArr$最大值
> 局部最优值$\lrArr$极大值

**非线性规划的一般模型**

$$
min \quad f(\mathbf{x})\\
s.t. \left \{
    \begin{aligned}
        \mathbf{G(x)} \leq \mathbf{0}\\
        \mathbf{H(x)} = \mathbf{0}
    \end{aligned}
    \right.
$$
其中$\mathbf{G(x)}$、$\mathbf{H(x)}$均为向量值多元函数；$f(\mathbf{x})$为实值多元函数。

### 6.3.1 理论
对于无约束非线性规划与等式约束非线性规划，请自行复习数分B笔记~~然后抄一百遍~~
而对于不等式约束非线性规划，则有：

(外点)罚函数法
:  这个方法的核心在于令目标函数加上一个罚函数后，在取超出约束范围的点时不断增大负担，使其最终经过迭代后会趋近于最优点，同时让问题转化为无约束、等式约束非线性规划。方案如下：（以标准模型为例）
构造新目标函数：$$F(x) = f(x) + \sigma P(x)\\ P(x) = \sum \limits_{k=1}^n\phi(g(x))+\sum\limits_{k=1}^m\psi(h(x))$$
其中，$\sigma$为一个较大的正数，$g(x)$为不等式约束，$h(x)$为等式约束，$\phi,\psi$满足：
    1. 连续
    2. $g(x)$在界内时为0，在界外时为正数
    3. $h(x)$在满足等式时为0，其余情况下均为正数
因此，我们会一般地认为：
$$\phi(x) = [max\{0,-|g(x)|\}]^\alpha\\ \psi(x) = |h(x)|^\beta\\ \alpha,\beta \geq 1$$
这样的方法也可以离散化：（上面方法存在精度不足的问题）
$$F_k(x) = f(x) + \sigma_k P(x)$$且$\{\sigma_n\}$满足$\lim\limits_{n\rarr\infin}\sigma_n=+\infin$,$\lim\limits_{n\rarr\infin}\sigma_nP(x_k)=0$
$x_k$为$F_k(x)$以$x_{k-1}$为起始点的最优解（可以考虑令$\{\sigma_n\}$以指数递增）
> 另有内点罚函数法与乘子法在此不做展开

# 7 插值与拟合

## 7.1 插值

### 7.1.1 理论部分

* Lagrange插值法：看丘维声高等代数
* Newton插值法：还是看丘维声高等代数
* 分段线性多项式插值
  $$P(x) = \frac{x-x_i}{x_{i+1}-x_i}f(x_{i+1})+\frac{x-x_{i+1}}{x_i-x_{i+1}}f(x_i),x \in [x_i,x_{i+1}]$$(即对每两个点使用一次Lagrange插值)
* 分段抛物线插值（即对每三个点使用一次Lagrange插值）
* 样条插值
  先有定义：

  样条函数
  : 给定区间$[a,b]$上的一个划分：$$\Delta : a=x_0<x_1<\ldots<x_n=b$$
  如果函数$S(x)$满足：
    1. 在每个小区间$[x_i,x_{i+1}]$上是$m$次多项式
    2. $S(x)\in \mathbb{C}^{m-1}[a,b]$
   
    则称$S(x)$为关于划分$\Delta$的$m$次样条函数
  
  而利用给定的部分点值计算样条函数便是样条插值
* 二维数据的样条插值
  原理与一维相同，但要求改为$S(x)$满足$m-1$阶连续可偏导

### 7.1.2 可用函数

* 利用`scipy.interpolate`模块
  1. 一维插值`interp1d`
  2. 二维插值`interp2d`
  3. 二维离散插值`griddata`
* 利用`Pandas`模块的`Series`与`DataFrame`下的`interpolate`方法

## 7.2 拟合

### 7.2.1 最小二乘拟合

***问题***：已知一组二维点$(x_i,y_i)(i = 1,2,\ldots,n)$,$x_i$互不相同,要求寻求一个曲线$y=f(x)$,使$f(x)$在某种准则下与给定的数据点最接近。

而在最小二乘拟合中，我们定义：

最小二乘原则
: 采用“$J = \sum \limits_{i=1}^n(f(x_i)-y_i)^2$达到最小”作为接近的判断标准的一种原则

从而采用最小二乘原则的拟合方法被称为最小二乘法。

#### 线性最小二乘拟合

给定一个在实数域上线性无关的基$\varphi_1,\varphi_2,\ldots,\varphi_n$,假定拟合函数是这个基的线性组合：$$f=\sum\limits_{k=1}^na_k\varphi_k$$
由于f是给定点集的拟合函数，因此我们令$$\nabla J(a_1,a_2,\ldots,a_n)=(\frac{\partial J}{\partial a_1}, \ldots, \frac{\partial J}{\partial a_n})=\mathbf{0}$$
从而
$$\sum\limits_{j=1}^n(\sum\limits_{i=1}^n\varphi_i(x_i)\varphi_k(x_i))a_j=\sum\limits_{i=1}^ny_i\varphi_k(x_i),k=1,2,\ldots,n$$
不妨令
$$
\mathbf{R}=\left(
\begin{array}{cccc}
 \varphi_1(x_1) & \varphi_2(x_1) & \cdots  & \varphi_n(x_1) \\
 \varphi_1(x_2) & \varphi_2(x_2) & \cdots  & \varphi_n(x_2) \\
 \vdots  & \vdots  &   & \vdots  \\
 \varphi_1(x_n) & \varphi_2(x_n) & \cdots  & \varphi_n(x_n) \\
\end{array}
\right),\\\mathbf{A}=(a_1,a_2,\ldots,a_n)^T,\mathbf{Y}=(y_1,y_2,\ldots,y_n)^T
$$
则有：
$$\mathbf{R^TRA=R^TY}$$
于是便可解了
> 证明参考丘维声高等代数关于正交阵的那一章
> 形式为$A^TAx=A^T\beta$

#### 非线性最小二乘拟合

即当$f(x)$无法由一个基线性表出时，比如$$f(x)=\frac{x}{ax+b}\quad or \quad f(x) = a_1+a_2e^{-a_3x}+a_4e^{-a_5x}$$
则问题转化为目标函数为$min\ J = \sum \limits_{i=1}^n(f(x_i)-y_i)^2$的无约束非线性规划问题

#### 拟合函数的选择

> 观察法

### 7.2.2 可用函数

* 利用`numpy`模块的`polyfit`进行多项式拟合
* 利用`scipy.optimize`模块的`curve_fit`进行各类最小二乘拟合

# 8 微分方程

## 8.1 数值解

> 符号解见[sympy](#313-高贵的符号解)

问题：
$$
\left\{
    \begin{aligned}
        \frac{dy}{dx} = f(x,y)\\
        y(x_0)=y_0
    \end{aligned}
\right.
$$
我们求微分方程的数值解就是求目标函数在$n$个点上的点值。

**理论**
* Taylor展开
  已知$y(x_n+h)=y(x_n)+y'(x_n)h+\frac{y''(x_n)}{2!}h^2+o(h^2)$
  则不妨取到展开的一次项，并令$h=x_{n+1}-x_n$，于是递推式有$$y_{n+1}=y_n+hf(x_n,y_n)$$
* 数值积分
  由题得$dy=f(x,y)\,dx$，于是便有$$y(x_{n+1})-y(x_n)=\int_{x_n}^{x_{n+1}}f(x,y(x))\, dx$$
  右侧积分计算参考[数值积分](#314-暴力的数值解)

**实践**

1. 手动实现上面的理论部分(doge)
2. 使用`scipy.integrate.odeint(func, y0, t)`以求解，其中`func`为函数序列，`y0`为初始条件序列，`t`为数值解所对应的$x$值序列（其中序列的第一个元素为初始条件所对应的x值），返回一个列数与函数序列长度相等的矩阵。
3. 使用`scipy.integrate.solve_ivp()`以求解

### 8.2 利用`sympy`进行拉氏变换

> ?(没学过相关数学理论)

# 9 综合评价的方法

## 9.1 基本概念

**概念**
1. 评价对象
2. 评价指标
3. 权重
4. 评价模型（即如何将权重与指标组合成综合评价指标）

**评价指标的筛选**
1. 最小均方差法
2. 极大极小离差法
3. 条件广义方差极小法（未学）
4. 极大不相关法（未学）

**预处理**
设有$n$个评价对象，$m$个指标，第$i$个评价对象的第$j$个指标值为$a_{ij}$，令$M_j=\mathop{max}\limits_{1\leq i \leq n}a_{ij},m_j=\mathop{min}\limits_{1\leq i \leq n}a_{ij}$
1. 一致化处理（即将同时需求最大、最小以及居中型指标的问题通过预处理统一为一种指标的问题）
   1. 极小$\rarr$极大：取倒数$x_j'=\frac{1}{x_j}$或平移$x_j'=M_j-x_j$
   2. 居中$\rarr$极大：$$x_j'=\left\{
    \begin{aligned}
      \frac{2(x_j-m_j)}{M_j-m_j},\quad m_j \leq x_j \leq \frac{M_j+m_j}{2}\\
      \frac{2(M_j-x_j)}{M_j-m_j},\quad \frac{M_j+m_j}{2} < x_j \leq M_j
    \end{aligned}
    \right.$$(即找个我们所期望的中枢位置，然后按罚函数的思路构造)
   3. 区间$\rarr$极大：设限制范围为$[b_{min},b_{max}]$，则令$c_j=\mathop{max}\{b_{min}-m_j,M_j-b_{max}\}$，于是：$$x_j'=\left\{
    \begin{aligned}
      1-\frac{b_{min}-x_j}{c_j},\quad x_j < b_{min}\\1,\quad x_j \in [b_{min},b_{max}]\\1-\frac{x_j-b_{max}}{c_j},\quad x_j > b_{max}
    \end{aligned}
    \right.$$
  2. 无量纲化处理
     1. 统计学意义上的标准化$$a_{ij}^*=\frac{a_{ij}-\mu_j}{s_j}$$
     2. 代数学意义上的标准化$$a_{ij}^*=\frac{a_{ij}}{\sum\limits_{i=1}^na_{ij}^2}$$
     3. 比例变换法（以极大型指标为例）$$a_{ij}^*=\frac{a_{ij}}{M_j}$$
     4. 极差变换法（以极大型指标为例）$$a_{ij}^*=\frac{a_{ij}-m_j}{M_j-m_j}$$
     5. 功效系数法（以极大型指标为例）$$a_{ij}^*=c\times\frac{a_{ij}-m_j}{M_j-m_j}+d$$

## 9.2 数学模型

1. **线性加权** $$f_i=\sum\limits_{j=1}^mw_ja_{ij}^*$$
2. **TOPSIS法**
   即由正理想解与负理想解建立了一个评价距离的概念
   设评价指标矩阵经一致化和无量纲化处理后所得评价矩阵$\mathbf{A^*}=(a_{ij}^*)_{n\times m}$(若存在加权参数，则评价矩阵为$\mathbf{\tilde{A}^*}=A^*\times diag\{\omega_1,\omega_2,\ldots,\omega_m\}$)
   令正理想解为：$\mathbf{C^+}=(c_1^+,c_2^+,\ldots,c_m^+)^T$，负理想解为$\mathbf{C^-}=(c_1^-,c_2^-,\ldots,c_m^-)^T$，其中$$c_j^+=\mathop{max}\limits_{1\leq i \leq n}a_{ij}^*\\ c_j^-=\mathop{min}\limits_{1\leq i \leq n}a_{ij}^*$$
   记各评价对象的评价向量为$\beta_i$，即$\mathbf{A^*}=(\beta_1,\beta_2,\ldots,\beta_n)^T$,则有：$$s_i^+=\lVert\beta_i-\mathbf{C^+}\rVert\\s_i^-=\lVert\beta_i-\mathbf{C^-}\rVert$$
   于是得到评价参数：$$f_i=\frac{s_i^-}{s_i^++s_i^-}$$
3. **灰色关联度分析**
   指定分辨系数为$\rho$，然后经过与TOPSIS法中相同的操作进行一致化与无量纲化处理，依照正理想解的生成方法得到评价矩阵$\mathbf{A^*}$与比较序列$\mathbf{\beta_0}=(b_{01},b_{02},\ldots,b_{0m})$,定义灰色关联系数：$$\xi_{ij}:=\frac{\mathop{min}\limits_{1\leq s \leq n}\mathop{min}\limits_{1\leq k \leq m}\left|b_{0k}-a_{sk}^*\right|+\rho\mathop{max}\limits_{1\leq s \leq n}\mathop{max}\limits_{1\leq k \leq m}\left|b_{0k}-a_{sk}^*\right|}{\left|b_{0j}-a_{ij}^*\right|+\rho\mathop{max}\limits_{1\leq s \leq n}\mathop{max}\limits_{1\leq k \leq m}\left|b_{0k}-a_{sk}^*\right|}$$其中$\rho\in[0,1]$（显然由$\mathbf{\beta_0}$定义，$\mathop{min}\limits_{1\leq s \leq n}\mathop{min}\limits_{1\leq k \leq m}\left|b_{0k}-a_{sk}^*\right|=0$)
   那么评价参数为：$$f_i=\sum\limits_{k=1}^m\omega_k\xi_{ik}$$
4. **熵值法**
   
   特征比重
   : 设第i个评价对象的第j个观测值的标准化数据$a_{ij}^*>0$，则定义第i个观测对象的第j项指标的特征比重为$$p_{ij}=\frac{a_{ij}^*}{\sum\limits_{i=1}^na_{ij}^*}$$

   熵值
   : 记第$j$项指标的熵值为$e_j$，则：$$e_j:=-\frac{1}{\mathrm{ln}\, n}\sum\limits_{i=1}^np_{ij}\mathrm{ln}\,p_{ij}$$

   差异系数
   : 记第$j$项指标的差异系数为$g_j$，则：$$g_j:=1-e_j$$

   于是我们可以生成第$j$项指标的权重系数：$$\omega_j:=\frac{g_j}{\sum\limits_{i=1}^mg_i}$$，那么综合评价值为:$$f_i:=\sum\limits_{j=1}^m\omega_jp_{ij}$$

5. **层次分析法**（步骤有些复杂，在此不做记录）

# 10 图论

# 11 多元分析

## 11.1 判别分析

问题：已知有$r$类判别对象$A_1,A_2,\ldots,A_r$，每一类$A_i$由含有$m$个指标的$n_i$个样本决定。现给出一个判别对象$\mathbf{x}$，需判断其属于$A_1,A_2,\ldots,A_r$中的哪一类。我们在判断过程中，往往存在一套**判断规则**，即面对判断对象能给出可以作为分类判断依据的值的规则，进而我们可以构建判断函数$W(i,\mathbf{x})$

我们可以得到一些信息：
记$a_K^{(i)}$为类$A_i$的第$k$个样本的样本向量，则：
样本均值向量：$$\mathbf{\mu_i}=\frac{1}{n_i}\sum\limits_{k=1}^{n_i}a_k^{(i)}$$
离差矩阵：$$\mathbf{L_i}=\sum\limits_{k=1}^{n_i}(a_k^{(i)}-\mathbf{\mu_i})(a_k^{(i)}-\mathbf{\mu_i})^T$$（即将指标向量当作随机变量的协方差矩阵）

### 11.1.1 代码应用

此处所使用的函数均为创造了一个类似于`Problem`的对象，还需用`.fit()`等方法导入模型数据以及求解模型。
* 距离判别法：`sklearn.neighbors.KNeighborsClassifier()`
* *Fisher*判别法：`sklearn.discriminant_analysis.LinearDiscriminantAnalysis()`
* 贝叶斯判别法：`sklearn.native_bayes.GaussianNB()`
* 交叉检验判别法准确率：`sklearn.model_selection.cross_val_score()`
* 各标准化方法：`sklearn.preprocessing`

> 显然由`Python`的命名规则可知，前三个在创造`class`，而第四个只是一介普通函数

```python
import pandas as pd
import numpy as npy
import sklearn.neighbors as skn
import sklearn.preprocessing as skp
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score


if __name__ == '__main__':
	source = pd.read_excel('data/11第11章  多元分析/Pdata11_2.xlsx', header = None).values
	X = source[:-2, 1:-1].astype(npy.float64)
	X_new = skp.StandardScaler().fit_transform(X)
	knn = skn.KNeighborsClassifier(n_neighbors = 3, metric = 'mahalanobis', metric_params = {'V': npy.cov(X_new.T)})
	Y = source[:-2, -1].astype(int)
	test = source[-2:, 1:-1]
	knn.fit(X, Y)
	print('距离判别法：')
	print(knn.predict(test))
	print(knn.score(X, Y))
	print(cross_val_score(knn, X, Y, cv = 2).mean())
	# 验证

	cls = LDA()
	cls.fit(X, Y)
	print('Fisher判别法：')
	print(cls.predict(test))
	print(cls.score(X, Y))
	print(cross_val_score(cls, X, Y, cv = 2).mean())

	clss = GaussianNB()
	clss.fit(X, Y)
	print('贝叶斯判别法：')
	print(clss.predict(test))
	print(clss.score(X, Y))
	print(cross_val_score(clss, X, Y, cv = 2).mean())
```

### 11.1.2 理论

#### 距离判别法

核心：建立待判对象$\mathbf{x}$到$A_i$的距离$d(\mathbf{x},A_i)$，然后令判别函数$W(i,\mathbf{x})=d(\mathbf{x},A_i)$，若$W(k,\mathbf{x})=\mathop{min}\limits_{i=1,2,\ldots,r}{W(i,\mathbf{x})}$，则我们认为$\mathbf{x}\in A_k$

问题来到了：“距离”用什么方式计算？`sklearn.neighbors.KNeighborsClassifier`的默认计算为欧式距离，但书中推荐使用马氏距离（因为错判概率较低），可选的还有闵可夫斯基距离等

> 马氏距离
> : 我们分两种情况讨论:
>   1. r个总体协方差相同时:$$d(\mathbf{x},A_i):=\sqrt{(\mathbf{x}-\mu_i)^T\Sigma^{-1}(\mathbf{x}-\mu_i)}$$，其中$$\Sigma=\frac{1}{n-r}\sum\limits_{i=1}^r\mathbf{L_i}$$
>   2. r个总体协方差不同时:$$d(\mathbf{x},A_i):=\sqrt{(\mathbf{x}-\mu_i)^T\Sigma_i^{-1}(\mathbf{x}-\mu_i)}$$，其中$$\Sigma_i=\frac{1}{n_i-1}\mathbf{L_i}$$

#### Fisher判别法

令$\mathbf{L}=\sum\limits_{i=1}^r\mathbf{L_i}$，而后得到$\mathbf{L}^{-1}$
再令$\mathbf{B}=\sum\limits_{i=1}^rn_i(\mu_i-\mu)(\mu_i-\mu)^T$，其中$\mu=\frac{1}{n}\sum\limits_{i=1}^rn_i\mu_i$
然后计算$\mathbf{BL}^{-1}$的属于其最大特征值的特征向量$p$，令$u=\mathbf{L}^{-1}p$

于是可以计算$\omega_i=W(\mu_i):=u^T\mu_i$，然后对$A_i$重新排序，使得$\omega_i$从小到大排列，得到新序列$\omega_{i'}$。令$c_0=-\infin$，$c_r=+\infin$，$c_i=\frac{n_i\omega_i+n_{i+1}\omega_{i+1}}{n_i+n_{i+1}}$，则若$c_{k-1}< W(\mathbf{x}) < c_k$，则$\mathbf{x}\in A_k$

#### 贝叶斯判别法

设$r$个$m$维总体的密度函数分别为已知的$\phi_i(\mathbf{x})$，且有足够的把握认为$\mathbf{x}\in A_i$的概率为$p_i$，则令判别函数$$W(i,\mathbf{x}):=p_i\phi_i(\mathbf{x})$$，若$$W(k,\mathbf{x})=\mathop{max}\limits_{i=1,2,\ldots,r}W(i,\mathbf{x})$$，则$\mathbf{x}\in A_k$

### 11.1.3 判别准则的评价

误判率
: 设有总数为$N$的训练样本，对于每个总体$A_k$，有$N_k$个属于它的样本被误判为其他总体的样本，则误判率$P$的估计为$$\hat{P}:=\frac{\sum\limits_{i=1}^rN_i}{N}$$

* 回代误判率：即使用建立判别标准的各样本逐个带入判别标准计算误判率（以此方法估计误判率的结果较真实误判率偏小）
* 交叉误判率：在对每个$N_i$计数时，按如下方法计数：对于$A_i$中的样本，不重复地选取一个移除，然后按移除后的样本重建判别标准，再以被移除的那个样本作为训练样本，若出现误判则$N_i$加一。重复此操作直到$A_i$中的样本全部被取过一遍。

## 11.2 主成分分析

核心思想：降维，通过一些方法将主要因素提取出来作为新的指标，减少需要考虑的指标，在尽量不影响研究对象的精度的情况下简化模型。

### 11.2.1 代码

`sklearn.decomposition.PCA(n_components, copy = True)`，是一个`class`，详情请看`help()`或官方文档给出的内容。（同样需要经过`.fit()`以训练模型）
或者由于模型中的大部分操作为线性代数操作，因此可以考虑手动完成，

```python
import numpy as npy
from sklearn.decomposition import PCA


if __name__ == '__main__':
	source = npy.loadtxt('data/11第11章  多元分析/Pdata11_8.txt', delimiter = '\t')
	model = PCA()
	model.fit(source)
	print(model.explained_variance_ratio_)
	print(model.components_)
```

### 11.2.2 原理

设$X_1,X_2,\ldots,X_m$表示以$x_1,x_2,\ldots,x_m$为样本观测值的随机变量，如果有$c_1,c_2,\ldots,c_m$满足$\sum\limits_{i=1}^mc_i^2=1$使得下式$$Var\left(\sum\limits_{i=1}^mc_iX_i\right)$$的值达到最大，那么这样的一个解就是一个**主成分方向**。
一般来说，可代表$m$个随机变量的主成分不止一个。可以预见的是，为了保证主成分之间相互独立，多个主成分方向必然满足相互正交。同时，指标的量纲对于主成分分析影响极大，因此通常采用统计学意义上的标准化对数据进行无量纲化处理。进而可以求得这$m$个随机变量的相关系数矩阵，主成分方向便是此矩阵的特征向量（因此最后得到的矩阵的每一行为一个特征向量）。设每个主成分方向所属于的特征值为$\lambda_i(i=1,2,\ldots,n)$，则每个主成分的贡献度$\omega_j=\frac{\lambda_j}{\sum\limits_{i=1}^m\lambda_i}$

## 11.3 因子分析

### 11.3.1 代码

1. 根据下文原理手搓代码
2. `sklearn.decomposition.Factoranalysis()`（不提供因子旋转选项）
3. （库）`factor_analyzer`$\rArr$[*Documents*](https://factor-analyzer.readthedocs.io/en/latest/)

```python
# 展示一下factor_analyze库
import numpy as npy
import factor_analyzer as fa


if __name__ == '__main__':
	source = npy.loadtxt('data/11第11章  多元分析/Pdata11_8.txt', delimiter = '\t')
	model = fa.factor_analyzer.FactorAnalyzer(n_factors = 2, rotation = None)
	model.fit(source)
	eig = model.get_eigenvalues()
	rate = eig[0] / npy.sum(eig[0])
	print(rate*100)# 贡献率
	print(model.loadings_)
```

### 11.3.2 原理

可以认为，主成分分析的意图为将多个变量合成为较少的可以反映数据共性的共同变量。那么就可以认为因子分析在试图将多个因素拆解为由少量隐因素决定的变量

#### 数学模型

设$X=(x_1,x_2,\ldots,x_m)$为原始指标，$\mu=(\mu_1,\mu_2,\ldots,\mu_m)$为期望向量，$F=(f_1,f_2,\ldots,f_p),p < m$为公共因子向量，$\varepsilon=(\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_m)$为特殊因子向量。
$$X=\mu+AF+\varepsilon,\\
\left\{
\begin{aligned}
  x_1=\mu_1+a_{11}f_1+\ldots+a_{1p}f_p+\varepsilon_1\\
  x_2=\mu_2+a_{21}f_1+\ldots+a_{2p}f_p+\varepsilon_2\\
  \vdots\\
  x_m=\mu_m+a_{m1}f_1+\ldots+a_{mp}f_p+\varepsilon_m
\end{aligned}
\right.
$$
其中$$EX=\mu,\quad EF=0,\quad E\varepsilon=0\\Var(F)=I_m,\quad Var(\varepsilon)=diag\{\sigma_1^2,\sigma_2^2,\ldots,\sigma_m^2\}\\Cov(F,\varepsilon)=0$$

需要估计的对象：$A,D(\varepsilon)$

#### 因子分析

方法（主成分分析法）：
首先可以比较容易地求得相关系数矩阵$R$，然后得到其$m$个相互正交的特征单位向量$u_1,u_2,\ldots,u_m$以及对应的$m$个特征值$\lambda_1,\lambda_2,\ldots,\lambda_m(\lambda_1\geq\lambda_2\geq\ldots\geq\lambda_m)$，于是可以估计$A$：$$A=[\sqrt{\lambda_1}u_1,\sqrt{\lambda_2}u_2,\ldots,\sqrt{\lambda_p}u_p]$$这样估计下的贡献率计算为$\lambda_i/m$，计算共同度时则对$A$逐行求平方和。而$diag\{\sigma_1^2,\sigma_2^2,\ldots,\sigma_m^2\}$则利用$R-AA^T$上的主对角线上的元素进行估计。

#### 因子旋转

为了使隐因素易于解释，我们需尽量让隐因素变量前的因子绝对值尽量趋于1或0，因此，我们需要利用第一型正交矩阵使$A$“旋转”至我们理想的位置：
$$x-\mu=(AT)(T^TF)+\varepsilon=B\bar{F}+\varepsilon$$

常用方法：最大方差旋转法
> 书上未给出理论部分，甚至在实践上也只给了相关功能的函数名称

#### 因子得分

令$D=diag\{\sigma_1^2,\sigma_2^2,\ldots,\sigma_m^2\}$，$A$为当前模型下对因子矩阵的估计，则（在微积分极值求法下的）因子得分为$$\hat{F}=(A^TD^{-1}A)^{-1}A^TD^{-1}(x-\mu)$$
作用为：在面对样本中已知的数据时估计隐因子的值，可以用于诊断模型，也可以用作对对象的评价依据

## 11.4 聚类分析

### 11.4.1 原理

#### 基本操作

1. [无量纲化](#91-基本概念)
2. [距离函数](#距离判别法)$d(\omega_i,\omega_j)$
3. 相似系数计算
   1. 夹角余弦，即将任何两个样本$\omega_i$与$\omega_j$看成$p$维空间的两个向量，则$$cos\theta_{ij}=\frac{\sum\limits_{k=1}^pa_{ik}a_{jk}}{\sqrt{\sum\limits_{k=1}^pa_{ik}^2}\sqrt{\sum\limits_{k=1}^pa_{jk}^2}}$$进而有夹角余弦矩阵$$\Theta=[cos\theta_{ij}]_{n\times n}$$
   2. 皮尔逊相关系数：即常规意义上的相关系数

### 11.4.2 层次聚类

> 可以联想一下*Huffmann*树的构建方法

步骤：
1. 将每个样品独自聚成一类，构造$n$个类。
2. 根据所确定的样品距离计算公式，计算$n$个样品间的距离，得到距离矩阵
3. 找到最近的两个类，将它们构建成一个新类，其他类不变，得到$n-1$个类。
4. 重复步骤2、3，直到将所有样品归为一类

而样品距离计算公式则需根据实际情况进行考虑，至于具体计算方法，举一个例子：
**最短距离法**
若$G_i,G_j$均为样品的集合，那么两类间的距离为两类间距离最近的样品的距离，即$$D_{ij}=\mathop{min}\limits_{\omega_i\in G_i,\omega_j\in G_j}d(\omega_i,\omega_j)$$
若$G_i,G_j$不全是样品的集合，那么设$G_i={G_{i1},G_{i2}}$，则距离为$$D_{ij}=\mathop{min}\{D_{i1,j},D_{i2,j}\}$$

### 11.4.3 $K$均值聚类

目标：将总样本集$G$划分为$C$个子集：$G_1,G_2,\ldots,G_C$，这个样本集满足：
1. $G_1\cup G_2\cup\ldots\cup G_C = G$
2. $G_i\cap G_j = \varnothing (1\leq i < j \leq C)$
3. 任意$G_i$都是非平凡的
4. 设$m_i(i=1,2,\ldots,C)$为$C$个聚类中心（即$G_i$内的所有样本的均值）,记$$J_e=\sum\limits_{i=1}^C\sum\limits_{\omega\in G_i}\lVert\omega-m_i\rVert^2$$则$J_e$应尽可能地低。

算法：
1. 初始化，将总样本集$G$任意划分为$C$类，记为$G_1,G_2,\ldots,G_C$，并计算对应的$C$个初始聚类中心，然后计算$J_e$
2. 沿用之前的$C$个聚类中心，并将各样本集清空。再按最小距离原理将样品$\omega_j$进行聚类，即：若$d(\omega_j,m_k)=\mathop{min}\limits_{1\leq i \leq C}d(\omega_j,m_i)$，则$\omega_j\in G_k$（即将$\omega_j$加入$G_k$中），在所有样本被分类完成后，重新计算$C$个初始聚类中心与$J_e$
3. 若$J_e$与前一次相同（或聚类中心与前一次相同），则聚类完成，否则重复步骤2

那么，如何确定类数$C$呢？
在此的两种方法主要依靠绘制$C$关于某个参数的指标的图像观察确定。
#### 簇内离差平方法

望文生义，计算各聚类内样本的协方差矩阵，然后计算其各元素的平方之和，作为判断指标

#### 轮廓系数法

单点轮廓系数
: 假定数据集被拆分为$m$个簇$G_1,G_2,\ldots,G_m$，样本点$\omega_i$是$G_k$中的一个点。则令$$a_i:=\frac{1}{|G_k|-1}\sum\limits_{\omega_j\in G_k,\ \omega_j \not ={\omega_i}}d(\omega_i,\omega_j)\\ b_i:=\mathop{min}\limits_{1\leq r \leq m , \ r\not ={k}}\left\{\frac{1}{|G_r|}\sum\limits_{\omega_j\in G_r}d(\omega_i,\omega_j)\right\}$$即$a_i$为$G_k$中其他样本到样本$\omega_i$的平均距离，而$b_i$则为其他簇到样本$\omega_i$的平均距离的最小值。
那么我们定义**轮廓系数**为$$S_i:=\frac{b_i-a_i}{max\{a_i,b_i\}}$$

那么对于一个分划的轮廓系数$S$则定义为这个数据集中的所有样本点的轮廓系数的平均值。
其中，若$S<0$，则聚类效果不佳，我们期望轮廓系数会尽可能地接近1

### 11.4.5 代码实践

* 轮廓系数：`sklearn.metrices.silhouette_score(A, metric = 'euclidean')`
* 距离：`sklearn.cluster.hierarchy. distance.pdist()`（可以计算闵可夫斯基距离、马氏距离等），返回一个长度为$n(n-1)/2$的向量，可以用`~. distance.squareform()`将其转化为方阵
* 生成聚类树：`sklearn.cluster.hierarchy. linkage(B, 'method')`,其输入值`B`为上面的距离函数的输出值；其输出值可用于`~. fcluster()`生成聚类，也可以由`~. dendrogram()`绘制聚类树状图。
* K均值聚类：`sklearn.cluster.KMeans()`

```python
import pandas as pd
import numpy as npy
import matplotlib.pyplot as matplt
from sklearn.metrics import silhouette_score
import sklearn.cluster as scl

if __name__ == '__main__':
	source = pd.read_csv('data/11第11章  多元分析/iris.csv')
	data = source.iloc[:, :-1].values
	K_limit = 10
	# 判断KMean所需的k（虽然事实上iris数据中只包含三种花的共150个样本）

	ind_1 = []
	ind_2 = []
	for i in range(1, K_limit + 1):
		md = scl.KMeans(n_clusters = i)
		md.fit_transform(data)
		labels = md.labels_
		center = md.cluster_centers_

		# 轮廓系数法
		if i >= 2:
			ind_2.append(silhouette_score(data, labels, metric = "euclidean"))

		# 簇内离差平方法
		inner = []
		for label in set(labels):
			inner.append(npy.sum((data[labels == label] - center[label]) ** 2))
		ind_1.append(npy.sum(inner))

	matplt.rc('font', size = 10)
	axe1 = matplt.subplot(1, 2, 1)
	axe1.plot([i for i in range(1, K_limit + 1)], ind_1, 'r*-', label = 'TSSE')
	axe1.legend()
	axe2 = matplt.subplot(1, 2, 2)
	axe2.plot([i for i in range(2, K_limit + 1)], ind_2, 'c^-', label = 'silhouette')
	axe2.legend()
	matplt.savefig('KMean_show_select.png', dpi = 500)
	matplt.show()
```
运行图：![轮廓-离差对比](pics/KMean_show_select.png)
```python
import pandas as pd
import numpy as npy
import matplotlib.pyplot as matplt
import sklearn.cluster as scl
import scipy.cluster.hierarchy as sch

if __name__ == '__main__':
	source = pd.read_csv('data/11第11章  多元分析/iris.csv')
	data = source.iloc[:, :-1].values

	# 层次聚类（这里举例不恰当捏）
	Dis_list = sch.distance.pdist(data, metric = 'euclidean')
	cls_tree = sch.linkage(Dis_list)
	sch.dendrogram(cls_tree)
	matplt.savefig('cls_by_layers.png', dpi = 500)

	# KMeans
	fig1 = matplt.figure()
	model = scl.KMeans(n_clusters = 3)
	model.fit_transform(data)
	labels = model.labels_
	axes = fig1.subplots(1, 2)
	settings = ['r*', 'b^', 'c.']
	name = ['setosa', 'versicolor', 'virginica']
	for i in range(3):
		axes[0].plot(data[labels == i, 0], data[labels == i, 1], settings[i])
		axes[1].plot(data[i * 50:(i + 1) * 50, 0], data[i * 50:(i + 1) * 50, 1], settings[i], label = name[i])
	fig1.legend()
	fig1.savefig('KMean.png', dpi = 500)
	matplt.show()
```
运行图：
![层次](pics/cls_by_layers.png) ![KMean](pics/KMean.png)

# 12 多元回归分析

## 12.1 多元线性回归模型

### 12.1.1 数学模型

$$
y=\beta_0+\beta_1x_1+\beta_2x_2+\ldots+\beta_m x_m+\varepsilon
$$
其中$\varepsilon\sim N(0,\sigma^2)$，$\beta_i$是回归系数

### 12.1.2 最小二乘估计

对因变量$y$以及随机变量$X_1,X_2\ldots,X_m$进行$n$次测试得到$n$组数据，从而有
$$
\left\{
\begin{aligned}
  Y=X\beta+\varepsilon\\
  \varepsilon\sim N(0,\sigma^2 I_n)
\end{aligned}
\right.
$$
其中$$\beta=(\beta_0,\beta_1,\ldots,\beta_m)$$
$$
X =\left(
\begin{array}{cccc}
 1 & x_{11} & x_{12} & \cdots  & x_{1m} \\
 1 & x_{21} & x_{22} & \cdots  & x_{2m}  \\
 \vdots  & \vdots  & \vdots  & & \vdots  \\
 1 & x_{n1} & x_{n2} & \cdots  & x_{nm} \\
\end{array}
\right),\\
Y=(y_1,y_2,\ldots,y_n)^T,\varepsilon=(\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n)
$$
当$X$列满秩的时候可以得到$\beta$的估计$\hat{\beta}$为$$X^TX\beta=X^TY$$的解

### 12.1.3 回归方程的评估

由$\hat{Y}=X\hat{\beta}={\hat{y}_1,\hat{y}_2,\ldots,\hat{y}_n}$可得$Y$的估计值，从而可以计算残差平方和SSE（来自拟合的影响）与回归平方和SSR（来自随机波动的影响）：$$SSE=\sum\limits_{i=1}^n(\hat{y}_i-y_i)^2\\ SSR = \sum\limits_{i=1}^n(y_i-\bar{y})^2$$以及总平方和$$SST=SSR+SSE$$
自行计算上述平方和的期望可得：
|     | SSE | SSR | SST |
| --- | --- | --- | --- |
| 自由度 | $n-m-1$ | $m$ | $n-1$ |

于是可得检验：
$H_0:\beta_0=\beta_1=\ldots=\beta_m=0$（检验这样的线性关系是否存在）
$H_0^{(j)}:\beta_j=0$（检验与某个变量的线性关系是否存在）

对于$H_0$，有：$$F=\frac{SSR/m}{SSE/(n-m-1)}\sim F(m,n-m-1)$$
而对于$H_0^{(j)}$，假定$(X^TX)^{-1}=(c_{ij})_{m\times m}$，则有$$t_j=\frac{\hat{\beta}_j/\sqrt{c_{jj}}}{\sqrt{SSE/(n-m-1)}}\sim t(n-m-1)$$

> 显然若线性关系显著，就应当拒绝以上假设

还有一个指标：
**复相关系数**：$$R=\sqrt{\frac{SSR}{SST}}$$越靠近1，$y$与$X_1,X_2,\ldots,X_m$的线性关系越密切（一般认为需大于0.8或0.9）

## 12.2 线性回归的正则化

> 问题很简单：如果$X$并非满秩阵呢？

多重共线性
: 当设计矩阵的列向量间具有近似的线性相关时，即存在不全为$0$的常数$c_1,c_2,\ldots,c_m$使得$c_1x_1+c_2x_2+\ldots+c_m x_m \approx 0$，则称各自变量间有**多重共线性关系**

在这种情况下，最小二乘法的结果将会变得不理想
*于是有两种方法：~~高代经典退化阵处理方法与罚函数法~~*

### 12.2.1 岭回归

> 回忆一下我们证明以下命题的方法
> $$
> \left|
> \begin{matrix}
>   A & B \\
>   C & D
> \end{matrix}
> \right|
> = | AD-CB |
> $$

总存在$k>0$，使得$X^TX+kI$是非退化的，于是有$\hat{\beta}(k)=(X^TX+kI)^{-1}X^TY$，这样的估计被称为**岭估计**
而可以绘制关于$k$与$\hat{\beta}$各分量的曲线，被称为岭迹

*Properties*
1. 岭估计不是无偏估计
2. 岭估计是压缩估计（$\lVert\hat{\beta}(k)\rVert\leq\lVert\beta\rVert$）

#### k的选取问题

别问，问就是画岭迹，看拐点一把梭哈（doge）
这是方法一

或是求得岭估计的均方差误差$MSE(\hat{\beta}(k))=E\lVert\hat{\beta}-\beta\rVert^2$的极小值点
这是方法二

### 12.2.2 LASSO回归

对于
$$J(\beta)=\lVert X\beta-Y \rVert^2 + k\lVert\beta\rVert$$
选择合适的参数$k$，求得的极小值点即为LASSO回归下的估计参数

关于k的选取：（复读）
别问，问就是画岭迹，看拐点一把梭哈（doge）

## 12.3 Logistic回归模型

### 12.3.1 数学模型

Logistic回归模型所分析的是这样的函数：$f:\R^m\rarr\{0，1\}$
比较理想的是跃迁函数：
$$
f(x)=
\begin{cases}
  0, \beta_0+\beta_1x_1+\ldots+\beta_m x_m \leq 0\\
  1, \beta_0+\beta_1x_1+\ldots+\beta_m x_m > 0 
\end{cases}
$$
但是它的性质（连续性、可微）不佳，所以我们选择较为“平滑”的跃迁函数，即*Sigmoid函数*：
$$f_\beta(x)=\frac{1}{1+e^{-(\beta_0+\sum\limits_{j=1}^m\beta_jx_j)}}$$
其输出的是当取值为$x$时，$x$在对应的跃迁函数上被映射至1的概率$p$。
> 这样，其与多元回归分析的联系：
> $$\mathrm{ln}\left(\frac{p}{1-p}\right)=y^*=\beta_0+\beta_1x_1+\ldots+\beta_m x_m$$

对于一个样本集$\{(x_i,y_i)\}_{i\in I}$，我们采用极大似然估计的方法得到$\hat{\beta}$
若对于同一点$x_i$仍然测了多次，那么就回到了多元回归的问题上来：即按照最小二乘法运算。

> 注：
> 在将无量纲化的回归方程还原时，可以考虑手动推算一下
> 在多元回归分析中，对于经过统计学意义上的标准化后的数据，有：
> $$\beta_0=\bar{y}-\sigma_y\sum\limits_{i=1}^m\frac{\bar{x}_i\hat{\beta}_i}{\sigma_{x_i}}\\\beta_j=\frac{\sigma_y}{\sigma_{x_j}}\hat{\beta}_j\quad (j=1,2,\ldots,m)$$

## 12.4 相关函数与库

* 多元线性回归：`sklearn.linear_model.LinearRegression()`需要`fit`因变量观测向量`y`与自变量观测矩阵`x`（不包括元素全为1的第一列）
* 多元回归分析：一样可以利用`statsmodels. formula.ols(formula, data = df)`(格式见[第四章处](#42-应用))或是`statsmodel.api. OLS(y,X)`，其中前者只需按字典/DataFrame导入，后者则需导入模型中含一列1的增广矩阵$X$（可以使用`statsmodel.add_constant()`来增加）
* 岭回归：`sklearn.linear_model.Ridge()`，接受k，输出岭回归模型；`sklearn.linear_model.RidgeCV()`，接受待评估的k的数列，输出可以用于得到最优k值（在程序中的模型一般用$\alpha$、`alpha_`表示我们所称的k值）的模型。
* LASSO回归：`sklearn.linear_model.Lasso()`，接受k，输出LASSO回归模型；`sklearn.linear_model.LassoCV()`接受待评估的k的数列，输出可以用于得到最优k值的模型  
* Logistic回归模型：`statsmodel.api. Logit(y,X)`，建议`fit`时使用bfgs法(`method = 'bfgs'`)
* Logistic回归模型：`sklearn.linear_model.LogisticRegression()`，建议建立模型时令`solver = 'lbfgs'`
> 注：
> 以上来自机器学习库的函数均可以提供现成的复相关系数
> 以及，是个模型，就要fit

# 13 差分方程

> ~~累了，看数分吧，第一章就涉及这个~~

## 13.1 基础

差分
: 设$k\in \N_+$，则我们称$x_k$的一阶差分为：$$\Delta x_k = x_{k+1}-x_k$$
  对于高阶差分有：$$\Delta^nx_k=\Delta(\Delta^{n-1}x_k)$$

差分方程
: 差分方程中所含未知函数差分的最高阶数差分被称为该差分方程的阶，$n$阶差分方程的一般形式为：
  $$F(k,x_k,\Delta x, \Delta^2 x, \ldots, \Delta^n x) = 0$$
  或
  $$G(k,x_k,x_{k+1},\ldots,x_{k+n})=0$$

差分方程的解
: 若差分方程的解中含有相互独立的任意常数的个数恰好等于方程的阶数，则称这个解为差分方程的通解（即形如$k_1\eta_1+k_2\eta_2+\ldots+k_n\eta_n$的解）
  若一个解满足差分方程的初始条件，那么我们称这样的解为特解

线性差分方程
: 形式如$\sum\limits_{i=1}^na_i\Delta^ix_k=f(k)$的差分方程，可以等价为：$x_{k+n}+\sum\limits_{i=1}^na_ix_{k+n-i}=f(k)$的方程
  如果$f(k)=0$，则我们其为常系数齐次线性差分方程，反之则为非齐次线性方程

### 解法

对于n阶常系数线性齐次差分方程$x_{k+n}+\sum\limits_{i=1}^na_ix_{k+n-i}=0$，我们可以得到其**特征方程**：$\lambda^n+\sum\limits_{i=1}^na_i\lambda^{n-i}=0$
那么其通解的情况为：（我们在此将单根称为“一重根”）
设$\lambda$为该特征方程的$m$重实根，那么其通解中含有多项式$\lambda^k\sum\limits_{i=1}^mc_ik^{i-1}$；
设$r(\rm{cos}\theta+i\rm{sin}\theta)$为该特征方程的$m$重复根，那么其通解中含有多项式$r^k(\rm{cos}(k\theta)\sum\limits_{i=1}^mc_ik^{i-1}+\rm{sin}(k\theta)\sum\limits_{i=1}^mc_{m+i}k^{i-1})$
> 以上二式中$c_1,c_2,\ldots,c_{2m}$是任取的

其特解的情况为：
1. 利用常数变易法
2. 设$p,q\in F_{n+1}[x]$，则若常系数非齐次线性差分方程形如$f(k)=b^kp(k)$，那么：若b是方程的一个$r$重特征根，那么方程有特解$b^kk^rq(k)$;若b不是特征根，那么方程有特解$b^kq(k)$（$q(k)$的参数请考虑带入求解）

或：看数分

## 13.2 差分方程的代码求解

* `sympy.rsolve(eq, f(x), ics = {})`求符号解
* 数值解：它都离散了你还不会手搓？  

## 13.3 Leslie模型

## 13.4 减肥模型



# 补充一：概率论的部分理论知识

## 1. 分布

* 均匀分布
  $$f(x)=\left\{
    \begin{aligned}
        \frac{1}{b-a},\quad a \leq x \leq b \,(a < b)\\
        0, \quad \text{Other situations}
    \end{aligned}
    \right.
  $$
* 指数分布
  $$f(x)=\left\{
    \begin{aligned}
        \lambda e^{-\lambda x},\quad x > 0\\
        0, \quad x \leq 0
    \end{aligned}\qquad (\lambda > 0)
    \right.
  $$
* 伯努利分布
  $$
  X = 0,1\\
  P(X=0)=p\quad,P(X=1)=1-p
  $$
* 二项分布
  $$
  X = 0,1,2,\ldots,n\\
  \text{make} \quad q=1-p,\quad 0<p<1\\
  \text{then} \quad P(X=k)=C^k_np^kq^{n-k}
  $$
* 泊松分布
  $$
  X=0,1,2,\ldots\\
  P(X=k)=\frac{\lambda^k}{k!}e^{-\lambda}
  $$
* 几何分布
  $$
  X = 0,1,2,\ldots\\
  \text{make} \quad q=1-p,\quad 0<p<1\\
  \text{then} \quad P(X=k)=q^{k-1}p
  $$
* 超几何分布（略）
* 正态分布
  $$f(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}},\qquad -\infin<x<+\infin$$
* $\chi^2$分布
  设$X_1,\ldots,X_n$是相互独立的随机变量序列，它们均服从标准正态分布$N(0,1^2)$，令$Y=\sum\limits_{i=1}^nX_i^2$，则$Y\sim \chi^2(n)$,即自由度为$n$的$\chi^2$分布。
  $$f(x)=\left\{
    \begin{aligned}
        \frac{x^{\frac{n}{2}-1}e^{-\frac{x}{2}}}{2^{\frac{n}{2}}\Gamma(\frac{n}{2})},\quad x > 0\\
        0, \quad x \leq 0
    \end{aligned}
    \right.
  $$
  注：$\Gamma(n)=\int_0^{+\infin}x^{n-1}e^{-x}\,dx$
* $t$分布
  设随机变量$X,Y$相互独立，且$X\sim N(0,1^2),Y\sim \chi^2(n)$，则称随机变量$$T=\frac{X}{\sqrt{Y/n}}$$服从自由度为$n$的$t$分布，记作$T\sim t(n)$
  $$f(t)=\frac{\Gamma\left(\frac{n+1}{2}\right)}{\sqrt{n\pi} \; \Gamma\left(\frac{n}{2}\right)}\left(1+\frac{t^2}{n}\right)^{-\frac{n+1}{2}},\quad t\in(-\infin,+\infin)$$
* $F$分布
  设随机变量$X,Y$相互独立，且$X\sim \chi^2(n_1),Y\sim \chi^2(n_2)$,则称随机变量$$F=\frac{X/n_1}{Y/n_2}$$服从第一自由度为$n_1$,第二自由度为$n_2$的$F$分布，记为$F\sim F(n_1,n_2)$
  $$f(x)=\left\{
  \begin{aligned}
    \frac{\Gamma\left(\frac{n_1+n_2}{2}\right)}{\Gamma\left(n_1\right)\Gamma\left(n_2\right)}n_1^{\frac{n_1}{2}}n_2^{\frac{n_2}{2}}\frac{x^{\frac{n_1}{2}-1}}{(n_1x+n_2)^{\frac{n_1+n_2}{2}}},\quad x > 0\\
    0, \quad x \leq 0
  \end{aligned}
  \right.
  $$

## 2. 大数定律

> 即描述依概率趋于0的各定律

1. 切比雪夫不等式
   : 对任意变量$X$，若其方差存在，则$\forall\varepsilon>0$:$$P(\left|X-EX\right|\geq\varepsilon)\leq\frac{DX}{\varepsilon^2}$$
2. 伯努利大数定律
   : 设在n重伯努利实验中，成功的次数为$Y_n$，而在每次实验中成功概率为$p(0<p<1)$，则$\forall\varepsilon>0$:$$\lim\limits_{n\rarr\infin}P\left(\left|\frac{Y_n}{n}-p\right|\geq\varepsilon\right)=0$$
3. 切比雪夫大数定律
   : 设$X_1,\ldots,X_n$是相互独立的随机变量序列。若这n个随机变量的方差一致有界，则$\forall\varepsilon>0$:$$\lim\limits_{n\rarr\infin}P\left(\left|\frac{1}{n}\sum\limits^n_{i=1}(X_i-EX_i)\right|\geq \varepsilon\right)=0$$
4. 辛钦大数定律
   : 设$X_1,X_2\ldots,X_n,\ldots$是独立同分布的随机变量，且所有随机变量的数学期望$\mu=EX_1=EX_2=\ldots$，则$\forall\varepsilon>0$:$$\lim\limits_{n\rarr\infin}P\left(\left|\frac{1}{n}\sum\limits^n_{i=1}X_i-\mu\right|\geq \varepsilon\right)=0$$

## 3. 中心极限定理

1. *Kindeberg-Levy*中心极限定理
   : 设$X_1,X_2\ldots,X_n,\ldots$是独立同分布的随机变量,且$EX_i=\mu,DX_i=\sigma^2(i=1,2,\ldots)$,则对一切$x$，有:$$\lim\limits_{n\rarr\infin}P\left\{\frac{1}{\sqrt{n}\sigma}\sum\limits^n_{i=1}\left(X_i-\mu\right)\leq x\right\}=\int^x_{-\infin}\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,dt$$即渐进地服从$N(0,1^2)$
2. *De Moivre-Laplace*定理
   : 设在n重伯努利试验中，成功的次数为$Y_n$，而在每次试验中成功的概率为$p$，则对一切$x$有： $$\lim\limits_{n\rarr\infin}P\left(\frac{Y_n-np}{\sqrt{np(1-p)}}\leq x\right)=\int^x_{-\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,dt$$即渐进地服从$N(0,1^2)$

## 4. 统计量与抽样分布

1. 设$X_1,X_2\ldots,X_n,\ldots$为总体$N(\mu,\sigma^2)$的一个样本，则样本均值$\bar{X}$满足：$$\bar{X}\sim N(\mu,\frac{\sigma^2}{n})$$
2. 设$\bar{X}$是正态总体$N(\mu,\sigma^2)$的样本均值，则：$$\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1^2)$$
3. 设$X_1,X_2\ldots,X_n,\ldots$为总体$N(\mu,\sigma^2)$的一个样本，则样本方差$S^2$与样本均值$\bar{X}$相互独立，且$$\frac{n-1}{\sigma^2}S^2\sim\chi^2(n-1)\\$$
4. $$\frac{\bar{X}-\mu}{S/\sqrt{n}}\sim t(n-1)$$
5. 设$X_1,X_2\ldots,X_{n_1},\ldots$和$Y_1,Y_2,\ldots,Y_{n_2}$分别为总体$N(\mu_1,\sigma^2)$和$N(\mu_2,\sigma^2)$的两个样本，它们相互独立，则$$\frac{(\bar{X}-\mu_1)-(\bar{Y}-\mu_2)}{S_w/\sqrt{n_w}}\sim t(n_1+n_2-2)$$其中：$$S_w=\sqrt{\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}},\\ \qquad \\ n_w=\frac{1}{\frac{1}{n_1}+\frac{1}{n_2}}$$
6. $$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F(n_1-1,n_2-1)$$

## 5. 参数估计

### 5.1 点估计

#### 5.1.1 矩估计法

即将待求的未知参数用总体矩表示出来，然后用样本矩估计总体矩，比如：
估计总体方差$\sigma^2$:
$$\mu_1=EX\\\mu_2=EX^2=DX+(EX)^2=\sigma^2+\mu_1^2$$
故：
$$\hat{\sigma}^2=\mu_2-\mu_1^2=\frac{1}{n}\sum\limits_{i=1}^n(X_i-\bar{X})^2$$

#### 5.1.2 极大似然估计法

思想：我认为我在样本中观察到的现象就应该是总体原本应有的样貌，因此我在估计参数时也会倾向于让我所观察到的现象发生的概率达到最大。

设总体的概率密度为$f(x)$，其中含有未知参数$\theta_1,\theta_2,\ldots,\theta_m$，有$n$个样本值$x_1,x_2,\ldots,x_n$
那么我们先定义：

似然函数
: $$L:=L(\theta_1,\theta_2,\ldots,\theta_m)=\mathop{\Pi}\limits_{i=1}^nf(x_i,\theta_1,\theta_2,\ldots,\theta_m)$$

这样的函数是关于$\theta_1,\theta_2,\ldots,\theta_m$的多元函数，那么问题变转化为了求多元函数$L(\theta_1,\theta_2,\ldots,\theta_m)$的极大点$(\hat{\theta}_1,\hat{\theta}_2,\ldots,\hat{\theta}_m)$的问题。

一般处理方法是找到$L$或$\mathcal{ln}L$的驻点。

#### 5.1.3 评估估计值的优良性

1. 无偏性
   即含估计参数的统计量表达式的期望仍然是原统计量：$$E_\theta(\hat{\theta}(X_1,X_2,\ldots,X_n))=\theta$$
2. 有效性
   设$\hat{\theta}(X_1,X_2,\ldots,X_n)$与$\hat{\theta}'(X_1,X_2,\ldots,X_n)$均为$\theta$的无偏估计，若对于任意样本，有:$D_\theta(\hat{\theta}) \leq D_\theta(\hat{\theta}')$，则称$\hat{\theta}$较$\hat{\theta}'$有效。
3. 相合性
   若$\hat{\theta}_n$依概率收敛于被估计参数事实上的值，则称估计量$\{\hat{\theta}_n\}$是未知参数$\theta$的相合估计量。

### 5.2 区间估计

置信区间
: 对于未知参数$\theta$，如果有两个统计量$\hat{\theta_1},\hat{\theta_2}$对给定的$\alpha$有$$P(\hat{\theta_1}< \theta <\hat{\theta_2})=1-\alpha$$则称$(\hat{\theta_1},\hat{\theta_2})$为$\theta$的置信区间，$1-\alpha$为置信度。

> tip1: 由定义可知，置信区间并不具有唯一性
> tip2: “置信度”表示将置信区间视为随机变量时，置信区间内含有未知参数的真实值的概率。

至于估计时，就根据[*统计量与抽样分布*](#4-统计量与抽样分布)以及[*中心极限定理*](#3-中心极限定理)来对目标参数进行估计即可。
~~某种程度上，这些结论保证了“万物皆可正态分布”~~

## 6 假设检验

显著性水平
: 在假设检验中指定一个很小的正数$\alpha\ (\alpha\in(0,1))$，把概率不超过$\alpha$的小概率事件视为不可能事件，则将这样的一个数称为显著性水平。

**基本思想**：构造一个发生概率低于显著性水平的小概率事件A，然后依小概率原理作为拒绝假设的依据：即在当前假设下，若经过一次试验后，事件A出现了，那么便可以考虑拒绝这一假设。

假设检验中的错误
: 在假设检验中拒绝了事实上是真实的假设，我们称其为**第一类错误**；在假设检验中接受了事实上不真实的假设，我们称其为**第二类错误**。

> 待看：最优势问题

### 6.1 显著性检验
> [懒得打字.jpg](#422-参数假设检验)

### 6.2 非参数检验——$\mathbf{\chi^2}$拟合优度检验

用大白话来说，就是猜分布函数。

皮尔逊（Pearson）统计量
: 假设总体仅在k个互不相交的实数集$A_i,i=1,2,\ldots,k$中取值，且在我们所假设的分布中，落入实数集$A_i$的概率为$p_{i0}$；并用$n_i$来表示我们所抽取的样本容量为$n$的样本中落入实数集$A_i$的元素数，则我们计皮尔逊统计量为$$\chi^2:=\sum\limits_{i=1}^k\frac{(n_i-np_{i0})^2}{np_{i0}}$$

#### 6.2.1 离散非参数检验

我们所需检验的假设为：
$$H_0:F(x)=F_0(x)$$其中$F_0(x)$为一个已知的猜测
设总体$X$仅在k个互不相交的实数集$A_1,A_2,\ldots,A_k$中取值，并令$p_i=P(X\in A_i),i=1,2,\ldots,k$，同时在我们所假设的分布中，落入实数集$A_i$的概率为$p_{i0}$。则我们所需检测的假设$H_0$可化为等价命题：$$H_0':p_i=p_{i0}$$
那么利用皮尔逊变量在$n\rarr\infin$时服从$\chi^2(k-1)$的分布的性质（书中以“理论上已经证明”略过了这个性质的证明过程）,就可以得到这个假设在显著性水平为$\alpha$时的拒绝域：$\chi^2 \geq \chi^2_\alpha(k-1)$（其中$\chi^2_\alpha(k-1)$代表$\chi^2(k-1)$的上$\alpha$分位数）

#### 6.2.2 连续非参数检验

其实由于上面理论中只需要求总体$X$在$k$个不同的**实数集**中取值，因此我们只需要求我们的分布函数的定义域可被分割为有限个区间即可套用上述结论

当完全猜的出分布函数时：
我们所需检验的假设为：
$$H_0:F(x)=F_0(x),\quad-\infin<x<+\infin$$
则考虑将实数轴切成k个区间：
令$$-\infin<y_1<y_2<\ldots<y_{k-1}<+\infin$$
则
$$
A_1=(-\infin,y_1]\\
A_i=(y_{i-1}，y_i],i=2,3,\ldots,k-1\\
A_k=(y_{k-1},+\infin)
$$
然后利用$F_0(x)$计算出$p_{i0},i=1,2,\ldots,k$，再抽取样本，便可计算皮尔逊统计量了。由于理论相同，所以拒绝域同上。

当只能知道分布函数类型时：
我们所需检验的假设为：
$H_0:F(x)=F_0(x;\theta_1,\theta_2,\ldots,\theta_m),\quad -\infin<x<+\infin$
其中仅知道$F_0$的类型。
则考虑利用极大似然估计法将全局未知参数的点估计确定。然后就回到了上面的情况以及步骤。只不过注意：这样得到的皮尔逊统计量所服从的分布是$\chi^2(k-m-1)$

## 7 方差分析

研究问题：多个正态总体在方差相同的条件下数学期望是否相等的假设检验问题
即：设有$m$个相互独立的具有方差的正态变量$X_i\sim N(\mu_i,\sigma^2)(i=1,2,\ldots,m)$，检验假设：$H_0:\mu_1=\mu_2=\ldots=\mu_m$

试验的因素
: 我们称影响试验结果的客观对象为试验的因素；不同的对象称为相应因素的不同水平

在单因素试验中，仅考虑一个因素的多个不同的水平，因此我们称这种试验为**单因素试验**。

### 7.1 单因素方差分析

我们假设有$m$个水平$A_1,A_2,\ldots,A_m$，在每个水平$A_i$下，总体$X_i\sim N(\mu_i,\sigma^2)$，$x_{i1},x_{i2},\ldots,x_{in_i}$为总体$X_i$的容量为$n_i$的样本，则我们首先产生了以下概念：

单因素试验方差分析的数学模型
: $$x_{ij}=\mu_i+\varepsilon_{ij},\varepsilon_{ij}\sim N(0,\sigma^2);j=1,2,\ldots,n;i=1,2,\ldots,m$$

总平方和
: $$S:=\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}(x_{ij}-\bar{x})^2$$，其中$$\bar{x}=\frac{1}{n}\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}x_{ij}$$
> 用于初步衡量全局偏差$\varepsilon$

我们不妨记每个水平上的样本均值为$\bar{x}_{i*}$，即$$\bar{x}=\frac{1}{n_i}\sum\limits_{j=1}^{n_i}x_{ij}$$
则可以分解:
$$S=\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}(x_{ij}-\bar{x})^2=\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}(x_{ij}-\bar{x}_{i*}+\bar{x}_{i*}-\bar{x})^2\\=\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}(x_{ij}-\bar{x}_{i*})^2+\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}(\bar{x}_{i*}-\bar{x})^2\\=\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}(x_{ij}-\bar{x}_{i*})^2+\sum\limits_{i=1}^mn_i(\bar{x}_{i*}-\bar{x})^2$$
引出概念:

误差平方和
: $$S_e:=\sum\limits_{i=1}^m\sum\limits_{j=1}^{n_i}(x_{ij}-\bar{x}_{i*})^2$$（又称组内平方和）

组间平方和
: $$S_A:=\sum\limits_{i=1}^mn_i(\bar{x}_{i*}-\bar{x})^2$$

则有$S=S_e+S_A$
可以计算得：$$ES_e=(n-m)\sigma^2\\ ES_A=(m-1)\sigma^2+\sum\limits_{i=1}^mn_i(\mu_i-\mu_0)^2$$

效应
: 即某个总体的均值与各总体的均值之差，比如第$i$个总体的均值与各总体的均值之差$\alpha_i=\mu_i-\mu$为被称为第$i$个水平的效应。

于是我们考虑利用变量$$F:=\frac{S_A/(m-1)}{S_e/(n-m)}$$作为检验$H_0$的统计量。

***Theorem***
1. $$S_e/\sigma^2\sim \chi^2(n-m)$$
2. $S_A$与$S_e$相互独立，且当所有水平的期望一致时，$$S_A/\sigma^2\sim\chi^2(m-1)$$

则有$F\sim F(m-1,n-m)$,可得拒绝域为$F\geq F_\alpha(m-1,n-m)$
> 由于我们借助计算机进行计算，所以书上为了方便计算的部分暂且忽略。

于是有方差分析表：
| 方差来源 | 平方和 | 自由度 | 均方 | F值 |
| ------- | --- | --- | --- | --- |
| 因素 | $S_A$ | $m-1$ | $\bar{S}_A = \frac{S_A}{m-1}$ | $\bar{S}_A/\bar{S}_e$ |
| 误差 | $S_e$ | $n-m$ | $\bar{S}_e=\frac{S_e}{n-m}$ | 
| 总和 | $S=S_A+S_e$ | $n-1$ | | |

### 7.2 双因素方差分析

双因素试验方差分析的数学模型
: $$x_{ijk}=\mu+\alpha_j+\beta_i+\gamma_{ij}+\varepsilon_{ijk},\varepsilon_{ijk}\sim N(0,\sigma^2);j=1,2,\ldots,n;i=1,2,\ldots,m,k=1,2,\ldots,t$$,其中$\alpha_j$为$A_j$的效应，$\beta_i$为$B_i$的效应，$\gamma_{ij}$为$A_j$与$B_i$的交叉效应。


于是可以照葫芦画瓢地进行分解：
$$
S:=\sum\limits_{i=1}^m\sum\limits_{j=1}^n\sum\limits_{k=1}^t(x_{ijk}-\bar{x})^2\\
S=S_e+S_A+S_B+S_{AB}\\\quad\\
S_e=\sum\limits_{k=1}^t\sum\limits_{i=1}^m\sum\limits_{j=1}^n(x_{ijk}-\bar{x}_{ij*})^2\\
S_A=mt\sum\limits_{j=1}^n(\bar{x}_{*j*}-\bar{x})^2\\
S_B=nt\sum\limits_{i=1}^n(\bar{x}_{i**}-\bar{x})^2\\
S_{AB}=t\sum\limits_{i=1}^m\sum\limits_{j=1}^n(\bar{x}_{ij*}-\bar{x}_{i**}-\bar{x}_{*j*}+\bar{x})^2
$$
从而有：
$$
F_A=\frac{S_A/(n-1)}{S_e/[nm(t-1)]}\sim F(n-1,nm(t-1))\\
F_B=\frac{S_B/(m-1)}{S_e/[nm(t-1)]}\sim F(m-1,nm(t-1))\\
F_{AB}=\frac{S_{AB}/[(n-1)(m-1)]}{S_e/[nm(t-1)]}\sim F((n-1)(m-1),nm(t-1))
$$
如果不考虑交叉效应，则可以考虑将$t$设为1，并将$nm(t-1)$项换成$(n-1)(m-1)$，舍弃$S_{AB}$项

## 8 一元正态线性回归

回归函数
: 设$Y$是依赖于一般变量$x$的一个随机变量， 则我们称$\mu(x)=EY$为$Y$对$x$的回归函数。

### 8.1 一元正态线性回归的数学模型
设$Y$为可观测的随机变量，$x$为一般变量，它们之间存在以下关系：$$Y=a+bx+\varepsilon\\\varepsilon\sim N(0,\sigma^2)$$
其中未知参数$a,b,\sigma^2$不依赖于$x$，称$y=\mu(x)=a+bx$为随机变量$Y$对$x$的线性回归，称变量$x$为回归变量，变量$a,b$为回归系数。

设$x_1,x_2,\ldots,x_n$为变量$x$的任意$n$个不完全相同的值的序列，$y_1,y_2,\ldots,y_n$为随机变量$Y$的对应的$n$个观测值。那么我们可以由极大似然估计得到一元正态线性回归的数学模型中线性回归方程的各个参数。先令：
$$
\begin{aligned}
    l_{xx}:=\sum\limits_{i=1}^n(x_i-\bar{x})^2=\sum\limits_{i=1}^nx_i^2-n\bar{x}^2\\
    l_{xy}:=\sum\limits_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})=\sum\limits_{i=1}^nx_iy_i-n\bar{x}\bar{y}\\
    l_{yy}:=\sum\limits_{i=1}^n(y_i-\bar{y})^2=\sum\limits_{i=1}^ny_i^2-n\bar{y}^2
\end{aligned}
$$
则有
$$\hat{b}=\frac{l_{xy}}{l_{xx}}\\\hat{a}=\bar{y}-\hat{b}\bar{x}\\\hat{\sigma^2}=\frac{l_{yy}-\hat{b}l_{xy}}{n}$$
从而我们得到了**经验回归方程**$y=\hat{a}+\hat{b}x$
> 与最小二乘法所得系数在此模型下是一致的

## 8.2 无偏估计

首先，
$$
\begin{align*}
    E\hat{a}=a,\qquad E\hat{b}=b\\
    D\hat{a}=\sigma^2\left(\frac{1}{n}+\frac{\bar{x}^2}{l_{xx}}\right),\quad D\hat{b}=\frac{\sigma^2}{l_{xx}}
\end{align*}
$$
而$\hat{\sigma}^2$并非$\sigma^2$的无偏估计，因此我们有修正后的无偏估计：$$s^2:=\frac{n}{n-2}\hat{\sigma}^2$$

于是：
***Theorem 1***
1. $$\hat{b}\sim N\left(b,\frac{\sigma^2}{l_{xx}}\right)$$
2. $$\hat{a}\sim N\left(a,\sigma^2\left(\frac{1}{n}+\frac{\bar{x}^2}{l_{xx}}\right)\right)$$
3. $$\frac{(n-2)s^2}{\sigma^2}\sim\chi^2(n-2)$$
4. $\bar{y},\hat{b},s^2$三者相互独立

### 8.3 显著性检验

需检验的假设：$Y$与$x$存在线性关系
等价于：拒绝假设$H_0:b={0}$

> 可以很容易地发现，若接受$H_0$时我们所探究的问题就变成了单因素方差分析中所探究的问题。所以我们也沿用单因素方差分析中分析显著性的思路。

令$\hat{y}_i=\hat{a}+\hat{b}x_i,i=1,2,\ldots,n$,则我们称$$Q:=\sum\limits_{i=1}^n(y_i-\hat{y}_i)^2$$为**残差平方和**，$$U:=\sum\limits_{i=1}^n(\hat{y}_i-\bar{y})^2$$为**回归平方和**
于是有$l_{yy}=Q+U$。

显然，$Q=n\hat{\sigma}^2$，$U=\hat{b}^2l_{xx}$,于是：$$E\left(\frac{Q}{n-2}\right)=\sigma^2\\ EU=\sigma^2+b^2l_{xx}$$

#### $\mathbf{F}$检验法

根据**Theorem1**，我们可以得到：$$F=\frac{U}{Q/(n-2)}\sim F(1,n-2)$$，所以对于给定显著性水平$\alpha$，拒绝域为$F\ge F_\alpha(1,n-2)$。若假设得到拒绝，则我们的回归方程式是**显著的**,反之不显著。

#### $\mathbf{r}$检验法

我们令$$r:=\frac{l_{xy}}{\sqrt{l_{xx}l_{yy}}}\\\rArr\quad Q=l_{yy}(1-r^2)=\frac{U}{l_{yy}}$$可见，$r$越接近1，$Y$与$x$的线性关系越密切。
我们又发现：$F=\frac{(n-2)r^2}{1-r^2}$，于是可以由$F$检验法求出$r$的拒绝域。

### 8.4 预测与控制

#### 预测

可以证明，对任意固定的$x_0$，统计量$$t=\frac{y_0-\hat{y}_0}{s\sqrt{1+\frac{1}{n}+\frac{(x_0-\bar{x})^2}{l_{xx}}}}\sim t(n-2)$$
其中$s=\sqrt{Q/(n-2)}$被称为**剩余标准差**

则由此可以计算预测值$\hat{y}$的置信区间。

#### 控制

即预测的反问题：如果我指定了一个精度，那么一般变量$x$在哪个范围内才可以满足这样的精度

可以考虑借助反函数来求解，也可以简化：
$$
\text{when} \ n\rarr +\infin \ \text{and} \ x_0\rarr \bar{x}\\
s\sqrt{1+\frac{1}{n}+\frac{(x_0-\bar{x})^2}{l_{xx}}}\rarr s\\
$$
所以置信区间变化为：
$$U(\hat{y}_0,t_{\frac{\alpha}{2}}(n-2)s\sqrt{1+\frac{1}{n}+\frac{(x_0-\bar{x})^2}{l_{xx}}})\\\rarr U(\hat{y}_0,u_{\frac{\alpha}{2}}s)$$
其中$u_{\frac{\alpha}{2}}$表示标准正态分布的上$\frac{\alpha}{2}$分位数
显然线性函数的反函数更加简单易算

### 8.5 一元非线性回归

如果$\mu(x)$是非线性的但是只含有两个未知参数$a,b$时，可以考虑将$\mu(x)$整理为$g(y)=a+bh(x)$的关系，那么在换元后就可以进行类似一元线性回归分析的步骤。


