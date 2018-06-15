class GirlFriend(object):
	__girl = None
	__only_you = False
	def __init__(self,name):
		if self.__only_you == False:
			self.name = name
			self.__only_you = True
	def __new__(cls,*args):
		if cls.__girl == None:
			cls.__girl = object.__new__(cls)
		return cls.__girl	

c1 = GirlFriend('冯宝宝')
print(c1.name)
c2 = GirlFriend('王震球')
print(c2.name)