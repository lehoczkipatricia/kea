def szovegKodol(kodold):
	valami=kodold
	valami=valami.replace("a","$")
	valami=valami.replace("i", "ß")
	valami=valami.replace("b", "{")
	valami=valami.replace("n", "}")
	valami=valami.replace("u", "=")
	valami=valami.replace("e", "€")
	return valami

szam=int(input("Kódolás: 1, Dekódolás:2: "))
if (szam==1):
	kodold=str(input("Írd be a szöveget: "))
	kodold=szovegKodol(kodold)
	print("Kódolt szöveg: ",kodold)

	