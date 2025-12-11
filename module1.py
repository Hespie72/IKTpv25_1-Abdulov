# 5.1
from importlib.metadata import diagnose


def float_kontroll(sisend:str)->float:
    """Lihtne Kalkulaator:
    + - Liihtmine
    - - Lahutamine
    * - Korrutamine
    / - jagamine
    Muul jahul tagastab "Tundmatu tehe"
    :param float a: esimene arv
    :param float b: teine arv
    :param str tehe: tehe,mis tuleb teha
    :return/rtype: tehte tulemus float või str
    """
    while True:
        try:
            arv=float(sisend)
            return arv      
        except ValueError:
            sisend=input("Palun siseta arv: ")

def int_kontroll(sisend:str)->int:
    """Kontrollib, kas sisestatud ad"""
    while True:
        try:
            arv=int(sisend)
            return arv      
        except ValueError:
            sisend=input("Palun siseta arv: ")

#1 
def arithmetic(a:float,b:float,tehe:str)->any:
    """Lihtne Kalkulaator:
    + - Liihtmine
    - - Lahutamine
    * - Korrutamine
    / - jagamine
    Muul jahul tagastab "Tundmatu tehe"
    :param float a: esimene arv
    :param float b: teine arv
    :param str tehe: tehe,mis tuleb teha
    :return/rtype: tehte tulemus float või str
    """
    if tehe in ["*", "/", "+", "-"]:
        if tehe=="/" and b==0:
            vastus= "Nulliga jagamine pole lubatud"
        else:
            vastus=eval(f"{a} {tehe} {b}") #tehe teostamine eval funktsiooniga
    else:
        vastus="Tundmatu tehe"
    return vastus
#2 
def is_year_leap(aasta:int)->bool:
    """Kontrolib, kas aasta on liigaasta
    :param int: aasta arvuna
    :return/rtype: True kui liigaasta, False kui tavaline aasta
    """
    if (aasta % 4 == 0 and aasta % 100 != 0):
        return True
    else:
        return False

#3
def square(külg:float)->any:
    """Arvutab ruudud: übermõõd, pindala ja diagoonali
    :param float külg: ruudu külge pikkus
    :return/rtype"""
    ümbermõõt = 4 * külg
    pindala = külg ** 2 #või külg * külg
    diagonaal = külg**0,5*2
    return ümbermõõt, pindala, diagonaal
#4
def season(kuu:int)->str:
    if kuu in [1, 2, 12]:
        return "talv"
    elif kuu in [3, 4, 5]:
        return "kevad"
    elif kuu in [6, 7, 8]:
        return "suvi"
    elif kuu in [9, 10, 11]:
        return "sügi"
    else:
        print("Siseta õige arv!")
#5
def bank(a, years):
    for _ in range(years):
        a *= 1.10
    return a
#6
def is_prime(n):
    if n < 2:
        print("Jagajad pole määratletud (arv pole algarv).")
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Jagajad:", i, "ja", n // i)
            return False

    return True
#7
def date(day, month, year):
    # Päev peab olema 1..31 ja kuu 1..12
    if month < 1 or month > 12 or day < 1 or day > 31:
        return False

    # Kuude päevad
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Liigaasta kontroll
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    return day <= days_in_month[month - 1]
#9
def average(numbers):
    if not numbers:
        return None 
    return sum(numbers) / len(numbers)
#10
def min_max(numbers):
    return (min(numbers), max(numbers))
