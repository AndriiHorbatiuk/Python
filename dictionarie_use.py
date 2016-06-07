def count_holes(n):
	dictionarie = {0:1, 4:1, 6:1, 8:2, 9:1, 1:0, 2:0, 3:0, 5:0, 7:0}
	nuli = 0
	n_list_zero = [0]
	if n < 0:
		n_list = list(str(-n))
	elif n >= 0:
		n_list = list(str(n))
	n = unicode(n)
	if isinstance(n,str) and n.isnumeric() == False:
		nuli = 'ERROR'
	if '.' in n_list:
		nuli = 'ERROR'
	else:
		n_list = [int(i) for i in n_list]
		if n_list[0] == 0 and len(n_list) > 1:
			n_list_zero = [i for i,x in enumerate(n_list) if x > 0]
		for i in range(n_list_zero[0],len(n_list)):
			nuli = nuli + dictionarie[n_list[i]]
		

	return nuli
result = count_holes('qq')
print result