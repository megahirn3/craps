import random as r
last_throw = 0
def wurfeln():
    global summe
    input("willst du würflen? ENTER=JA, CTRL=NEIN")
    wurfel1 = r.randint(1,6)
    print(f"würfel1 ist {wurfel1}")
    wurfel2 = r.randint(1,6)
    print(f"würfel2 ist {wurfel2}")
    summe = wurfel1 + wurfel2
    print(f"die Augensumme der würfel ist {summe}")
    

def loserloop():
    while True:
        if summe == last_throw:
            print("glück gehabt du idiot3")
            break
        elif summe == 11:
            print("glück gehabt du idiot4")
            break
        elif summe == 2 or 3 or 12 or 7:
            print("hast verloren dummkopf5")
            break
        else:
            last_throw == summe
            wurfeln()
            pass

        

if wurfeln() == 7 or 11:
    print("glück gehabt du idiot1")
elif wurfeln == 2 or 3 or 12:
    print("du hast verloren, loser2")
else:
    loserloop()