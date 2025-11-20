# import random

# p1=input("siseta mida sa tahad kasutada (rock, paper, scissors) ")
# options=["rock", "paper", "scissors"]
# p2=random.choice(options)
# print(f"computer valis {p2}")
# if p1==p2:
#     print("tulemus on viik")
# elif (p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") or (p1=="scissors" and p2=="paper"):
#     print("sa võitsid!")
# else:
#     print("computer võitis!")

from ssl import Options
while True:
    Options=["rock", "paper", "scissors"]
    try:
        p1=input("sisesta mida sa tahad kasutada (rock, paper, scissors) ")
        break
    except:
        print("sisesta õige valik!")
while True:
    Options=["rock", "paper", "scissors"]
    try:
        p2=input("sisesta mida sa tahad kasutada (rock, paper, scissors) ")
        break
    except:
        print("sisesta õige valik!")
if p1==p2:
    print("tulemus on viik")
elif (p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") or (p1=="scissors" and p2=="paper"):
    print("esimene mängija võitis!")
elif (p2=="rock" and p1=="scissors") or (p2=="paper" and p1=="rock") or (p2=="scissors" and p1=="paper"):
    print("teine mängija võitis!")
else:
    print("sisesta õige valik!")