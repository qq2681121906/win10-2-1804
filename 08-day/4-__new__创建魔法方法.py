class Car(object):
	def __init__(self,name):
		print('---__init__方法被调用---')
	def __del__(self):
		print('---__del__方法被调用---')
	def __new__(cls,*k,*kv):
		print('---__new__方法被调用---')

car = Car('大众')