# #常见的数据类型
# int float str bool NoneType(就是None,是空值)
#
num="theshy666"
print(type(num))

num=12345
print(type(num))


num=5.0
print(num)
print(isinstance(num,int))
print(isinstance(num,bool))
print(isinstance(num,float))


#字符串的定义 "" '' |  """  """这里面的所有都会输出,包括空格"""

msg='It\'s very good' #\转义字符  \n换行 \t首行缩进
print(msg)

msg="It's very good"
print(msg)

msg="""

准备起飞
"""
print(msg)



#字符串的拼接
s1 = "人生苦短" "我用python" ",OK"
print(s1)

msg1="人生苦短"
msg2="我用python"
print("大飞说:"+msg1+","+msg2)


msg1="我是淳哥"
age=18
msg3="我是本质天才"
msg4="我即将起飞"
print("大家好"+","+msg1+","+"我今年"+str(age)+","+msg3+","+msg4+".")
# 加号只能拼接字符串,其他类型需要转化为字符串才能拼接


# #字符串的格式化 方式一 %s 占位符
name="淳哥"
age=18
pro="通信工程"
hobby="LOL&羽毛球"
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好是%s." %(name,age,pro,hobby))

# 方式二 f"{}"
name="淳哥"
age=18
pro="通信工程"
hobby="LOL&羽毛球"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好是{hobby}.")

