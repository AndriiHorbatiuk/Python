import sys
import moduls.modul_grupirovanie_spiska
text = str(sys.argv[1])
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Ubiraem probely
text = text.replace(" ","")
# Delaem iz string spisok
text = list(text)
# Zamenyaem bekvy frazy na a i b
for i in range(0,len(text)):
	if text[i].isupper() == True:
		text[i] = text[i].replace(text[i],"b")
	else:
		text[i] = text[i].replace(text[i],"a")
	i += 1
# Grupiruem spisok po 5 elementov. Esli v poslednem elemente net 5 simvolov - ne uchityvaem ego
text = moduls.modul_grupirovanie_spiska.list_divider(text, 5)
count = 0
for count in range(0,len(text)):
	if len(text[count]) < 5:
		del text[count]
	count += 1
# Vychislyaem sootvetstvie bukv klyucha i alfavita
coded_text = ''
for letter in text:

	letter_position = key.find(letter)


	if letter_position != -1:
		new_letter = alphabet[letter_position % len(alphabet)]

	else:
		new_letter = letter

	coded_text = coded_text + new_letter
print coded_text