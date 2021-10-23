#variables
money = float(input("Amount of money you have:"))
applePrice = float (input("Price of apple per piece:"))     #apple price per piece
maxNumberApples = int(money / applePrice)                   #maximum number of apples
ttlPayment = maxNumberApples * applePrice                   #total payment for apples
change =  money - ttlPayment                                #change

#program
print("You can buy", f"{maxNumberApples}" , "and your change is", f"{change:.2f} pesos")