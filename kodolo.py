def szovegKodol(kodold):
	valami=kodold
	valami=valami.replace("a","$")
	valami=valami.replace("i", "ß")
	valami=valami.replace("b", "{")
	valami=valami.replace("n", "}")
	valami=valami.replace("u", "=")
	valami=valami.replace("e", "€")
	return valami

def szovegDeKodol(kodolas):
	kesz=kodolas
	kesz=kesz.replace("$","a")
	kesz=kesz.replace("ß","i")
	kesz=kesz.replace("}","n")
	kesz=kesz.replace("=","u")
	kesz=kesz.replace("{","b")
	kesz=kesz.replace("€","e")
	return kesz

szam=int(input("Kódolás: 1, Dekódolás:2: "))

if (szam==1):
	kodold=str(input("Írd be a szöveget: "))
	kodold=szovegKodol(kodold)
	print("Kódolt szöveg: ",kodold)


elif (szam==2):
	kodolas=str(input("Írd be a dekódolandó szöveget: "))
	kodolas=szovegDeKodol(kodolas)
	print("Dekódolt szöveg:", kodolas)
	
	


		
