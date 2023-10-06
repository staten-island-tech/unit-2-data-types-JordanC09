x = int(input("Please input a number: "))
a = int(input("Please input another number: "))

mylist = []
common = []


if x - a > 0:
    first = x
else:
    first = a

maxxie = len(mylist)
short = maxxie - 1
part = 0

def factor1():
    z = 1
    for i in range(x):
        y = x % z
        if y == 0 and first == x:
            mylist.append(z)
        if y == 0 and first == a:
            for i in range(short):
                if z == mylist[part]:
                    common.append(z)
                    break
                part += 1
        z += 1


def factor2():
    c = 1
    for i in range(a):
        b = a % c
        if b == 0 and first == a:
            common.append(a)
        if b == 0 and first == x:
            for i in range(short):
                if c == mylist[part]:
                    common.append(c)
                    break
                part += 1
        c += 1


if first == x:
    factor1()
    factor2()
if first == a:
    factor2()
    factor1()


print(max(common)