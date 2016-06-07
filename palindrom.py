import sys
a = list(sys.argv[1].lower())
b = a[::-1]
a = ''.join(a)
b = ''.join(b)
a = a.replace(" ","")
b = b.replace(" ","")
if a == b:
	print("YES")
else:
	print("NO")