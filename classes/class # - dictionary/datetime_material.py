from datetime import datetime
import time

now = datetime.now()
print('in raw foramt:')
print(now)
print ("Current date and time in a custon format we wrote: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


while 1:
    time.sleep(1)
    now = datetime.now()
    
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    





# The strftime() method returns a string representing the date, controlled by an explicit format string. The format codes used in this example are:

# %Y: year with century as a decimal number.
# %m: month as a zero-padded decimal number.
# %d: day of the month as a zero-padded decimal number.
# %H: hour (24-hour clock) as a zero-padded decimal number.
# %M: minute as a zero-padded decimal number.
# %S: second as a zero-padded decimal number.
