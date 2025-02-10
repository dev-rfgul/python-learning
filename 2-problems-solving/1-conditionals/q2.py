age=int(input("enter your age "))
day=input("enter the day ")
ticket_price=0
print(age)
if(age<=18):
    if(day=="wednesday"):
        ticket_price=8
        discount=0.02*ticket_price
        ticket_price=ticket_price-discount
        print("you are kid and you got 2 percent off so ticket price would be: ", ticket_price)
    else:
        ticket_price=8
        print("you are kid so ticket price would be: ", ticket_price)
else:
    if(day=="wednesday"):
        
        ticket_price=12
        discount=0.02*ticket_price
        ticket_price=ticket_price-discount
        print("you are adult and got 2percent off so ticket price would be: ", ticket_price)
    else:
        print("you are adult so ticket price would be: ", ticket_price)
        
