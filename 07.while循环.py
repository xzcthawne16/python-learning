#while
i=0
while i <3:
    print("准备起飞")
    i +=1
else:
    print("循环正常结束")

#小练习案例 计算1-1000之间所有偶数的累加纸之和
total=0
i=1

while i<=100:
    if i%2 ==0:
        total+=i
    i+=1
print(f"1-100之间的偶数的累加纸盒:{total}")