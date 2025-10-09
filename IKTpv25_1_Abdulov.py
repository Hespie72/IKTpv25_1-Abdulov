#ülesanne 1

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
#ülesanne 2
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
#ülesanne 3
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
#ülesanne 4
#
# from math import pi
#
# ümbermõõdu = float(input('Sisestage ümbermõõdu: '))
# diameeter = ümbermõõdu / pi
# print(f'diameetri pikkus on {diameeter:.2f}')
#
#ülesanne 5
#
# a = float(input('Sisestage N: '))
# b = float(input('Sisestage M: '))
#
# c = float(a**2+b**2)
# print(f'käsureal on {c:.2f}')
#
#ülesanne 6
#
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg
#
# print("Sinu kiirus oli " + str(kiirus) + " km/h")

#ülesanne 7

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

#ülesanne 8

# print('  @..@\n'
#       ' (----)\n'
#       '( \__/ )\n'
#       '^^ "" ^^ '
#
#
#       )

#ülesanne 9

# a = float(input('Sisestage a: '))
# b = float(input('Sisestage b: '))
# c = float(input('Sisestage c: '))
#
# ümbermõõdu = a + b + c
# print(f'valem: P = a + b + c\n'
#       f'{ümbermõõdu}')

# ülesanne 10
#
# pitsa_hind = 12.90 * 0.1
# sõbrad = int(input('Mitu sõbrad läksid Pitsa eest? '))
# pitsa_hind = pitsa_hind/sõbrad
# print(f'Iga sõber peab maksta {pitsa_hind:.2f}')