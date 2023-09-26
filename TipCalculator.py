tippercent = float(input("Please enter the tip percentage as a decimal "))

subtotal = float(input("Please enter the subtotal "))

tip = int(tippercent * subtotal)

total = tip + subtotal
print("The tip is",(tip),)
print("Your total is",(total),)