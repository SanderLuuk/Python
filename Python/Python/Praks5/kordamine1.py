# ===========================================================================
# Fibonacci jada on arvude jada, mille kaks esimest liiget on 0 ja 1 ning 
# iga järgnev liige on kahe eelneva liikme summa. (
# Rohkem infot: https://et.wikipedia.org/wiki/Fibonacci_jada ). 
# Kirjutame programmi, mis küsib kasutajalt arvu ning väljastab 
# vastava järjekorranumbriga Fibonacci jada liikme. Näiteks kui 
# kasutaja sisestab 5, siis programm väljastab 3; kui 
# sisestatakse 7, siis väljastatakse 8 
# (Fibonacci jada algus: 0, 1, 1, 2, 3, 5, 8).
# ===========================================================================
# 09.11.2016
# autor: Sander Luuk
# =========================================================================== 
# sisestame järjekorranumbri
jrk_nr = int(input("Sisesta Fibonacci järjekorra number: ")
# eeltinigimused - 2 esimest liiget
liige1 = 0
liige2 = 1
if jrk_nr == 1:
	print(liige1)
elif jrk_nr == 2:
	print(liige2)

else:
	#arvutame väärtuse i = tsükli muutuja
	for i in range(jrk_nr - 2):
		ajutine = liige1
		liige1 = liige2
		liige2 = liige2 + ajutine
	# väljastame tulemus
	print(liige2)