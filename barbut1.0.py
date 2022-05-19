def winer():
    try:
        d[input('W : ')] += 1
    except Exception as e:
        print(f"NUMELE >>>  {e}   <<<< NU ESTE VALABIL !!!")

    s = input('Pres "n" for next turn : / Press "q" to finish the game : ')
    print(" ")
    if s == 'q':
        return d
    else:
        winer()


def sss(n):
    if n > 0:
        return("are de primit de la")
    elif n < 0:
        return("are de dat la")
    else:
        return("nu are treaba cu")


def schema(s, s1):
    q = 0
    s2 = s1.copy()
    s2.remove(s)
    for i in s2:

        r = ((d[s]-d[i])*miza)

        print(f"{s} {sss(r)} {s2[q]}", end=" ")
        if abs(r) != 0:
            print(f"{abs(r)} lei")
        else:
            print(" ")

        q += 1
    return(" ")


a = int(input('enter the nr of players : '))
miza = int(input('enter the stake : '))
d = {}

for i in range(a):
    d.update({input('player name : '): 0})

winer()

l = list(d.keys())  # Dictionary to list
i = 0
while i < len(l):
    print(schema(l[i], l))
    print(" ")
    i += 1
