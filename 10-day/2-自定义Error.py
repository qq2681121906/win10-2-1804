class MyError(Exception):
	def __init__(self,str_error,acc):
		self.name = str_error
		
	def get_acc()：
		acc = input('请输入账号')
		if len(acc) < 6:
			raise MyError('账号小于6位不符合要求')
	def get_pwd():
		pwd = input('请输入密码:')
		if len(pwd) < 6:
			raise MyError('密码小于6位不符合要求')
	if len(acc) == 6 and len(pwd) == 6:
		print('登录成功')	
try:
	get_pwd()
	get_acc()
except Exception as re:
	print('遇到了异常，内容是%s'%re)
