#输入输出 input()  print()
#小练习  银行卡ATM取款 总金额10000
total=10000
password=input("请输入银行卡密码:")
print(f"密码正确,{password}")

num=input("请输入您的取款金额:")
print(f"取款后银行卡的余额为:{total-int(num)}")