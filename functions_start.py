import sys

def is_zero(x):
	if x == 0:
		return True
	return False

x = int(sys.argv[1])

if bool(is_zero(x)) == True:
	print 'Upsi'
else:
	print float(15.0 / x)