Dict = {'Karthik':29, 'Karthik':'Good boy', 'Keyan':28, 'abc':0, 'Abc':'this is different key', 'xyz':11}

print(Dict)
print(Dict.items())
print(Dict['Keyan'])

copiedDict = Dict.copy();
print(copiedDict)


copiedDict.update({'a':111})
print(copiedDict)

#copiedDict.add({'b':111}, {'c':111}, {'d':111} )
#print(copiedDict)


for keys in Dict.keys():
	print Dict[keys]

for key in copiedDict.keys():
	print(copiedDict[key])
	print('#')


for values in copiedDict.values():
	print(values)

sortedDict = copiedDict.keys();
sortedDict.sort()

print sortedDict

for s in sortedDict:
	print('Key: '+s+' Value: '+str(copiedDict[s]))


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
tuple1 = (50,)
print "variable Type: %s" %type (tuple1)

dict1 = {'a':1000, 'b':2000}
dict2 = {'a':1000, 'b':2000}
print(cmp(dict1, dict2))

print str(copiedDict)

smallListVal = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j']
bigListVal = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J']
dictList = {'smallAlpha': smallListVal, 'bigAlpha': bigListVal}

print dictList