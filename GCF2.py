x = int(input("Please input a number: "))
a = int(input("Please input another number: "))

mylist = []
common = []
z = 1



for i in range(x):
    y = x % z
    if y == 0 and x - a > 0:
        mylist.append(z)
        
            
         
        
    z += 1

maxxie = len(mylist)

short = maxxie - 1

c = 1
part = 0

for i in range(a):
    b = a % c
    if b == 0:
        for i in range(short):
            if c == mylist[part]:
                common.append(c)
                break
                
            
            
            part += 1
    
    c += 1


print(max(common))








#make fact5or code3 but instead of adding to my list it adds to gcf list if it equals a number in my list