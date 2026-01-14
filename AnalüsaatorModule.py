from codecs import ignore_errors
from copy import deepcopy
import os
import glob

def leia_projektifailid():
    laiend = input("Sisesta faililaiend (nt py või txt): ")
    failid = glob.glob("*." + laiend) 
    return failid
def analuusi_faili_sisu():
    failitee = input("Sisesta faili nimi: ")
    kokku = 0
    todo = 0
    fixme = 0
    tyhjad = 0
    with open(failitee, "r", encoding="UTF-8", errors="ignore") as f:
        for rida in f:
            kokku += 1
            if rida.strip() =="":
                tyhjad += 1
            todo += rida.count("TODO")
            fixme += rida.count("FIXME")
    return {
        "fail": failitee,
        "read_kokku": kokku,
        "tyhjad_read": tyhjad,
        "TODO": todo,
        "FIXME": fixme
}
def loo_raporti_kataloog():
    nimi = input("Sisesta raporti kataloogi nimi: ")

    if not os.path.exists(nimi):
        os.mkdir(nimi)

    return nimi


def leia_failid_algustahega():
    taht = input("Sisesta algustäht: ")
    failid = glob.glob(taht + "*.*")
    return failid
