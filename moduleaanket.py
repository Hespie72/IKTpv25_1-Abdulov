import random
import smtplib, ssl
from email.message import EmailMessage

kus=[]
vas=[]
punktid=0

with open("kusimused.txt","r",encoding="utf-8") as f:
    for rida in f:
        kus.append(rida.strip())
with open("vastus.txt","r",encoding="utf-8") as f:
    for rida in f:
        vas.append(rida.strip())

def saada_email():
    generator_email=valik_nimi+"."+valik_perknimi+"@gmail.com"  
    kusemail=input(f"Kas see on teie eposti aadress {generator_email}? (jah/ei): ").lower().strip()
    if kusemail=="jah":
        kellele=generator_email
    elif kusemail=="ei":
        kellele=input("Sisesta oma eposti: ")
    else:
        print("Palun sisesta jah või ei!")
        return saada_email()
    kiri=f"""Tere, see on teie küsitluse tulemus. {punktid}/"""
    teema="Küsimustik Pythonis"
    saatja_email="vitalya.abdulov.1979@gmail.com"
    parool="iccp iixp npok vsnp"
    smtp_server="smtp.gmail.com"
    port=587
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg["Subject"]=teema
    msg["From"]=saatja_email
    msg["To"]=kellele
    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email,parool)
            server.send_message(msg) #kui ei kasuta with siis on vaja sulgeda server.quit()
    except Exception as e:
        print(f"Midagi läks valesti... {e}")

def kusimused():
    global valik_nimi
    global valik_perknimi
    valik_nimi=input("Sisesta oma nimi?: ").lower().strip()
    valik_perknimi=input("Sisesta oma perekonnanimi: ").lower()
    kuscount=0
    for i in range(0, random.randint(0, len(kus)-1)):
        kuscount = random.randint(0, len(kus)-1)
        print(kus[kuscount])
        answer=input("Sisesta oma vastus: ").lower().strip()
        if answer.lower()==vas[kuscount].lower():
            print("Õige vastus!")
            global punktid
            punktid+=1
        else:
            print(f"Vale vastus! Õige vastus on: {vas[kuscount]}")
        kuscount+=1
    print(f"Sinu punktid on: {punktid}/")
def lisa_uus_kus():
    mitu_kus=0
    with open("kusimused.txt","a",encoding="utf-8") as f:
        with open("vastus.txt","a",encoding="utf-8") as fv:
            while True:
                try:
                    mitu_kusi = int(input("Sisesta kui palju küsimused sa tahad lisa(ainult arv): "))
                    mitu_kus=mitu_kusi
                    break
                except ValueError:
                    print("Palun sisesta kehtiv arv.")
            for i in range(mitu_kus):
                while True:
                    uus_kus = input("Sisesta uus küsimus: ").strip()
                    uus_vas = input("Sisesta õige vastus: ").strip()
                    test_kus = input(f"Uus küsimus '{uus_kus}' koos vastusega '{uus_vas}'. Kas kõik on õige?(jah/ei): ")
                    if test_kus.lower() == "jah":
                        f.write("\n" + uus_kus)
                        fv.write("\n" + uus_vas)
                        print("Küsimus ja vastus on lisatud.")
                        break
                    elif test_kus.lower() == "ei":
                        print("Küsimus ja vastus ei ole lisatud. Proovi uuesti.")
                    else:
                        print("Palun sisesta jah või ei!")