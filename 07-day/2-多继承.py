class Donkey(object):
	#驴类
	def manzou(self):
		print('走得慢------')
	def jiao(self):
		print('驴在欢叫---')
class Horse(object):
	#马类
	def naili(self):
		print('马力足，持久强------')
	def jiao(self):
		print('马在嘶鸣----')
class Mule(Donkey,Horse):
	#骡子
	pass

骡子一号 = Mule()
骡子一号.manzou()
骡子一号.naili()
骡子一号.jiao()