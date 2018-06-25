# 迭代器01 第一种类型 generator 
L = [ x*2 for x in range(5)]
print(L)
L = ( x*2 for x in range(5))
print(L)
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))  # StopIteration
for i in L:
	print(i)
