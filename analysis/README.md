# Analysis Part

Here is the test for the branch

The program in this part will be stored in this branch

## Data Preparation
The generated raw data is stored in 'info.csv', the code is in 'random_gen.py'. You can change the path and parameters in the code, it will automatically output a csv.

The raw data include: capacity(evaluated by the # of chips), factory machine type, location, simulated occupation status, naive operation time of each operation (no difference between factories, maybe assigned later). 

## What is analysis.py?
<del>懒得写英文了</del>

### 两个常数


```python
SIMULATION_RANGE = 10
SIMULATION_TIMES = 1000
```

simulation 会取第 x 个能用的位置，$x \in [1, SIMULATION_RANGE]$

SIMULATION_TIMES 是模拟的次数


### 函数

```python
allocate_package (package)
```

输入一个 package ，返回一个 sorted list 叫做 time_distribution，该 list 由每次模拟后 package 的完成时间组成

（其实这个函数我实现了输入顾客选择的时间，然后返回用户的方案所需要的完成时间在 sorted list 里比多少百分比的模拟完成时间更快，返回是一个小数，把那个 return time_distribution 删掉就可以切换成这种模式）


``` python
insert_time (list, x, y)
delete_time (list, x, y)
```
在 list 里插入/删除 tuple(x, y) ，并保持原 list 操作后有序，这俩是用来方便维护 process_list 

### 后话

或许可以去根据 time_distribution 的返回值去画个图？<del>还能用来水report</del>

以及，csv 文件里输出的 list 是带引号的 string 类型，pandas 输出的时候有什么办法让它不带引号吗，不然在 analysis.py 里还要去写一个 eval(str(oplist)) 来读入 list。<del>虽然也能解决这个问题但是好蠢</del>