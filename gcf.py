x = int(input("Please input a number: "))
a = int(input("Please input another number: "))





mylist = []
hislist = []
def factors():
    z = 1

    for i in range(x):
        y = x % z
        if y == 0:
            mylist.append(z)
            
         
        
        z += 1


    c = 1
    for i in range(a):
        b = a % c
        if b == 0:
            hislist.append(c)
            
            
        c += 1
    



    if z - c > 0:
        sprang = z
    else:
        sprang = c
    
    
    start = 0




    for i in range(sprang):
        if mylist[start] == hislist[start]:
            print(start)
        start += 1
            
        


factors()

#copy factors in factors. print if y = 0 and y = other y
#a = x, b = y, c = z
#if y == 0 and z == c:
    #     print(z)

#and z == c:
#and y == 0 and c == z:

#C an have more Than 2 numbers for GCF

#Restart