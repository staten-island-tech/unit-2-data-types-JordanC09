number1 = int(input("Input a number: "))
number2 = int(input("Input another number "))
mylist = []
number = 1
def gcf():
    if number1 > number2:
        number = number1
    else:
        number = number2
    for i in range(1, number+1):
        if number1 % i == 0 and number2 % i == 0:
            mylist.append(i)
    print(max(mylist))


gcf()

