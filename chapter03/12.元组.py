# 元祖基本操作 tuple 元素可以重复,有序,但是不可以修改
t1=(1,2,3,4,5,6,7,8,9)

print(t1)
print(type(t1))

#索引访问
print(t1[0])
print(t1[-1])
#切片
print(t1[0:5:1])

#统计元素的个数
print(t1.count(1))

#index() 获取元素的索引
print(t1.index(4))

#元组中定义一个元素的时候需要在最后加一个,
t3=(1,)
print(t3)
print(type(t3))

t4=(1)
print(t4)
print(type(t4))

#组包和解包
#组包
t1=(1,2,3,4,5,6,7,8,9)
t2=10,9,8,7,6,5,4,3,2,1

print(t1)
print(t2)

#解包
a,b,c,d,e,f,g,h,i=t1
print(a,b,c,d,e,f,g,h,i)

#*扩展解包 *解包所有剩余元素
first,second,*other,last=t1
print(first,second)
print(other)
print(last)


#小练习
students=(
    ("001","A",85,92,78),
    ("002","B",92,88,95),
    ("003","C",78,85,82),
    ("004","D",88,79,91),
    ("005","E",95,96,89),
    ("006","F",76,82,77),
    ("007","G",89,91,94),
    ("008","H",75,69,82),
    ("009","I",86,89,98),
    ("010","J",66,69,72)

)
#计算每个学生的总分,各科平均分然后一并输出出来
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分\t\t")
# for s in students:
#     total=s[2]+s[3]+s[4]
#     avg=total/3
#     print(f"{s[0]}\t\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}") #:.1f保留小数点后一位

#第二种方法 解包
for id,name,chinese,math,english in students:
    total=chinese+math+english
    avg=total/3
    print(f"{id}\t\t{name}\t\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}")


#统计各科成绩的最低分 最高分 平均分 并输出
chinese_scores=[s[2] for s in students]
math_scores=[s[3] for s in students]
english_scores=[s[4] for s in students]
print(f"语文最低分:{min(chinese_scores)},最高分:{max(chinese_scores)},平均分:{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分:{min(math_scores)},最高分:{max(math_scores)},平均分:{sum(math_scores)/len(math_scores)}")
print(f"英语最低分:{min(english_scores)},最高分:{max(english_scores)},平均分:{sum(english_scores)/len(english_scores)}")

#查找成绩平均分大于90的学生,并输出
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    if avg >90:
        print(f"学号为{s[0]},姓名为{s[1]}是优秀学生")
