class House:
	def __init__(self,area,addr):
		self.area = area
		self.addr = addr
		self.items = []

	def __str__(self):
		return '新房子的大小是%d,地址位于:%s,其中包含的家具有:%s'%(self.area,self.addr,str(self.items))
	
	def add_items(self,item):
		if int(self.area) > int(item.area):
			self.area -= item.area
			self.items.append(item.name)
		else:
			print('家具太大了,我家小,容纳不下')
class Bed:
	def __init__(self,area,name):
		self.area = area
		self.name = name
	def __str__(self):
		return '%s已经购买好了,他的大小是%d'%(self.name,self.area)

house01 = House('200平米','前门北大街01')
print(house01)

baby_bed = Bed('100cm','婴儿床')
print(baby_bed)

house01.add_items(baby_bed)
print(house01)