# #########################################
# Esimene python keeles kirjutatud programm
# #########################################
# Tervitus.python
# Autor: Sander Luuk
# Kuupäev: 3.10.2016
###########################################
# võtemae vajalikud moodulid tööle
import math
#kasutaja sisendi küsimine
#ristkylik
pikkus = input('sisesta pikkus: ')
laius = input('sisesta laius: ')
#arvutamine
pindala = int(pikkus) * int(laius)
#väljastamine
print('pindala arvutamine: ')
print('pikkus ' + pikkus)
print('laius ' + laius)
print('pindala ' + str(pindala))
#
#kolmnurk
print ('========================')
a = int(input('Siseta a külje pikkus: '))
b = int(input('Siseta b külje pikkus: '))
c = int(input('Siseta c külje pikkus: '))
# P arvutamine
p = (a+b+c) / 2;
# pindala atvutamine
s = math.sqrt(p* (p-a) * (p-b) * (p-c))
#ümmardamine väärtus 3 komakohaga
s = round(s, 3)
#väljastamine
print ('kolmnurga pindala = ' + str(s))