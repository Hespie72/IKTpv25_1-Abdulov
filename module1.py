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
    else:
        return "sügi"
    #5
    def bank(a:float,year:int)->float:
        inttress=0.1
