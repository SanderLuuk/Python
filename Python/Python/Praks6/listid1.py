#######################################################################################
# Lihtsa sonaraamatu jaoks koosta neli jarjendit (arv, eesti, inglise, itaalia) sisuga:
# - arv - 1, 2, 3, 4
# - eesti - yks, kaks, kolm, neli
# - inglise - one, two, three, four
# - itaalia - uno, due, tre, quattro
# Valjasta koik elemendid tabelina ekraanile:
# 1 - yks - one - uno
# 2 - kaks - two - due
#...
# - Lisa arvude ja eesti jarjendile veel kaks elementi.
# - Kontrolli, kas itaalia sonade jarjendis eksiteerib element 'tre'
# - Valjasta koigi nelja jarjendi elemendid tahestikulises jarjekorras kasvavalt. 
#====================================================================================
#Kuupaev : 16.11.2016
#Autor : Sander Luuk
#====================================================================================
########################################################################################
arvud = [1, 2, 3, 4]
eesti = ['yks', 'kaks', 'kolm', 'neli']
inglise = ['one', 'two', 'three', 'four']
itaalia = ['uno', 'due', 'tre', 'quattro']
# 
elementide_arv = len(arvud)
#
for i in range(elementide_arv):
  print(arvud[i], '-', eesti[i], '-', inglise[i], '-', itaalia[i])
#
#
arvud.append(5)
arvud.append(6)
eesti.append('viis')
eesti.append('kuus')
#
# eesti.sort()
for sona in eesti:
   print(sona)
#
#
#
for jarjend in jarjendid:
	for i in range(len(jarjend)):
		print(jarjend[i], "-", end="")
	print()
#
#
jarjendid = [arvud, eesti, inglise, itaalia]
for jarjend in jarjendid:
  jarjend.sort()
  for element in jarjend:
    print(element, ' ', end="")
  print()
#  
element = 'tre'
if element in itaalia:
   print('Element ' + element + ' olemas itaalia listis')
else:
   print('Element ' + element + ' ei ole itaalia listis')