#from os import PathLike


#print ("Tere maailm!")
#nimi=input("Sisesta oma nimi: ").capitalize()# sisend ja ootab enterit
#print(f"Tere maailm! Tervitan sind {nimi}")
#vanus=int(input("Sisesta oma vanus: "))#int teisendab stringi täisarvuks
#print(f"Tere maalim! Tervitan sind {nimi.upper{}}. sa oled {vanus} aastat vana") #upper teeb suurtähed
#print(f"Tere maalim! Tervitan sind {nimi.lower{}}. sa oled {vanus} aastat vana") #lower teeb väiketähed

# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta.
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile,
# kui palju komme laual nüüd on.
#from random import *
#laua_peal=randint(10, 50) #juhuslik arv 10-50
#print(f"Laual on {laua_peal} kommi")
#võtab=int(input("Mitu kommi sa soovid võtta? ")) #sesind võtab teisendab stringi täisarvuks
#laua_peal-=võtab #laua_peal=laua_peal-võtab, võtab kommid laualt maha
#print(f"Laual on nüüd {laua_peal} kommi")




# 2.
# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 1.65
# d) kas_on_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende
# Kirjuta kood tüüpide kontrollimiseks.
#vanus = 18          #int
#eesnimi = "Jaak"    #str
#pikkus = 1.65      #float
#kas_kaib_koolis = True  #bool
#print(f"vanus {vanus} on: {type(vanus)}")
#print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
#print(f"pikkus {pikkus} on: {type(pikkus)}")
#print(f"kas_kaib_koolis {kas_kaib_koolis} on: {type(kas_kaib_koolis)}")

#4.
#import math 
#
#umbermoodu = float(input("Sisseta puu umbermoot (cm): "))
#diameeter = umbermoodu / math.pi
#print("Puu diameeter on:", round(diameeter, 2), "cm")

#5.
#print('Tere, maailm!')
#nimi = input('Mis on sinu nimi? ').capitalize()

#print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
#print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
#vanus = input()
#print(f'Oi kui tore, sa oled {vanus} aastat vana')





#vanus = 18  #int
#nimi = 'Jaak'  #str
#pikkus = 16.5  #float
#kas_käib_koolis = False  #bool

#if kas_käib_koolis == True:
#    print('Näeme koolis')
#else:
#    print('Näeme tööl')

#print(type(vanus))
#print(type(nimi))
#print(type(pikkus))
#print(type(kas_käib_koolis))


#from random import randint
#while True:
#    kommid = randint(5, 10)
#    print(f'Laual on {kommid} kommi')
#    poiss = int(input('Mitu kommi sa soovid võtta? '))
#    if poiss > kommid:
#        print('Laual pole nii palju komme')
#    else:
#        print(f'Laual on {kommid - poiss} kommi')



#from math import pi

#ümbermõõdu = float(input('Sisestage ümbermõõdu: '))
#diameeter = ümbermõõdu / pi
#print(f'diameetri pikkus on {diameeter}')


#a = float(input('Sisestage N: '))
#b = float(input('Sisestage M: '))

#c = float(a**2+b**2)
#print(f'käsureal on {c:.2f}')


#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg

#print("Sinu kiirus oli " + str(kiirus) + " km/h")
# print('Tere, maailm!')
# nimi = input('Mis on sinu nimi? ').capitalize()
#
# print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
# print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
# vanus = input()
# print(f'Oi kui tore, sa oled {vanus} aastat vana')
#
#
#
#
#
# vanus = 18  #int
# nimi = 'Jaak'  #str
# pikkus = 16.5  #float
# kas_käib_koolis = False  #bool
#
# if kas_käib_koolis == True:
#    print('Näeme koolis')
# else:
#    print('Näeme tööl')
#
# print(type(vanus))
# print(type(nimi))
# print(type(pikkus))
# print(type(kas_käib_koolis))
#
#
# from random import randint
# while True:
#    kommid = randint(5, 10)
#    print(f'Laual on {kommid} kommi')
#    poiss = int(input('Mitu kommi sa soovid võtta? '))
#    if poiss > kommid:
#        print('Laual pole nii palju komme')
#    else:
#        print(f'Laual on {kommid - poiss} kommi')
#
#
#
# from math import pi
#
# ümbermõõdu = float(input('Sisestage ümbermõõdu: '))
# diameeter = ümbermõõdu / pi
# print(f'diameetri pikkus on {diameeter}')
#
#
# a = float(input('Sisestage N: '))
# b = float(input('Sisestage M: '))
#
# c = float(a**2+b**2)
# print(f'käsureal on {c:.2f}')
#
#
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg
#
# print("Sinu kiirus oli " + str(kiirus) + " km/h")

# numbrid = []
# for u in range(5):
#     a = int(input('Sissestage numbrid: '))
#     numbrid.append(a)
#
# kesk = 0
# for i in range(len(numbrid)):
#     kesk = kesk + numbrid[i]
#     result = kesk/len(numbrid)
# print(result)

# print('  @..@\n'
#       ' (----)\n'
#       '( \__/ )\n'
#       '^^ "" ^^ '
#
#
#       )

# a = float(input('Sisestage a: '))
# b = float(input('Sisestage b: '))
# c = float(input('Sisestage c: '))
#
# ümbermõõdu = a + b + c
# print(f'valem: P = a + b + c\n'
#       f'{ümbermõõdu}')

# 
# numbrid = []
# pitsa_hind = 12.90 * 0.1
# sõbrad = int(input('Mitu sõbrad läksid Pitsa eest? '))
# pitsa_hind = pitsa_hind/sõbrad
# print(f'Iga sõber peab maksta {pitsa_hind:.2f}')
