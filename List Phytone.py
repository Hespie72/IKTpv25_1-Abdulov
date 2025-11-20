#List-loend
#Loome listi
from ast import Str


l=[]#tühi list
l1=[]
print(f"Listi algseis: {l}")
while True:
    print("Tee valik:")
    print("\n1-lisa elemente\n2-Lisa elemente pos-le\n3-Eemalda elemente pos jarge\n4-element\n5-sort\n6-reverse\n7-clear\n8-2list")
    while True:
        try:
            valik=int(input())
            break
        except:
            print("Arvud: 1....n")
    print("Tõõ listiga")
    if valik==1:
        while True:
            try:
                i=int(input("Mitu elementi soovid lisada? "))
                if i>0:
                    break
                else:
                    print("Arvud >0")
            except:
                print("siseta õige number!")
        for element_id in range(i):
            element=input(f"{element_id}. element ")
            l.append(element)
        print(f"Uuendatud list on {l}")
    elif valik==2:
            while True:
                try:
                    pos=int(input(f"Positisioon kuhu soovid lisada (0-{len(l)})"))
                    if 0<=pos<=len(l):
                        break
                    else:
                        print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
                except:
                    print("Täisarv on vaja kasutada")
            element=input("Siseta element mid soovid lisada: ")
            l.insert(pos,element)
            print(f"Uuendtud list on {l} ")
    elif valik==3:
        while True:
            try:
                pos=int(input(f"Positisioon kuhu soovid eemaldada (0-{len(l)-1}): "))
                if 0<=pos<=len(l)-1:
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
            except:
                print("Täisarv on vaja kasutada")
        eem_element=l.pop(pos)
        print(f"Eemldatud element on {eem_element}")
        print(f"sinu list on {l} ")
    elif valik==4:
        element=input("Siseta element mid soovid eemaldada: ")
        mitu=l.count(element)
        if mitu==0:
            print("Elementi ei leitud")
        else:
            for e in range(mitu):
                print(f"Eemaldame element '{element}' {l.index(element)} positsioonilt")
                l.remove(element)
        print(f"Uuendatud list on {l}")
    elif valik==5:
        l.sort()
        print(f"Sorteeritud list on {l}")
    elif valik==6:
        l.reverse()
        print(f"Pööratud list on {l}")
    elif valik==7:
        l.clear()
        print(f"List on tühi {l}")
    elif valik==8:
        while True:
            try:
                u=int(input("Mitu elementi soovid teise listi lisada? "))
                if u>0:
                    break
            except:
                print("siseta õige number!")

        for e in range(u):
            element1=input(f"sisesta {e}. element ")
            l1.append(element)
        l.extend(l1)
        print(f"Uuendatud list on {l}")
