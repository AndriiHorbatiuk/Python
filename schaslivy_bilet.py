import sys
a = list(sys.argv[1])
b = list(sys.argv[2])
# Dobavlyaem nuli v nachalo pervomu chislu
i = 0
if len(a)<6:
	while len(a)<6:
		a.insert(i, 0)
		i = i +1
# Dobavlyaem nuli v nachalo vtoromu chislu
i = 0
if len(b)<6:
	while len(b)<6:
		b.insert(i, 0)
		i = i +1
# Delaem diapazon
achyslo = int(''.join(str(i) for i in a))
bchyslo = int(''.join(str(i) for i in b))
# Uznaem minimum i maximum
if achyslo < bchyslo:
	minimum = achyslo
	maximum = bchyslo
else:
	minimum = bchyslo
	maximum = achyslo
# Delaem cykl po proschetu schastlivyh biletov
schaslivyh = 0
i = 0
for count in range (minimum,maximum + 1):
	minimum_list = [int(x) for x in str(minimum)]
	if len(minimum_list)<6:
		while len(minimum_list)<6:
			minimum_list.insert(i, 0)
			z = i + 1
# Proverjaem na schastlivost
	if int(minimum_list[0]) + int(minimum_list[1]) + int(minimum_list[2]) == int(minimum_list[-1]) + int(minimum_list[-2]) + int(minimum_list[-3]):
		schaslivyh += 1
	minimum += 1
print schaslivyh