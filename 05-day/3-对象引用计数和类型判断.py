import sys
class People:
	def __init__(self,name,salary):
		self.__name = name
		self.salary = salary
class Worder:
	def __init__(self,name,salary):
		self.__name = name
		self.salary = salary

xiaohua01 = People('小花01',5000)
xiaohua02 = xiaohua01
xiaohua03 = xiaohua01
print(sys.getrefcount(xiaohua01))
print(isinstance(xiaohua03,People))