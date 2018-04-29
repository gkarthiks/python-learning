a = 5.0
print(a)

def someFunction():
	a = 'This is a local scope variable'
	print(a)

someFunction()
print('Now printing global scope:'+str(a))