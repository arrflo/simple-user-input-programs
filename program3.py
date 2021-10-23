#variables
moneY = float(input("Amount of money you have:"))
applePrice = float (input("Price of apple per piece:"))     #apple price per piece
maxNumberApples = int(moneY / applePrice)                   #maximum number of apples
ttlPayment = maxNumberApples * applePrice                   #total payment for apples
changE =  moneY - ttlPayment                                #change

#program
print("You can buy", f"{maxNumberApples}" , "and your change is", f"{changE:.2f} pesos")