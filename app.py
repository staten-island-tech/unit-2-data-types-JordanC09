list1 = [1,2,3,4]
list2 = [1,2,3,4,5]

x = len(list1)

part = 0
t = 1

for i in range(x):
    if t  == list1[part]:
        print("hi")
    part += 1

maxxie = len(list1)
print(maxxie - 1)