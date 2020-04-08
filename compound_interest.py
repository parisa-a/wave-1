# input from the user 
money = input("Enter amount deposited into your savings account: ")

# convert amount into float (to allow for decimals in input)
money = float(money)
interest = float(0.04)

# create a function to output savings after x years, round to 2 d.p. and convert to str
def compoundinterest(money, years, interest):
    dollars = money * ((1 + interest) ** years)
    dollars_rounded = round(dollars, 2)
    dollars_str = str(dollars_rounded)
    return dollars_str

# calculate and print dollars per year
for years in range(1, 4):
    # use 4 in the range above b/c python stops one item before the end 
    ci = compoundinterest (money, years, interest)
    years = str(years)
    # concatenation 
    print("The money in the savings account after " + years + " year(s) is: " + ci + " " + "dollars.")