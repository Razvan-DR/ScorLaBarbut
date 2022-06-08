def winner():  # A recursive function that takes the player name in checks it in the dictionary if found adds 1
    try:
        d[input('W : ')] += 1
    except Exception as e:  # Exception for wrong names or names that are not in the original dictionary
        print(f"NAME >>>  {e}   <<<< Is Not Available !!!")

    s = input('\nPres "n" for another turn : / Press "q" to finish the game : ')
    print(" ")
    if s == 'q':
        return d
    else:
        winner()


def sss(n):  # Function that evaluates the specific number and returns the correct string for the said relationship
    if n > 0:
        return("has to receive from")
    elif n < 0:
        return("has to give to ")
    else:
        return("has nothing to do with")


def schema(s, s1):  # Function that takes each key element(in this program is the name o a player) and established the relationship with the rest of the keys by comparing their values
    q = 0
    s2 = s1.copy()  # Makes a copy of the original list i can work on it
    s2.remove(s)
    for i in s2:

        # From the value of the first given key  deduct the value of the second given key and rase it with the stake to obtain the result which is the relationship between the said keys
        r = ((d[s]-d[i])*miza)

        print(f"{s} {sss(r)} {s2[q]}", end=" ")

        if abs(r) != 0:
            # If r is not 0 print "r $" , else do not print anything
            print(f"{abs(r)} $")
        else:
            print(" ")

        q += 1
    return(" ")


a = int(input('enter the nr of players : '))
miza = int(input('enter the stake : '))
d = {}

# Define a dictionary with {a} key-value pairs and takes the key as input and the value is set to zero
for i in range(a):
    d.update({input('player name : '): 0})

winner()

l = list(d.keys())  # Dictionary to list
i = 0
while i < len(l):
    print(schema(l[i], l))
    print(" ")
    i += 1
