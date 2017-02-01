# --------------------------------------------------------------
# Programm peab valjastama kujundi.
# 0 0 0 0 0
# 0       0
# 0       0
# 0       0
# 0 0 0 0 0 
# ridade ja veergude arv peab olema voimalik muuta
#---------------------------------------------------------------
# autor: Sander Luuk
# Kuupaev: 24.10.2016
#----------------------------------------------------------------
# kasutaja sisend
# abi funktsioon
# valjasta ilma rea vahetuseta
# funktsiooni argumendiks on symbol

def irv(s):
	print(s + " ", end="")
# kujundi funktsioon
def kujund(s):
	for r in range(1, rida+1):
		if r==1 or r==rida:
			for v in range(1, veerg+1):
				irv("+")
		else:
			irv("+")
			for v in range (2, veerg):
				irv(" ")
			irv("+")
		print()
#kasutus
rida = int(input("ridade arv: "))
veerg = int(input("veergude arv: "))
kujund("+")