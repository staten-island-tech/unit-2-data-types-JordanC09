bill = float(input("Please enter the bill total "))
service = (input("Please enter if the sevice was bad, ok, good, or great "))
if service == "bad":
    tip = 0
if service == "ok":
    tip = 0.15
if service == "good":
    tip = 0.20
if service == "great":
    tip = 0.25

tips = int(bill * tip)
if tip == 0:
    print("There is no tip ")
else:
    print((tips),"is the tip ")

print((bill + tips),"is your total")