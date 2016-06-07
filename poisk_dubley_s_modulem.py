text = [1, 1.0, '1', -1, 1]
def clean_list(list_to_clean):
	new_list = list()
	#new_list.insert(0, list_to_clean[0])
	for letter in range(0,(len(list_to_clean))):
		if list_to_clean[letter] not in new_list:
			new_list.insert((len(new_list)+1), list_to_clean[letter])
	return new_list
text = clean_list(text)
print text