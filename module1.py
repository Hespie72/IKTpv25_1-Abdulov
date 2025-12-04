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