#!/usr/bin/python3
# coding: utf-8


# lien  Formule de Luhn 


print ("Vérification si un nombre, saisi précédemment, (numéro de SIREN, de SIRET, IMEI, de carte bancaire...) suit les conditions fixées de Luhn :\n => (True ou False, \'somme calculée obtenue = True|False\')\n")


def vérifLuhn(ch):
  somme = 0
  # Parité du dernier élément de la chaîne pour appliquer un calcul différent 1 fois sur 2.
  paritéDuDernierElement = len(ch) % 2
  for i in range (len(ch)-1, -1, -1):
    j = int(ch[i])
    # (i+1) car dans une chaîne, le premier élément est compté à partir de zéro : ch[0] et non ch[1].
    if ((i + 1) % 2 != pariteDuDernierElement):
      j = j * 2 
    if (j > 9):
        j = j - 9 
    somme = somme + j
  return somme% 10 == 0, “somme calculée obtenue = “ + str(somme)           
   
for n in (59, 9,  18, 8763, 325373017, 42407859000025, 353809054912495, 1234567890123452):
  print (str(n)+"  =>", vérifLuhn(str(n)))


---------------------------------------------------------------------------- Ou -----------------------------------------------------------------------------


Différences de manière d’obtention avec la version précédente :
 - l'alternance du traitement ne se base pas sur la parité de l’élément en cours mais sur le traitement précédent.
 - le résultat du calcul (*2 et -9 si x*2 > 9, x ∈ [0, 9]) est fourni par un tableau : (res_calcul_mult).
------------------------------------------------------------------------------------------------------------------------------------------------------------------


#!/usr/bin/python3
# coding: utf-8
 
print ("Vérification si un nombre, saisi précédemment, (numéro de SIREN, de SIRET, IMEI, de carte bancaire...) suit les conditions fixées de Luhn :\n => (True ou False, \'somme calculée obtenue = True|False\')\n")


def verifLuhn(ch):
  somme = 0
  calcul_mult = False
  res_calcul_mult = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9] # Suivant la valeur initiale de i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  for i in range(len(ch)-1, -1, -1):
    if (calcul_mult):
      somme += res_calcul_mult[int(ch[i])]
    else:
      somme += int(ch[i])
    calcul_mult = not(calcul_mult)
  return somme%10 == 0, “somme calculée obtenue = “ + str(somme)


for i in (59, 9,  18, 8763, 325373017, 42407859000025, 353809054912495, 1234567890123452):
  print (str(i)+” =>”, verifLuhn(str(i)))
















  
-------------------------------------------------------------------------- Résultat ------------------------------------------------------------------------