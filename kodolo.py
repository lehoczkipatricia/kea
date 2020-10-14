
szam=int(input("Kódolás: 1, Dekódolás:2: "))
if (szam==1):
	szoveg=input("Írd be a szöveget:")	
	szovegKodol(szoveg)
	print(szoveg)




def szovegKodol(szoveg):
	szoveg.replace("a","$")
	szoveg.replace("é","Ł")
	szoveg.replace("í","ß")
	szoveg.replace("ő","¤")
	szoveg.replace("ő","=")
	szoveg.replace("ü","@")
	szoveg.replace("g","*")
	szoveg.replace("c","+")
	szoveg.replace("b",":")
	return szoveg




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
		
