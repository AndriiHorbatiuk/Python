a = "ABC abc wer ffgt vrtby. RTHryrgh, thryh. GRTHyr5h! wer"
a = a.lower()
a = a.split()
# Del unused chars in the list
chars_to_remove = ['.', '!', '?','-',';',':',',']
for i in range(0,len(a)):
	a[i] = a[i].translate(None, ''.join(chars_to_remove))
