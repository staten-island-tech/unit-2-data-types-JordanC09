#if traffic is east and its been 5 minutes, switch traffic to west and reset traffic.

#If traffic is west and its been 5 minutes, switch traffic to east and reset timer
#If timer is divisable by 5 then switch traffic
#If traffic equals east and timer is divisible by 5, then set traffic to west
#If traffic equals west and timer is divisable by 5, then set traffic to east

#Think of false as negative and true as positive

#Truth Chart


#WRONG
#def command(x,y):
  #  direction = input("Please put in the traffic direction. Eastbound or Westound ")
   # if direction === Eastbound:
    # x = True
     #   y = False
    #if# direction === Westrbound:
       # x = False
        #y = True
   
   
x = True
y = True

def truthy(x,y):
    if x == y:
        print("False")
    elif x != y:
        print("True")
truthy(x,y)


   
   
 #The if,else command can be used to check someting. Ex: if he doens't have enough 
 #money, say no, else give money