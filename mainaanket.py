from moduleaanket import *
while True:
    aanket = input("Kas soovite t?ita ankeeti? (jah/ei): ").lower()
    if aanket == "jah":
        kusimused()
        saada_email()
        break
    elif aanket == "ei":
        print("Ankeedi t?itmine katkestatud.")
        lisakus = input("Kas soovite lisada uue k?simuse? (jah/ei): ").lower()
        if lisakus == "jah":
            lisa_uus_kus()
        else:
            print("Uue k?simuse lisamine katkestatud.")
        break
    else:
        print("Palun sisesta 'jah' v?i 'ei'.")