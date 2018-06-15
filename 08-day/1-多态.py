class Duck(object):
	def walk(self):
		print('小黄人在摇摆着行走---')
	def swim(self):
		print('小黄人在湖水中游泳---')
class People(object):
	def walk(self):
		print('小黄鸭-在摇摆着行走---')
	def swim(self):
		print('小黄鸭-在湖水中游泳---')

def Func(obj):#同样的一个函数，定义的时候，不知道结果是什么
	obj.walk()#执行的时候，才会表现出来太的具体形态结果
	obj.swim()

#好处：1.代码灵活；2.减少代码 
duck = Duck()
p01 = People()
Func(p01)