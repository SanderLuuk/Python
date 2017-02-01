# ===========================================================================
# Fibonacci jada on arvude jada, mille kaks esimest liiget on 0 ja 1 ning 
# iga j�rgnev liige on kahe eelneva liikme summa. (
# Rohkem infot: https://et.wikipedia.org/wiki/Fibonacci_jada ). 
# Kirjutame programmi, mis k�sib kasutajalt arvu ning v�ljastab 
# vastava j�rjekorranumbriga Fibonacci jada liikme. N�iteks kui 
# kasutaja sisestab 5, siis programm v�ljastab 3; kui 
# sisestatakse 7, siis v�ljastatakse 8 
# (Fibonacci jada algus: 0, 1, 1, 2, 3, 5, 8).
# ===========================================================================
# 09.11.2016
# autor: Sander Luuk
# =========================================================================== 
# sisestame j�rjekorranumbri
jrk_nr = int(input("Sisesta Fibonacci j�rjekorra number: ")
# eeltinigimused - 2 esimest liiget
liige1 = 0
liige2 = 1
if jrk_nr == 1:
	print(liige1)
elif jrk_nr == 2:
	print(liige2)

else:
	#arvutame v��rtuse i = ts�kli muutuja
	for i in range(jrk_nr - 2):
		ajutine = liige1
		liige1 = liige2
		liige2 = liige2 + ajutine
	# v�ljastame tulemus
	print(liige2)