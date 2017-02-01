# sonastik.py
# eesti- ja inglise keelse objektorienteeritud programmeerimise 
# põhimõistete sõnastiku loomine"
#---------------------------------------------------------------
# Autor: Sander Luuk
# Kuupaev: 08.12.2016
#---------------------------------------------------------------

eesti = {'Class': 'Klass', 'Class variable': 'Alamklass', 'Function overloading': 'Funktsiooni ülekate', 'Data member': 'Andme liige', 'Instance variable':  'Eksemplarmuutuja', 'Inheritance': 'Pärilus', 'Instance':'Eksemplar', 'Instantiation':'Klassi eksemplar', 'Method':'Protseduur', 'Object': 'Andmete ja meetodite komplekt', 'Operator overloading': 'Operaatori ülekate'} 
inglise ={ 'Klass': 'Class', 'Alamklass': 'Class variable', 'Funktsiooni ülekate': 'Function overloading', 'Andme liige': 'Data member', 'Eksemplarmuutuja': 'Instance variable', 'Pärilus': 'Inheritance', 'Eksemplar': 'Instance', 'Klassi eksemplar': 'instantiation', 'Protseduur': 'Method', ' Andmete ja meetodite komplekt': 'Object', 'Operaatori ülekate':'Operator overloading'}
sõna = input ('sisesta  pythoni andmetüübi inglisekeelne sõna tõlkimiseks! (suure tähega) ')


print(sõna, end='')
if sõna in eesti:
   print(' ->',eesti[sõna], end='')
if sõna in inglise:
   print(' ->', inglise[sõna], end='')
if sõna not in inglise and sõna not in eesti:
   print(' tõlget pole inglise- ja eestikeelses sõnastikus', end='')
print()
#

kas_veel = input('Kas tahad veel tõlget? (y või n): ')
while(kas_veel == 'y'):
	sõna = input ('sisesta  pythoni andmetüübi inglisekeelne sõna tõlkimiseks! (suure tähega) ')
	if sõna in eesti:
		print(' ->',eesti[sõna], end='')
	if sõna in inglise:
		print(' ->', inglise[sõna], end='')
	if sõna not in inglise and sõna not in eesti:
		print(' tõlget pole inglise- ja eestikeelses sõnastikus', end='')
	print()
	kas_veel = input('Kas tahad veel tõlget? (y või n): ')