# variables
apples = int(input("How many apples do you want to buy?"))      #number of apples
oranges = int(input("How many oranges do you want to buy?"))    #number of oranges
ttlApple = apples * 20                                          #total price of apples
ttlOrange = oranges * 25                                        #total price of oranges
ttlPrice = ttlApple + ttlOrange                                 #grandtotal

#program
print("The total amount is",f"{ttlPrice} pesos.")