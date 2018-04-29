a = 101
print(a)

def someFun():
	global a
	#print(a)
	a = 'Changing global variable'
	print(a)


someFun()
print(a)
