# --------------------------------------------------------------
# Luba kasutajale sisetada suvaline taisarv
# ja arvuta antud taisarvu numbrite summa
# Naiteks kasutaja sisestas 123 ja programm
# arvutab 1+2+3=6
#---------------------------------------------------------------
# autor: Sander Luuk
# Kuupaev: 24.10.2016
#----------------------------------------------------------------
# kasutaja sisend
arv = abs(int(input("sisesta suvaline taisarv: ")))
summa = 0
while arv > 0:
	number = arv % 10
	summa = summa + number
	arv = arv // 10
	print("number = ", number)
	print("arv = ", arv)
	print("summa = ", summa)
	print("===============")
print("summa = " + str(summa))