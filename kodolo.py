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

	
	szoveg.replace("ü","=")
	

#szovegDeKodol():


if (szam==2):
	
	text=str(input("Írd be a dekódolandó szöveget: "))
"""
	kesz=dekod.replace("$","a")
	kesz=dekod.replace("Ł","é")
	kesz=dekod.replace("ß","í")
	kesz=dekod.replace("¤","ő")
	kesz=dekod.replace("=","ő")
	kesz=dekod.replace("@","ü")
	kesz=dekod.replace("*","g")
	kesz=dekod.replace("+","c")
	kesz=dekod.replace(":","b")
	print(kesz)
	"""
def szovegDeKodol(text):
    chars = "\\`*_{}[]()>#+-.!$"
    for c in chars:
        text = text.replace(c, "\\" + c)
		
