#päev=input("Sisesta päev nimetus (näiteks esmaspäev): ")
#1.
#if päev.lower()=="neljapäev":
#    print("huura täna on programmeerimine")
#2.
#if päev.lower()=="neljapäev":
#    print("huura täna on programmeerimine")
#else:
#    print("Igatsen, programmeerida tahaks!")
#3.
#if päev.lower()=="Laupäev" or päev.lower()=="pühapäev":
#    print("Lõpuks, pean tööl käima")
#else:
#    print("Tõõpäev, pean tööl käima!")
#1-E 2-T 3-K 4-N 5-R 6-L 7-P
#paev_number=int(input("Siseta päeva number (1-7): "))
#if paev_number==1:
#   print("Esmaspäev")
#elif paev_number==2:
#   print("Teisipärv")
#elif paev_number==3:
#   print("Kolmapäev")
#elif paev_number==4:
#   print("Neljapäev")
#elif paev_number==5:
#   print("Reede")
#elif paev_number==6:
#   print("Laulpäev")
#elif paev_number==7:
#   print("Pühapäev")
#else:
#   print("Vale number! Palun siseta number vahemikus 1-7")

#1. Juku

#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.

#b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)

#<6 aastad  - tasuta
#6-14 - lastepilet
#15-65 - täispilet
#>65 - sooduspilet
#<0 ja >100 viga andmetega
#eesnimi=input("Sisesta eesnimi: ")
#if eesnimi=="Juku":
#    print("Lähme Jukuga kinno!")
#    vanus=input("Siseta Juku vanus: ")
#    if vanus.isdigit():
#        vanus=int(vanus)
#        if vanus<0 or vanus>100:
#            print("Väga andmetega!")
#        elif vanus<6:
#            print("Pilet on tasuta!")
#        elif vanus<=14:
#            print("Lastepilet!")
#        elif vanus<=65:
#            print("Täispilet")
#        else:
#            print("Sooduspilet")
#    else:
#        print("Palun sisesta vanus täisarvuna")
#2 Pinginaabrid

#Küsi kahe inimese nimed. Kui nimed koosnevad ainult tähedest siis  teavita kasutajat, kas nad on täna pinginaabrid või ei mitte.
#nimi1 = input("Siseta palun nimi =>").capitalize()
#nimi2 = input("Siseta palun nimi =>").capitalize()
#if nimi1.isalpha() and nimi2.isalpha():
#    if nimi1=="Vitalii" and nimi2=="Oleg" or nimi1=="Oleg" and nimi2=="Vitalii":
#        print(f"{nimi1} ja {nimi2} ei täna pinginaabrid")
#    else:
#        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
#else:
#        print("Palun sisesta ainult tähed")

#pikkus = int(input('Sisestage pikkus? '))
#laius = int(input('Siseta laius '))
#if pikkus>0 and laius>0:
#    
#    pindala = pikkus * laius
#    print(f'pindala suurus on {pindala} ')
#    user = input('Kas soovite remondi teha? ').capitalize()
#    if user.isalpha() and user == 'Jah':
#        hind = float(input('ruutmeetri hind? '))
#        if hind>0:
#            remondi_hind = hind * pindala
#            print(f'remondi summa on {remondi_hind} eurot')
#            kes = input("kes remondi teeb?(ise/töötaja) ").capitalize()
#            if kes.isalpha() and kes == 'Ise':
#                print(f'siis summa on {remondi_hind} eurot')
#            else:
#                print(f'siis summa on {remondi_hind + 300} eurot')
#        else:
#            print("Hind ei saa olla negativne!")
#    else:
#        print('Head päeva!')
#else: 
#   print('Arvud peavad olema suurem kui 0!')

#4 Allahindus

#Leia 30% soodustusega hinna, kui alghind on suurem kui 700

#hind = input('Sisesta hind: ')
#if hind.isdigit():
#    hind = float(hind)
#    if hind > 700:
#        soodus_hind = hind * 0.7 #või "hind *= 0.7"
#        print(f'Soodushind on {soodus_hind} eurot')
#    else:
#        print(f'Hind on {hind} eurot')

#5 Temperatuur

#Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)

#temp = input('Sisesta temperatuur: ')
#if temp.isdigit():
#try:
#    temp = int(temp)
#    if temp > 18:
#        print('Temperatuur on üle 18 kraadi')
#    else:
#        print('Temperatuur on alla 18 kraadi')
#except:
#   print('Palun sisesta temperatuur ujukomaarvuna!')

#6 Pikkus

#Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)
try:
    pikkus = float(input('Sisesta oma pikkus cm: '))
    if pikkus  <= 145:
        print('Olete lühike')
    elif pikkus <= 185:
        print('Olete keskmine')
    elif pikkus >= 185:
        print('Olete pikk')
    else: 
        print('Palun sisesta pikkus numbrina!')
except:
    print('Siseta numbrid!' )

#7 Pikkus ja sugu
#
#Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).
#try:
#    pikkus = float(input('Sisesta oma pikkus cm: '))
#    sugu = input('Sisesta oma sugu (mees/naine): ').lower()
#    if sugu == 'mees':
#        if pikkus <= 160:
#            print('Olete lühike mees')
#        elif pikkus <= 190:
#            print('Olete keskmine mees')
#        elif pikkus > 190:
#            print('Olete pikk mees')
#        else:
#            print('Palun sisesta pikkus numbrina!')
#    elif sugu == 'naine':
#        if pikkus <= 150:
#            print('Olete lühike naine')
#        elif pikkus <= 175:
#            print('Olete keskmine naine')
#        elif pikkus > 175:
#            print('Olete pikk naine')
#        else:
#            print('Palun sisesta pikkus numbrina!')
#    else:
#        print('Palun sisesta sugu kas mees või naine!')
#except:
#    pass:
#    print('Siseta numbrid! ')

#8 Poes

#Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).
#from random import randint
#piim_hind = randint(1,5)
#leib_hind = randint(1,5)
#liha_hind = randint(5,15)
#leib = input('Kas sa tahad osta leib? ')
#if leib.lower() == 'jah':
#    tükki = int(input('Mitu tükki? '))
#    leib_summa = leib_hind * tükki
#else:
#    leib_summa = 0
#piim = input('Kas sa tahad osta piim? ')
#if piim.lower() == 'jah':
#    tükki = int(input('Mitu tükki? '))
#    piim_summa = piim_hind * tükki
#else:
#     piim_summa = 0
#liha = input('Kas sa tahad osta liha? ')
#if liha.lower() == 'jah':
#    tükki = int(input('Mitu tükki? '))
#    liha_summa = liha_hind * tükki
#else:
#    liha_summa = 0
#kokku = leib_summa + piim_summa + liha_summa
#print(f"See on sinult {kokku} eurot")