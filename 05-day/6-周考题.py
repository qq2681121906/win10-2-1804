class Tool(object):
	def sushu(self):
		for i in range(100,200):
			flag = True
			for b in range(2,i):
				if i%b == 0:
					flag = False
					break
			if flag:
				print(i)
t = Tool()
t.sushu()