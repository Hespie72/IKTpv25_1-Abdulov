# 1️⃣ Sõna või lause analüüs
# Sisesta sõna või lause.
# Loenda:
# mitu täishäälikut 
# mitu kaashäälikut 
# kui sisestati lause – loenda ka tühikud ja kirjavahemärgid 
# import string
# t=[ 'a', 'e', 'i', 'o', 'u', 'ü', 'ä', 'õ', 'õ']
k=[ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'v', 'z', 'x', 'q', 'w', 'r', 't', 'p']
# m=string.punctuation + string.whitespace
# sõna_lause=input("Siseta sõna või lause: ").lower()
# täishäälikud=0
# kaashäälikud=0
# märgid=0
# for täht in sõna_lause:
#     if täht in t:
#         täishäälikud+=1
#     elif täht in k:
#         kaashäälikud+=1
#     elif täht in m:
#         märgid+=1
# print(f"Sõnas või lauses on {täishäälikud} täishäälikut, {kaashäälikud} kaashäälikut ja {märgid} märki.")
# print(f", {kaashäälikud} kaashäälikut ja {märgid} märki.")
# 2️ Loendid
# 2.1 Nimed 
# Küsi kasutajalt viis nime.
# Salvesta nimed loendisse ja kuva need tähestikulises järjekorras.
# Kuva viimane lisatud nimi.
# Lisa võimalus nimekirjas olevaid nimesid muuta ✍
# from math import e
# nimed=[]
# for i in range(5):
#     nimi=input(f"Sisesta {i+1}. nimi: ")
#     nimed.append(nimi)
# print("Nimed on lisatud")
# nimed.sort()
# print(f"Nimed tähestikulises järjekorras: {nimed}")
# print(f"Viimane lisatud nimi on: {nimed[-1]}")
# print("kas soovid nimekirjas olevaid nimesid muuta? (jah/ei): ")
# vastus=input("Sisesta jah või ei: ").lower()
# if vastus=="jah":
#     while True:
#         try:
#             pos=int(input(f"Positsioon (0-{len(nimed)-1}): "))
#             if 0<=pos<=len(nimed)-1:
#                 break
#             else:
#                 print(f"Positsioon peab olema vahemikus 0 kuni {len(nimed)-1}")
#         except:
#             print("Täisarv on vaja kasutada")
#     uus_nimi=input("Sisesta uus nimi: ")
#     nimed[pos]=uus_nimi
#     print(f"Uuendatud nimed on: {nimed}")
#2.2 Kordustega nimed 🔁 Antud on loend kordustega. Koosta programm, mis väljastab nimed ilma kordusteta
# nimed=["Mari", "Jüri", "Kati", "Mari", "Peeter", "Jüri", "Anna"]
# ilma_kordusteta = list(set(nimed))
# print(f"Nimed ilma kordusteta: {ilma_kordusteta}")
#2.3 Vanused 🎂 Koosta vanuste loend ja leia: suurim väikseim kogusumma keskmine
# vana=[12, 45, 23, 67, 34, 89, 23, 45, 12]
# print(f"Vanuste loend: {vana}")
# print(f"Suurim vanus: {max(vana)}")
# print(f"Väikseim vanus: {min(vana)}")
# print(f"Vanuste kogusumma: {sum(vana)}")
# print(f"Vanuste keskmine: {sum(vana)/len(vana)}")
#3️ Kasuta loendis olevaid arve ja joonista tärnidega diagramm.
# ******************
# *******************
# ********************************
# *****************************************
# ****************************************************
# ************
# list1=[5, 7, 16, 21, 28, 12]
# for arv in list1:
#     print('*'*arv)
#4️ Töö listiga 📝 Koosta menüü, mis võimaldab kasutajal teha järgnevaid toiminguid listiga:
# indexid=["Tallinn", "Tartu", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa" "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
# while True:
#     try:
#         index=int(input("Sisesta indeks (0-9): "))
#         if 0<=index<=9:
#             print(f"Valitud asukoht on: {indexid[index]}")
#             break
#         else:
#             print("Indeks peab olema vahemikus 0 kuni 9")
#     except:
#         print("Täisarv on vaja kasutada")
# index_list=list(str(index))
# n1=int(index_list[0])
# print(f"Esimene number on: {index} {indexid[n1-1]}")
# if n1 in [0, 1, 2, 7]:
#     print("Mine mere!")
# else:
#     print("Mine metsa!")
#5️ Töö listiga 
# import random


# loend_arvud=[]
# loend_tähed= []
# mitu=random.randint(2,20)
# for i in range(mitu):
#     elem=random.randint(1,100)
#     loend_arvud.append(elem)
#     täht=chr(random.randint(65,90))
# print(loend_arvud)
# while 1:
#     try:
#         user = int(input(f"Sisesta mitu paari soovid vahetada (max {mitu//2}): "))
#         if 1 <= user <= mitu//2:
#             break
#         else:
#             print(f"Vale sisestus.(max {mitu//2} )")

#     except:
#         print("Vale andmetüüp, proovi uuesti.")
#         continue


# for i in range(user):
#     loend_arvud[i], loend_arvud[-(i+1)] = loend_arvud[-(i+1)], loend_arvud[i]
# print("Vahetatud loend: ", loend_arvud)
# 6
loend_arvud[]
mitu=radint(2,20)
