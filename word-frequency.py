def find_most_frequent(text):
	text = text.lower()
	text = text.split()
	d = dict()
	result_list = list()
# Del unused chars in the list
	chars_to_remove = ['.', '!', '?','-',';',':',',']
	for i in range(0,len(text)):
		text[i] = text[i].translate(None, ''.join(chars_to_remove))
# Check is the list item in the dictionarie (d), yes - add +1 to the value, no - set value to 1
		if text[i] in d:
			d[text[i]] += 1
		else:
			d[text[i]] = 1
# Chack for items in d. If value is more than 1 then add key to the result_list
	for key, freq in d.iteritems():
		if freq > 1:
			result_list.insert((len(result_list)-1),key)
	result_list = sorted(result_list, key=str.lower)
	return result_list
result = find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.')
print result