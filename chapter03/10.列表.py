#列表
#列表名=[元素1,元素2,元素3],可以存放不同类型的元素、可重复、有序且元素可修改
#列表的索引 正向0开始,反向-1开始
#列表的操作  查看:list[下标]  修改 list[下标]='A' 删除 del list[下标]
s_list=[1,2,3,4,5,6]
print(s_list[1])
print(s_list[-5])
s_list[3]='A'
print(s_list[3])
del s_list[5]
for i in s_list:
    print(i,end='')
from traceback import print_stack

#切片 s[开始索引:结束索引:步长] 开闭后开,不包含结束索引,可以省略开始索引和结束索引和步长,默认开头和结尾,步长默认为1
#s[start:end:step]
s=[1,2,3,4,5,6,7,8,9,10,11,12]

print(s[0:5:1])
print(s[:5:1])
print(s[0::1])
print(s[::])
print(s[0:-2:2])


#列表的常见方法
s=[1,2,3,4,5,6,7,8,9,10,11]
s.append(12)
print(s)

s.insert(2,0)  #在index前插入
print(s)

s.remove(9)
print(s)

e=s.pop(1)
print(e)

e=s.pop()  #默认删除最后一个元素,并且pop有返回值
print(e)

s.sort()
print(s)

s.reverse()
print(s)

#小练习 将用户输入的10个数字,存储到一个列表之中,并将列表中的数字进行排序,输出最小的值,最大值和平均值
num_list=[]
for i in range(10):
    num=int(input("请输入一个有效的数字:"))
    num_list.append(num)
print("数字列表为:",num_list)

num_list.sort()
print("排序后的数字列表为:",num_list)

print(f"数字列表中的最小值是{num_list[0]}")
print(f"数字列表中的最大值是{num_list[-1]}")
print(f"数字列表中的平均值是{sum(num_list)/len(num_list)}")


#小练习 合并两个列表中的元素,并对合并的结果进行去重处理,并且排序
num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]

# 合并列表
for num in num_list2:
    num_list1.append(num)

# 去除重复记录
new_list=[]

for num in num_list1:
    if num not in new_list:
        new_list.append(num)
new_list.sort()
print("合并后表num_list1为:",num_list1)
print("去重且排序后表new_list为:",new_list)

#小练习简化版 解包 合并两个列表中的元素,并对合并的结果进行去重处理,并且排序
num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]

# #合并列表
#解包:将列表这一类容器解开成一个一个独立的元素
#组包:将多个值合并到一个容器
num_list=[*num_list1,*num_list2]
# num_list=num_list1+num_list2  可以直接加
#去除重复记录
new_list=[]

for num in num_list:
    if num not in new_list:
        new_list.append(num)
new_list.sort()
print("合并后表num_list1为:",num_list)
print("去重且排序后表new_list为:",new_list)


# #小练习 生成1-20的平方列表
num_list1=[]
for i in range(1,21):
    num_list1.append(i**2)

print(num_list1)

#小练习 生成1-20的平方列表的简化版
#推导式的简化  语法格式:[要插入的值 for i in 序列/列表]
num_list2=[i**2 for i in range(1,21)]
print(num_list2)


#小练习 从一个数字列表中提取所有偶数,并计算其平方,组成一个新的列表
#语法格式:[要插入的值 for i in 序列/列表 if 条件]
num_list1=[1,2,3,4,5,6,7,8,9,10]
new_list=[i**2 for i in num_list1 if i%2==0]
print(new_list)

