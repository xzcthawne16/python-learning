#集合 无序(所以不可以用索引查询) 无重复 可修改
#常见方法
#add() 添加元素
s1={1,2,3,4,5,6,7,8,9}
print(s1)

s1.add(10)
print(s1)

#remove() 移除集合中的指定元素,如果指定元素不存会报错
s1.remove(8)
print(s1)

#pop() 随机删除集合中的元素并返回
e=s1.pop()
print(e)
print(s1)

#clear() 清空集合
s1.clear()
print(s1)

s2={"a","b","c","d","e","x","y"}
s3={"c","e","y","z"}
#difference() 求两个集合的差集(存在于第一个集合,但是不存在于第二个集合)
print(s2.difference(s3))
print(s3.difference(s2))

#union() 求两个集合的并集
print(s2.union(s3))
print(s3.union(s2))

#intersection():求两个集合的交集
print(s2.intersection(s3))
print(s3.intersection(s2))
