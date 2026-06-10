#字符串的常见方法
# s="    Hello-Python-Hello-World     "
#
# #find() 查找制定字符串中第一次出现的索引位置
# index=s.find("-")
# print(index)
# #count() 统计子字符串在指定字符串中出现的次数
# num=s.count("o")
# print(num)
# #upper() 转为大写
# s1=s.upper()
# print(s1)
# #lower()转为小写
# s2=s.lower()
# print(s2)
# #split()将字符串按照指定字符串切割-列表
# s3=s.split("-")
# print(s3)
# #strip()去除字符串两端的空格
# s4=s.strip()
# print(s4)
#
# print("------------")
# print(s) #对于字符串的常见操作,不会改变原来的字符串



#邮箱格式验证:用户输入邮箱,验证邮箱格式是否正确(包含一个@和至少一个.)
#第一方法
mail=input("请输入你的邮箱号:")
if mail.count("@")==1 and mail.count(".")>=1:
    print(f"{mail}邮箱格式正确")
else:
    print(f"{mail}邮箱格式错误")

#第二方法   in 返回的是bool值
mail=input("请输入你的邮箱号:")
if mail.count("@")==1 and "." in mail:
    print(f"{mail}邮箱格式正确")
else:
    print123(f"{mail}邮箱格式错误")