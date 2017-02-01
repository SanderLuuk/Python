# karp.py
# kirjeldame karp objekti - fikseerida karbi omadused ja 
# tekitada karbile mingid tegevused
#---------------------------------------------------------------
# Autor: Sander Luuk
# Kuupaev: 28.11.2016
#---------------------------------------------------------------
class Karp:
	'''
	klassi muutujad nimedega laius, korgus, pikkus  vaikimisi vaartused on -1
	'''
	laius = -1
	korgus = -1
	pikkus = -1
	
	def __init__(self, l=-1, k=-1, p=-1):# ise saan m22rata protsessi .. ehk k6rgused ja laiused ja pikkused
		self.laius = l
		self.pikkus = p
		self.korgus = k
		self.kirjeldus()
		
	def kirjeldus(self):
		print('laius = ', self.laius)
		print('pikkus = ', self.pikkus)
		print('korgus = ', self.korgus)
		print('antud karbi ruumala on = ', self.ruumala())
	
	def ruumala(self):
		v = self.laius * self.pikkus * self.korgus   #tegevus on funktsioon , aga nimetame meetodiks
		return v

class Karp_M(Karp):
	materjal = ''
	
	def __init__(self, l=-1 , p=-1 , k=-1 , m=''):
		Karp.__init__(self, l, p, k)
		self.materjal = m
		#self.kirjeldus()
		
	def kirjeldus(self):
		if(self.materjal ==''):
		   Karp.kirjeldus(self)
			
		else:
			print('materjal = ', self.materjal)
			Karp.kirjeldus(self)
	
#
# Objektide loomine 
minu_karp1 = Karp(11, 14, 13)
minu_karp1.kirjeldus()
minu_karp2 = Karp (5, 5, 5)
minu_karp2.kirjeldus()
minu_karp3 = Karp ()
minu_karp3.kirjeldus()
minu_karp4 = Karp_M(7, 7, 7, 'Papp')
minu_karp4.kirjeldus()
