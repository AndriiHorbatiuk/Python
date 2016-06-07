# Grupiruem spisok po 5 elementov. Esli v poslednem elemente net 5 simvolov - ne uchityvaem ego
def list_divider(text,n):
	text = [''.join(text[i:i+n]) for i in range(0, len(text), n)]
	return text