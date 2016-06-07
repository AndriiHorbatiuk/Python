import sys
a = list(sys.argv[1])
levo = 0
pravo = 0
i = ''
for i in a:
	if i == "(":
		levo = levo + 1
	else:
		pravo = pravo + 1
if levo == pravo:
	print("YES")
else:
	print("NO")