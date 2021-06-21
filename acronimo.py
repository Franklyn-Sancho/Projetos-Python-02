text = str(input('entre com uma string\n'))
text = text.split()
acronym = ""
for i in text:
	acronym = acronym+str(i[0]).upper()
	print(acronym)