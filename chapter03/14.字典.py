#字段 -- key不能重复(如果重复,后面的值,会覆盖前面的值) key必须是不可变类型(str,int,float,tuple)
dict1={"a":100,"b":99,"c":98,"d":97}
print(dict1)
print(type(dict1))

dict2={0:650,1.5:222,(1,2):854,("a","b"):111}
print(dict2)

#访问
print(dict1["b"])
dict1["b"]=101
print(dict1)

#字典的常用操作
dict1={"王林":670,"李慕婉":608,"许立国":580}
print(dict1)

dict1["淳哥"]=750
print(dict1)

dict1["王林"]=567

print(dict1["淳哥"])#根据key值获取value
print(dict1.get("淳哥"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

#删除
score=dict1.pop("许立国")
print(score)
print(dict1)

del dict1["李慕婉"]
print(dict1)
