# 1 variant
#1. Kirjuta programm, mis antud arvu n (vahemikus 1 kuni 9) põhjal kuvab ekraanile n kuuske. проверка
# while True:
#     try:
#         n = int(input("kuidas jõlupuu on (1-9): "))
#         break
#     except:
#         print("siseta numberid!")
# puu1 = r"    /V\     "
# puu2 = r"   / V \    "
# puu3 = r"  / V V \   "
# puu4 = r" /VV V VV\  "
# if 1 <= n <= 9:
#     print (puu1 * n)
#     print (puu2 * n)
#     print (puu3 * n)
#     print (puu4 * n)
# else: 
#     print("siseta õige number")
#2. Korruta kõik paaritud väärtused vahemikus 0 kuni kasutaja sisestatud arvuni (R).
#     R = int(input("Sisestage R-number: "))
# try:
#     for i in range(0, R + 1):
#         if i % 2 != 0:
#             print(f"{i} * {R} = {i * R}")
# except:
#     print("Palun siseta õige number!")
#3. неправильно
# import random

# N = random.randint(5, 15)  
# print(f"numbrite arv on {N}")
# positive_arv = 0
# print("Genereeritud numbrid:")
# for i in range(N):
#     number = random.randint(-10, 10)
#     print(number)
#     if number > 0:
#         positive_arv += 1
# 4. проверка
#   arv = int(input("Sisesta naturaalarv: "))

#   paaris = 0 
#   paaritu = 0  
# try:
#   for number in arv:
#       if int(number) % 2 == 0:
#          paaris += 1
#       else:
#             paaritu += 1
# except:
#    print("Palun siseta number!")
# print(f"Arvus {arv} on {paaris} paarisarvu ja {paaritu} paaritut arvu.")
# 5. проверка
A = int(input("Sisesta arv A: "))
B = int(input("Sisesta arv B: "))

if A > B:
     A, B = B, A
try:
  summa = sum(range(A, B + 1))

  print(f"Arvude {A} kuni {B} summa on {summa}.")
except:
  print("Palun siseta õige number!")