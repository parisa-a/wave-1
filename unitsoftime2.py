import math

# user input of seconds 
seconds = int(input("Enter a duration of time in seconds: "))

# number of days 
days = math.floor(seconds / 24 / 60 / 60)
remainder1 = seconds - (days * 24 * 60 * 60)

# of hours 
hours = math.floor(remainder1 / 60 / 60)
remainder2 = remainder1 - (hours * 60 * 60)

# of minutes 
minutes = math.floor(remainder2 / 60)
sec = remainder2 - (minutes * 60)

# if..then..else to add leading 0 - if value is <10 it needs a leading zero
# Alternatively, use padding function called zfill() e.g. hours.zfill(2)
if hours < 10:
    hours = "0" + str(hours)
else:
    hours = str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)

if sec < 10:
    sec = "0" + str(sec)
else:
    sec = str(sec)

# convert days to string 
days = str(days)

# concatenation
print("The duration of time entered is equivalent to: " + days + ":" + hours + ":" + minutes + ":" + sec + ".")