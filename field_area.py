# input of length and width 
length = input("Enter a length in feet: ")
width = input("Enter a width in feet: ")

# converting length and width to float (to allow for decimals in input)
length = float(length)
width = float(width)

# calculate area 
area = length * width / 43560

# convert area to string 
area = str(area)

# concatenation
print ("The area of the field is: " + area + " " + "acres.") 