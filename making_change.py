import math

change = int(input("Enter the amount of change required in cents: "))

# number of toonies
toonie = math.floor(change / 200)
remainder1 = change - (toonie * 200)

# number of loonies
loonie = math.floor(remainder1 / 100)
remainder2 = remainder1 - (loonie * 100)

# number of quarters
quarter = math.floor(remainder2 / 25)
remainder3 = remainder2 - (quarter * 25)

# number of dimes
dimes = math.floor(remainder3 / 10)
remainder4 = remainder3 - (dimes * 10)

# number of nickels
nickels = math.floor(remainder4 / 5)
remainder5 = remainder4 - (nickels * 5)

# number of pennies
pennies = remainder5

print("Amount of Change needed: " + str(change))
print("The number of toonies is: " + str(toonie))
print("The number of loonies is: " + str(loonie))
print("The number of quarters is: " + str(quarter))
print("The number of dimes is: " + str(dimes))
print("The number of nickels is: " + str(nickels))
print("The number of pennies is: " + str(pennies))