# input of length and width 
length = input("Enter a length in feet: ")
width = input("Enter a width in feet: ")

# converting length and width to int
length = int(length)
width = int(width)

# calculate area 
area = length * width / 43560

# convert area to string 
area = str(area)

# concatenation
print ("The area of the field is: " + area + " " + "acres.") 