#variables
moneY = float(input("Amount of money you have:"))
applePrice = float (input("Price of apple per piece:"))
maxNumberApples = int(moneY / applePrice)
ttlPayment = maxNumberApples * applePrice
changE =  moneY - ttlPayment 

#program
print("You can buy", f"{maxNumberApples}" , "and your change is", f"{changE:.2f} pesos")