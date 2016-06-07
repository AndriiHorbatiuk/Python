import sys
a = list(sys.argv[1])
a = ''.join(a)
a = a.split()
b = a[::-1]
b = ' '.join(b)
print b