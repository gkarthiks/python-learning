name = "GKarthikeyan"
print(name[0])
print(name[1:12])

print((name+'\t')*2)

print("a" in name)

print(r"This is to print \n")


a = "String"
b = 10

print'%s is the string and  %d is the number' % (a,b)

print(name[:7])

oldStr = "Old String"
newStr = oldStr.replace("Old", "New")
print oldStr
print newStr
oldStr = oldStr.replace("Old", "New")
print(oldStr)

loweCase = "gkarthikeyan"
print(loweCase.upper())
print(loweCase.capitalize())


print(":".join("Python".upper()))

string="12345"		
print(''.join(reversed(string)))

word="this is split example"
print(word.split(' '))