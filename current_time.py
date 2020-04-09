import time

# splits the string (the function of time.asctime) into sections - the empty () means it is separated by each space 
datetimestring = time.asctime()
split = datetimestring.split()

# the number in the brackets is which section it is in - starts w/ 0 bc indexes start at 0, not 1 
day = split[0]
month = split[1] 
date = split[2] 
time = split[3] 
year = split[4]

print("Today's date: " + day + ", " + month + " " + date + ", " + year)
print("Current time (HH:MM:SS): " + time)