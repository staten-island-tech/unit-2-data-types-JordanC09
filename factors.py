x = int(input("Please input a number: "))



def factors():
    z = 1

    for i in range(x):
        y = x % z
        if y == 0:
         print(z)
        
        z += 1
        

factors()

# divide by z, z increases eby 1 untill z equals x