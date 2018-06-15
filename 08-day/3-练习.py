class Car(object):
	def __init__(self,name):
		self.name = name
	def run(self):
		print('%s在飞奔'%self.name)
class Dazhong(Car):
	def run(self):
		return '大众在飞奔'
class Bmw(Car):
	def run(self):
		return '宝马在飞奔'
class Benchi(Car):
	def run(self):
		return '奔驰在飞奔'

class People(object):
	def __init__(self,name):
		self.name = name
	def fangfa(self,car):
		print('%s在开着%s'%(self.name,car.run()))

car = Car('大众')
car.run()
dazhong = Dazhong('大众')
baoma = Bmw('宝马')
benchi = Benchi('奔驰')
ren = People('晓俊')
ren.fangfa(benchi)