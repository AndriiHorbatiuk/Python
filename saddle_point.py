def saddle_point(matrix):
		column_list = [None]*len(matrix)
		minimum = list()
		for i in range(0, len(matrix)):
# Sozdaem massiv minimalnyh znacheniy
			minimum.insert(len(minimum)+1,min(matrix[i]))
# Zapisyvaem poziciii minimalnyh znacheniy v strokah
			minimum_position = matrix[i].index(min(matrix[i]))
			print minimum_position
# Zapisyvaem stolbec v massiv
			for count in range(0,len(matrix)):
				column_list[count] = matrix[count][minimum_position]
# Sravnivaem maksimalnyy element v stolvce s minimalnym v stroke
			if max(column_list) in minimum:
				return (i,minimum_position)
			else:
				return False

result = saddle_point([[0,0,0],[2,1,2],[1,0,1]])
print result