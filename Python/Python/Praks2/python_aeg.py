# --------------------------------------------------------------
# Ülesanne 1:
#
# Luba kasutajale sisestada aeg kujul tunnid.minutid (näiteks 3.23 tähendab, et tegu on 3 tunniga ja 23 minutiga, aga väärtus on sisestatud nagu komaga arv 3.23)
#
# Programm peab arvutama, mitu tundi ja mitu minutid on sisestatud ja väljastama vastavad teated ekraanile:
# -------------------------------------------------------------
# Autor: Sander Luuk
# Kuupäev: 11.10.2016
# -------------------------------------------------------------
#
import math
# Annan kasutaja sisendi
#
Aeg = float(input( "Sisesta aeg kujul tunnid.minutid: "))
#
# Arvutus
Tunnid = int(Aeg)
# 3.23 - 3 -> 0.23 * 100 -> 23.0 -> 23	
Minutid = int(math.ceil((Aeg - Tunnid) * 100))
# kontroll
if (Tunnid > 23):
	print ("tundide arv ei ole korrektne")
else:
	print ("Tunnid: " + str(Tunnid))
if (Minutid > 59):
	print ("Minutite arv ei ole korrekrne")
else:
	print ("Minutid: " + str(Minutid))