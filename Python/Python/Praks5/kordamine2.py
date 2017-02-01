# ====================================================
# NB! Suvaliste arvude genereerimiseks kasutame moodulit 
# random, mille saab oma programmi lisada käsuga:
# import random
# Ning suvalise arvu saame genereerida ette antud 
# vahemikust funktsiooniga randint(algus, lõpp):
# random.randint(4,10) # genereeritakse suvaline arv vahemikust 4-10
#
# Koosta programm, mis aitab lastel treenida liitmist. 
# Programm peaks pakkuma välja juhuslike arvudega
# liitmistehteid ning ootama kasutajalt vastust. Kui vastus on 
# õige, kiitma kasutajat, kui aga vale, andma õige vastuse 
# ja esitama uue tehte. Järjest esitatavate tehete 
# hulk võib olla programmis ette antud (näiteks 10),
# samuti võib olla ette antud piirid, kui suuri arve kasutajalt 
# küsitakse (näiteks 1 kuni 50). Programm peaks
# pidama arvestust ka õigete vastuste üle ning väljastama pärast 
# viimast tehet tulemuse.
# ====================================================
# Kuupäev: 09.11.2016
# autor: Sander Luuk
# ====================================================
import random  # toon sisse random elemendi  PS: randomit kasutaades on vaja kindalsti määrata ära min ja max arv. Kui suurem arv esitada ennem kui väiksem siis on vaja kasutada if meetodit. PS Koolon  = THEN.

#
mitu_korda = int(input("Mitu korda arvutad: ")) # määran ära mitu korda ma tahan arvutuskäiku teha
min_arv = int(input( "Milline on vaikseim arv")) # määran ära milline on minimaalne suvaline arv 
max_arv = int(input( "Milline on suurim arv")) # määran ära milline on suurim suvaline arv
#
on_oige = 0 
#
for kord in range(1, mitu_korda+1):
	arv1 = random.randint(min_arv,max_arv)
	arv2 = random.randint(min_arv,max_arv)
	summa = arv1 + arv2
	vorrand = str(arv1) + " + " + str(arv2) + " = "
	vastus = int(input(vorrand))
	if vastus == summa:
		print("tubli!")
		on_oige = on_oige + 1
	else:
		print ("vale " + vorrand + str(summa))
print("oigete vastuste arv on " + str(on_oige))


