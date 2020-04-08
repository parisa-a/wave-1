import math
math.pi

# input of radius and height 
radius = input("Enter a radius in centimeters: ")
height = input("Enter a height in centimeters: ")

# converting radius and height to float (to allow for decimals in input)
radius = float(radius)
height = float(height)

# calculate volume 
volume = float(math.pi * radius ** 2 * height)

# limit to one decimal place 
volume_rounded = round(volume, 1)

# convert volume_rounded to str
volume_rounded = str(volume_rounded)

# concatenation
print("The volume of the cylinder is: " + volume_rounded + " " + "centimeters cubed")