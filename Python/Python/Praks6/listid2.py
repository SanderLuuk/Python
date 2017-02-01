########################################################################################
# Moodusta jarjend jargnevate sonedega:
# - Jah, kindlasti!
# - Jah!
# - Voib-olla!
# - Ei!
# Tee programm, kus kasutaja saab kysida jah/ei kysimuse ja programm annab vastuse yhe 
# suvalise elemendi eelnevast jarjendist.
# Python suudab juhuslikke arve genereerida:
# import random
# Seejarel voime suvalises kohas programmis kasutada juhusliku arvu saamiseks funktsiooni 
# random.randint(x, y), mis genereerib juhusliku taisarvu x-st y-ni (molemad kaasaarvatud), 
# naiteks: juhuarv = random.randint(1, 10)
# Lisa ka sisse- ja valjajuhatavad tekstid, et dialoog kasutajaga oleks vaimalikult loomulik.
# Kui valmis, siis lisa jarjendisse 20 erinevat vastusevarianti, mille ingliskeelsed vasted 
# leiad lehekyljelt https://en.wikipedia.org/wiki/Magic_8-Ball 
#=======================================================================================
# Autor: Sander Luuk
# Kuupaev: 16.11.2016
#########################################################################################
import random
#
vastused = ["Jah, Kindlasti!", "Jah!", "Voib-olla!", "Ei!"]
#
kysimus = input("sisesta oma kysimus: ")
#
vastuse_jrk_nr = random.randint(0, len(vastused)-1) # len - Pikkus
print(vastused[vastuse_jrk_nr])
#
kas_veel = input ("kas kysid veel? (y voi n): ") 
while (kas_veel is "y"):
	kysimus = input("sisesta oma kysimus: ")
	vastuse_jrk_nr = random.randint(0, 3)
	print(vastused[vastuse_jrk_nr])
	kas_veel = input ("kas kysid veel? (y voi n): ") 
