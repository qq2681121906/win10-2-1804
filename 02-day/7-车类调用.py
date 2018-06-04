class Car():
	def __init__(self,wheelNum,color):
		self.wheelNum = wheelNum
		self.color = color
	def pao(self):
		print('%s在跑,%d个轮子在转动------'%(self.name,self.wheelNum))
	def jiao(self):
		print('%s再叫,'%self.name)
	def zhuiwei(self):
		print('%s在追尾'%self.name)
car = Car(4,'red')
car.name = '宝马'
car.pao()
car.jiao()
car.zhuiwei()
print('车的颜色为:%s'%car.color)
print('车的轮子数量为:%s'%car.wheelNum)
print('-----------------------')
car = Car(3,'blue')
car.name = '奥迪'
car.pao()
car.jiao()
car.zhuiwei()
print('车的颜色为:%s'%car.color)
print('车的轮子数量为:%s'%car.wheelNum)