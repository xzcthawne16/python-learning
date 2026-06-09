# # 字面量的写法
print(100)
print(3.14)
print(True)
print(False)
print("Hello Python")
print("---------------")
print(None)


print(True + 1)   #True值是1
print(False - 1) # False值是0


# # 变量   一般情况下,一个变量名(容器)只定义一个数据
num=1314.4
print(num)
print(num + 2)
print(num - 2)
num=1314.4
print(num)
num="theshy"
print(num)

#
base,incr=20.7,50 #定义变量的时候可以放在一起定义,但是要用 "," 隔开
print("未来第一个月的播放量:",base + incr)
print("未来第二个月的播放量:",base + incr + incr)  #python官方中是" "+" ",加号要用空格隔开
#
#
# #标识符
# 标识符的命名规则
# 1.只能包含数字,字母,下划线
# 2.不能以数字开头
# 3.不能包含关键字 比如True False  if else elif for while and or等
# 4.标识符严格区分大小写,大小写不同,则代表着不同的变量
# 5.多个部分用下划线连接,比如my_age my_name
# 6.英文字母要全部小写
#
#
# #小练习 交换变量的值
a,b=100,200
print("交换前a的值是:",a)
print("交换前b的值是:",b)
temp=None
temp=a
a=b
b=temp
print("交换后a的值是:",a)
print("交换后b的值是:",b)


# 小练习 a=100 b=200 c=300 将abc的值分别赋值给cab
a,b,c,temp_1=100,200,300,None
print("交换前a的值是:",a)
print("交换前b的值是:",b)
print("交换前c的值是:",c)
temp_1=c
c=a
a=b
b=temp_1
print("交换后a的值是:",a)
print("交换后b的值是:",b)
print("交换后c的值是:",c)

