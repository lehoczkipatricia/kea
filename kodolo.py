
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
	szoveg.replace("ü","=")
	szoveg.replace("g","*")
	szoveg.replace("c","+")
	szoveg.replace("b",":")
	return szoveg
	
#szovegDeKodol():