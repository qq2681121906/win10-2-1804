class bakepig():
	def __init__(self):
		self.time = 0
		self.state = ''
		self.seasoning = []
	def bake(self,time):
		self.time+=time
		if self.time >= 0 and self.time < 3:
			self.state = '皮都没烧透'
		elif self.time >= 3 and self.time < 6:
			self.state = '半生不熟'
		elif self.time >= 6 and self.time < 10:
			self.state = '熟了,能吃了'
		elif self.time >= 10:
			self.state = '烤糊了'
	def relish(self):
		relish = input('加作料')
		if relish != '':
			self.seasoning.append(relish)
		else:
			pass
	def __str__(self):
		return self.state+str(self.seasoning)
kz = bakepig()
while True:
	times = int(input('考多久'))
	kz.bake(times)
	kz.relish()
	print(kz)
	if kz.time > 15:
		print('烤化了!!!!!!!!!!!!!!!!!!!')
		break