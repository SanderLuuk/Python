
# -------------------------------------------------------
# arvuta kasutaja poolt sisestatud arvu faktoriaal
# arvuta arvude 1'st 10'ni paaris arvude summat
# arvuta arvude 1'st 10'ni paaritu arvude summat
# -------------------------------------------------------
# fail: faktoriaal.py
# Autor: Sander Luuk
# Kuup�ev: 17.10.2016
#--------------------------------------------------------
#
# Lubame kasutajal sisestada numbri
n = int (input("sisesta positiivne arv: "))
# Ku isisestatud number on negatiivne
if n < 0:
# v�ljasta vastav teada
	print ("Sellist vaartust ei saa kasutada: ")
# kui sisestatud vaartus on positiivne
else:
# defineerin fakt algvaartuse
	fakt = 1
	# nulli korral arvutust ei toimu
	if n == 0:
		print(str(n) + "! = " + str(fakt))
	# K�ik mis on suurem kui nulli
	else:
		for arv in range(1, n+1):
			# prindime arvutusk�gi v�lja
			print (fakt, "*", arv, "= ", end="")
			# pridime arvud v�lja kontrollimiseks
			print (arv)
			# arvutame summa v�lja
			fakt = fakt * arv
			# prindime arvutatud summa v�lja
			print("" , fakt )
			print( "------------------------" )
			# prindime l�pptulemuse
	print(str(n) + "! = " + str(fakt))