
def datori(dict):
    x = dict.get("w")
    n12, n13, n21, n23, n31, n32 = 0, 0, 0, 0, 0, 0

    if x == "player1":
        n31 = -n3
        n21 = -n3
        n12 = +n3
        n13 = +n3

    elif x == "player2":
        n32 = - n3
        n12 = -n3
        n21 = +n3
        n23 = +n3

    elif x == "player3":
        n23 = - n3
        n13 = - n3
        n31 = + n3
        n32 = + n3

    return (n12, n13, n21, n23, n31, n32)


def func():
    a = input("Player1  = ")
    b = input("Player2 = ")
    c = input("Player3 = ")

    dic = {a: "player1", b: "player2", c: "player3"}
    return list(datori(dic))


def schema1(l, n):
    if l[n] > 0:
        return print(f" are de recuperat {l[n]} lei ")
    elif l[n] < 0:
        return print(f" are de dat {l[n]} lei  ")
    else:
        return print("Nu are treaba cu ")


def schema(lista):
    print("Player1 : ")
    schema1(lista, 0)
    print("--> Player 2 ")
    schema1(lista, 1)
    print("--> Player 3 ")
    print("Player2 : ")
    schema1(lista, 2)
    print("--> Player 1 ")
    schema1(lista, 3)
    print("--> Player 3 ")
    print("Player3 : ")
    schema1(lista, 4)
    print("--> Player 1 ")
    schema1(lista, 5)
    print("--> Player 2 ")


s = 1
i = 0
list1 = [0, 0, 0, 0, 0, 0]
n1 = int(input("Numarul de ture = "))
n3 = int(input("Miza pe zar : "))


while i in range(n1):

    print(f"Turn {s}")
    list2 = func()
    sum_list = [a + b for a, b in zip(list1, list2)]
    list1 = sum_list

    i += 1
    s = s + 1
schema(list1)
