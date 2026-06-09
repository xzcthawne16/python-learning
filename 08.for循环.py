#for循环:遍历输入的字符串

msg=input("请输入需要遍历的字符串:")

for s in msg:
    print(f"元素:{s}")
else:
    print


# 小练习1 计算1-100之间所有奇数之和
# 涉及知识点range语句  range(end)从0到end结束的数字序列,不包含range
# range(start,end)获取一个从start开始,到end结束的数字序列,不包含range
#range(start,end,step)从start开始,到end结束的数字序列,间隔就是步长,不包含range
total=0
for n in range(1,101):
    if n %2 ==1:
        total+=n
print("1-100之间的奇数累加之和:",total)

#简化版
total=0
for n in range(1,101,2):
    total+=n
print("1-100之间的奇数累加之和:",total)

#小练习2 计算100-500之间所有3的倍数的数字之和
total=0
for n in range(100,501):
    if n%3==0:
        total+=n
print("100-500之间所有3的倍数的数字之和是:",total)

#同理简化版本
total=0
for n in range(102,501,3):
        total+=n
print("100-500之间所有3的倍数的数字之和是:",total)


#for循环的嵌套
#小练习1 输出m*n的矩阵*
m=int(input("请输入长方形的长度:"))
n=int(input("请输入长方形的宽度:"))

for i in range(n):
    for j in range(m):
        print("*",end=" ") #print语句自带换行,所以用end=" "来取消换行
    print() #print()自带换行

#小练习2 输出99乘法表
m=int(input("请输入行数:"))
n=int(input("请输入列数:"))

for i in range(1,n+1):
    for j in range(1,i+1): #第一行就出一个 第二个就出2个
            print(f"{j}*{i}={i*j}",end="\t")
    print()