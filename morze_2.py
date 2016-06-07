def encode_morze(text):
	text_list = list()
	sygnal = list()
	sygnal_final = list()
	morse_code = {" ":" ","A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}
	sygnal_diagram = {" ":"___", ".":"^", "-":"^^^", "*":"___"}
	initial_text_list = list((str(text)).upper())
	for i in initial_text_list:
		if i in morse_code:
			text_list.insert((len(text_list)+1),morse_code[i])
			if i != ' ':
				text_list.insert((len(text_list)+2),"*")
	a = "".join(text_list)
	a = list(a)
	del a[len(a)-1]
	for i in range(0,len(a)-1):
		if a[i] == ' ':
			del a[i-1]
	for i in a:
		if i in sygnal_diagram:
			sygnal.insert((len(sygnal)+1),sygnal_diagram[i])
	for i in range(0,len(sygnal)-1):
		if sygnal[i+1] != '___' and sygnal[i] != '___':
			sygnal_final.insert((len(sygnal_final)+1),sygnal[i])
			sygnal_final.insert((len(sygnal_final)+1),'_')
		elif sygnal[i+1] == '___' or sygnal[i] == '___':
			sygnal_final.insert((len(sygnal_final)+1),sygnal[i])
		elif i == len(sygnal[i])-1:
			sygnal_final.insert((len(sygnal_final)+1),sygnal[i])
	sygnal_final.insert((len(sygnal_final)+1),sygnal[len(sygnal)-1])
	sygnal_final = "".join(sygnal_final)
	return sygnal_final

print encode_morze('Prometheus')