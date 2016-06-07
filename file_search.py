def file_search(folder, filename):
	path = list()
	for i in range (0, len(folder)):
		if filename in folder[i]:
				path.insert((len(path)+1),folder[0])
				path.insert((len(path)+1),filename)
		elif filename not in folder[i] and len(folder) < 2:
				path = False
		if isinstance(folder[i],list):
			if filename in folder[i]:
				path.insert((len(path)+1),folder[i][0])
				path.insert((len(path)+1),filename)
			else:
				for count in range(0,len(folder[i])):
					if isinstance(folder[i][count],list):
						if filename in folder[i][count]:
							path.insert((len(path)+1),folder[i][0])
							path.insert((len(path)+1),folder[i][count][0])
							path.insert((len(path)+1),filename)
						else:
							for count2 in range(0,len(folder[i][count])):
								if isinstance(folder[i][count][count2],list):
									if filename in folder[i][count][count2]:
										path.insert((len(path)+1),folder[i][0])
										path.insert((len(path)+1),folder[i][count][0])
										path.insert((len(path)+1),folder[i][count][count2][0])
										path.insert((len(path)+1),filename)

	if path == False:
		return path
	elif len(path) > 2:
		path.insert(0,folder[0])
		path = '/'.join(path)
		return path
	elif len(path) <= 2:
		path = '/'.join(path)
		return path

result = file_search(['C:'], 'crack.exe')
print result