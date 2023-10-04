x = int(input("Please input a number: "))
a = int(input("Please input another number: "))





mylist = []
hislist = []


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
    
long = len(hislist)
loong = len(mylist)

if long - loong > 0:
    par = loong
else:
    par = long


            
def gcf():
    number = 0
    
    for i in range(par):
        if mylist[number] == hislist[number]:
            print(mylist[number])

        number += 1
    print(number)
    print(mylist)
    print(hislist)
    
gcf()


#for i in range(srang):
#        if list1[start] == list2[start]:
#           print(start)
#        start += 1




#copy factors in factors. print if y = 0 and y = other y
#a = x, b = y, c = z
#if y == 0 and z == c:
    #     print(z)

#and z == c:
#and y == 0 and c == z:

#C an have more Than 2 numbers for GCF

#Restart