###############################################################
# Loo kaks sonastikku (inglise, itaalia) ja anna neile
# vaartused (nagu jarjendite ylesandes). 
# 
# Lisa sonastikku jargmised sonad:
# - eesti - auto, itaalia - auto, inglise - car
# - eesti - koer, itaalia - cane, inglise - dog
# - eesti - kass, itaalia - gatto, inglise - cat
# - eesti - tere, itaalia - ciao, inglise - hello
# Tolgi (valjasta ekraanile) jargmised sonad:
# - tere -> inglise k, itaalia k
# - auto -> itaalia k
# - kass - > inglise k
###############################################################
inglise = {'yks':'one', 'kaks':'two', 'kolm':'three', 'neli':'four'}
itaalia = {'yks':'uno', 'kaks':'due', 'kolm':'tre', 'neli':'quattro'}
inglise['auto'] = 'car'; itaalia['auto'] = 'auto'
inglise['koer'] = 'dog'; itaalia['koer'] = 'cane'
inglise['kass'] = 'cat'; itaalia['kass'] = 'gatto'
inglise['tere'] = 'hello'; itaalia['tere'] = 'ciao'
sona = input('Sisesta sona tolgendamiseks: ')
print(sona, end='')
if sona in inglise:
   print(' ->',inglise[sona], end='')
if sona in itaalia:
   print(' ->', itaalia[sona], end='')
if sona not in inglise and sona not in itaalia:
   print(' tolget pole inglise ja itaalia sonastikus', end='')
print()
