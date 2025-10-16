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

pikkus = int(input('Sisestage pikkus?'))
laius = int(input('Siseta laius'))

pindala = pikkus * laius
print(f'pindala suurus on{pindala}')
user = input('Kas soovite remondi teha? ').capitalize()
if user.isalpha() and user == 'Jah':
    hind = float(input('ruutmeetri hind? '))
    remondi_hind = hind * pindala
    print(f'remondi summa on {remondi_hind} eurot')
    kes = input("kes remondi teeb?(ise/töötaja) ").capitalize()
    if kes.isalpha() and kes == 'Ise':
        print(f'siis summa on {remondi_hind} eurot')
    else:
        print(f'siis summa on {remondi_hind + 300} eurot')
else:
    print('Head päeva!')
