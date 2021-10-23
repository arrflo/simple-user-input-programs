# variables
appleS = int(input("How many apples do you want to buy?"))      #number of apples
orangeS = int(input("How many oranges do you want to buy?"))    #number of oranges
ttlApple = appleS * 20                                          #total price of apples
ttlOrange = orangeS * 25                                        #total price of oranges
ttlPrice = ttlApple + ttlOrange                                 #grandtotal

#program
print("The total amount is",f"{ttlPrice} pesos.")