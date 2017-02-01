# -* coding: utf-8 -*-
# -------------------------------------------------------
# arvuta arvude 1'st 10'ni summat
# arvuta arvude 1'st 10'ni paaris arvude summat
# arvuta arvude 1'st 10'ni paaritu arvude summat
# -------------------------------------------------------
# Autor: Sander Luuk
# Kuup‰ev: 17.10.2016
#--------------------------------------------------------
#
# Defineerime summa muutuja
# ja omistame algv‰‰rtuse
summa = 0
# genereerime vajalikud arvud
for arv in range(1, 11):
# prindime arvutusk‰gi v‰lja
	print (summa, "+", arv, "= ", end="")
	# pridime arvud v‰lja kontrollimiseks
	print (arv)
	# arvutame summa v‰lja
	summa = summa + arv
	# prindime arvutatud summa v‰lja
	print("" , summa )
	print( "------------------------" )
#prindime 10 esimese arvu summa
print ("summa = " + str(summa))
print("===========================")