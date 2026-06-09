#if 判断, 同样的缩进就代表是执行同一个if判断 ,if 判断 :
score=690
if score>=690:
    print("恭喜你,考上了清华大学")
    print("也恭喜你即将进入精彩的大学生活")
print("-------------")

# 小练习1 实现B站的登录功能,简单的账号和密码验证
correct_account='1'
correct_password='123456'  #因为input接收的是字符串,所以在一开始定义正确账号,密码的时候需要将其定义成字符串类型,不然就是int和字符串比较,永远不等

account=input("请输入你的账号:")
password=input("请输入你的密码:")

if account==correct_account and password==correct_password:
    print("账号密码正确,登录成功")

if account!=correct_account or password!=correct_password:
    print("账号密码错误,登录失败")

# 小练习1(用if else完成) 实现B站的登录功能,简单的账号和密码验证
correct_account='1'
correct_password='123456'  #因为input接收的是字符串,所以在一开始定义正确账号,密码的时候需要将其定义成字符串类型,不然就是int和字符串比较,永远不等

account=input("请输入你的账号:")
password=input("请输入你的密码:")

if account==correct_account and password==correct_password:
    print("账号密码正确,登录成功")

else:
    print("账号密码错误,登录失败")

#小练习 根据用户输入的年份,判断这一年是闰年还是平年 (非整百年份,且能被4整除的年份是闰年;整百年份必须被400整除才是闰年)
year=int(input("请输入年份:"))
if (year%100 !=0 and year %4 ==0)or (year%400==0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")


#elif小练习 根据用户输入的数,判断数字是正数,还是负数,还是0
num=int(input("请输入数字:"))

if num >0:
    print(f"{num}是一个正数")
elif num <0:
    print(f"{num}是一个负数")
else:
    print(f"{num}是0")
