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

def bisha(item):
	item.run()
	item.jump()
	item.tang()
	item.zhiquan()
print(item87)