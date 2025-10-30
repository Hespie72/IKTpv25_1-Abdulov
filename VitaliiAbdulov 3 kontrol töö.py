# 1 variant
#1. Kirjuta programm, mis antud arvu n (vahemikus 1 kuni 9) põhjal kuvab ekraanile n kuuske.
# n = int(input("n on (1-9): "))
# Jõulupuu = [
#             "    /V\\     \t",
#             "   / V \\    \t",
#             "  / V V \\   \t",
#             " /VV V VV\\  \t",
# ]
# if 1 <= n <= 9:
#     for line in Jõulupuu:
#         print (line * n)
# else: 
#     print("siseta õige number")

#2. Korruta kõik paaritud väärtused vahemikus 0 kuni kasutaja sisestatud arvuni (R).
# R = int(input("R on: "))
# tulemus = 1 

# for i in range(1, R * 0, 2):
#     tulemus = tulemus * i

# print(f"Tulemus on: {R} on {tulemus}")
# # 3.
# import random
# randomnumber = random.randint(1, 100)
# katseid = 0

# user = int(input("Arva number 1 kuni 100: "))
# katseid += 1
# while user != randomnumber:
#     if user < randomnumber:
#         print("Sinu number on liiga väike")
#     else:
#         print("Sinu number on liiga suur")
#     user = int(input("Arva number 1 kuni 100: "))
#     katseid += 1
    

# #Loenda paaris- ja paaritud numbrid sisestatud naturaalarvus. Näide: arv 34560 → 3 paarisarvu (4, 6 ja 0) ja 2 paaritut (3 ja 5).
