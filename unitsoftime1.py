# user input of duration of time
days = int(input("Enter a duration of time in days: "))
hours = int(input("Enter a duration of time in hours: "))
minutes = int(input("Enter a duration of time in minutes: "))
seconds = int(input("Enter a duration of time in seconds: "))

# converting days into seconds 
sec_d = days * 24 * 60 * 60 

# converting hours into seconds
sec_h = hours * 60 * 60 

# converting minutes into seconds 
sec_m = minutes * 60 
 
# calculation 
total_sec = sec_d + sec_h + sec_m + seconds 

#concatenation
print("The total amount of seconds in that duration of time is: " + str(total_sec) + " " + "seconds." )