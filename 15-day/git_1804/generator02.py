# generator02 
# 参考：http://python.jobbole.com/84527/


# def container(start, end):
# 	while start < end:
# 		print (start)
# 		start += 1
from inspect import isgeneratorfunction 
def container(start, end):
    while start < end:
        yield start  # 用于 创建 生成器generator
        start += 1
c = container(0, 59999999999999999999999999999)

print( isgeneratorfunction(container))
print(type(c))
print(c)  #  0，1，2，3，4
print(next(c))  # 01,2
# for i in c:
#     print(i)  #StopIteration