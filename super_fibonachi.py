def super_fibonacci(n, m):
	fibo = list(0, 1, 1, 2)
	number = 
	a_list = list(str(a))
	b_list = list(str(b))
	used_list = list()
	number = 0
	for i in range(0,(len(b_list))):
		if b_list[i] in a_list and not b_list[i] in used_list:
			number += 1
			used_list.insert((len(used_list)+1), b_list[i])
	return number
text = counter(2, 3)
print text