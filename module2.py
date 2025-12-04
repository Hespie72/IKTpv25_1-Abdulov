from module1 import *

while True:
    try:
        arv1=float(input("Sisesta esimene arv: "))
        break
    except ValueError:
        print("Palun sisesta arv!")
while True:
    try:
        arv2=float(input("Sisesta teine arv: "))
        break
    except ValueError:
        print("Palun sisesta arv!")
t=input("Sisesta tehe (+, -, *, /): ")
tulemus=arithmetic(arv1,arv2,t)
print(f"{arv1} {t} {arv2} = {tulemus}")