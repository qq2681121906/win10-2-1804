def test(out):
	def test_in(num_in):
		print('里面的内容是:%d'% num_in)
		return num_in + out
	return test_in

#test_in = test(1)
#test_in(2)
n = test(1)(2)
print(n)