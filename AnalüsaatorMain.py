from AnalüsaatorModule import *
import os

while True:
    print("""
1 - Otsi faile laiendi järgi
2 - Analüüsi faili
3 - Loo raporti kataloog
4 - Otsi faile algustähe järgi
5 - otsi faili
0 - Välju
""")

    valik = input("Vali: ")

    if valik == "1":
        failid = leia_projektifailid()
        print("Leitud failid:", failid)

    elif valik == "2":
        tulemus = analuusi_faili_sisu()
        print("Analüüsi tulemus:", tulemus)

    elif valik == "3":
        kaust = loo_raporti_kataloog()
        print("Kataloog valmis:", kaust)

    elif valik == "4":
        failid = leia_failid_algustahega()
        print("Leitud failid:", failid)

    elif valik == "5":
        otsitav_fail=input("Sisesta otsitava faili nimi(nt minu_fail.txt): ") 
        tulemus == otsi_faili(otsitav_fail)
        print(tulemus)
    elif valik == "0":
        print("Programm lõpetatud")
        break

    else:
        print("Vale valik!")