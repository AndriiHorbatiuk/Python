def file_search(folder, filename):
	path = list()
	if filename in folder:
		path.insert((len(path)+1),folder[0])
		path.insert((len(path)+1),filename)
		if len(path)>1:
			path = '/'.join(path)
	else:
		for i in range (0, len(folder)):
			if isinstance(folder[i],list):
				folder[i][0]=folder[0]+'/'+folder[i][0]
				path = path or file_search(folder[i], filename)
	if not path:
		path = False
		return path
	else:
		return path
result = file_search(['C:', '1.txt', '2.txt', '3.txt'], '4.txt')
print result