def encode_morze(text):
	text_list = list()
	sygnal = list()
	morse_code = {" ":" ","A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}
	sygnal_diagram = {" ":"_______", ".":"^", "-":"^^^"}
	initial_text_list = list((str(text)).upper())
	for i in initial_text_list:
		if i in morse_code:
			text_list.insert((len(text_list)+1),morse_code[i])
			a = list(str(text_list[len(text_list)-1]))
			print a
			for i in a:
				if i in sygnal_diagram:
					sygnal.insert((len(sygnal)+1),sygnal_diagram[i])
					print sygnal
	sygnal = "_".join(sygnal)
	return sygnal

print encode_morze('sos')