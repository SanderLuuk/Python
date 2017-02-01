# --------------------------------------------------------------
# Ülesanne 2:
# Oletame, et tegu on reisi organiseerimisega, ning tuleb lubada teatud suurusega grupp bussidega sõita reisile. Koosta programm, mis võimaldab sisestada, mitu inimest on gruppist # # ja mitu kohta on ühes bussis. 
# Programm peab arvutama, mitu bussi läheb vaja ning vajadusel ka annab teada, kas on olemas need kes ei mahtunud olemasolevate busside sisse:
# -------------------------------------------------------------
# Autor: Sander Luuk
# Kuupäev: 11.10.2016
# -------------------------------------------------------------
#
# Kasutaja sisend
#
inimeste_arv = int(input("inimeste arv grupis: "))
kohtade_arv_bussis = int(input("Kohtade arv bussis: "))
#
busside_arv = inimeste_arv // kohtade_arv_bussis
maha_jaanud_inimesed = inimeste_arv % kohtade_arv_bussis
# kontrollime, kas olemas need inimesed kes on maha jäänud
if(maha_jaanud_inimesed > 0):
	print("On olemas maha jaanuid: \n" + str(maha_jaanud_inimesed) + " inimest, seega")
	busside_arv = busside_arv + 1
print("Reisiks läheb vaja: " + str(busside_arv) + " bussi")