class People:
	def __init__(self,name,height,weight):
		self.name = name
		self.height = height
		self.weight = weight

	def jump(self):
		print('%s跳起来了------'%self.name)
	def run(self):
		print('%s跑起来------'%self.name)
	def zhiquan(self):
		print('%S直拳------'%self.name)
	def tang(self):
		print('%s躺下开始装死------'%self.name)

chengguohan = People('程国汉','2.50米',250)
chengguohan.jump()
chengguohan.run('程国汉')
chengguohan.zhiquan('程国汉')
chengguohan.tang('程国汉')

caozhijing = People('草薙京','1.80米',160)
caozhijing.jump()
caozhijing.run('草薙京')
caozhijing.zhiquan('草薙京')
caozhijing.tang('草薙京')