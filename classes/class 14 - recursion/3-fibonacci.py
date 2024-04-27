


# הבנת מקרה הבסיס ע"י האיברים הראשונים של הסדרה
# fib(1) = 1
# fib(2) = 1


# הבנת האיבר הכללי ע"י חישוב האיברים ומציאת התבנית
# fib(3) = fib(2) + fib (1)   =  1 + 1  = 2
# fib(4) = fib(3) + fib (2)   =  2 + 1  = 3
# fib(6) = fib(5)+fib(4)
# fib(i) = fib(i-1) + fib(i-2) 


def fib(i):
    if i == 1 or i == 2:        # מקרי הבסיס
        return 1
    return fib(i-1) + fib(i-2)  # קריאה רקורסיבית
    
if __name__ == '__main__':
    print(fib(10)) 
    
# תרגיל : 
# מה אם מקרה הבסיס לא יהיה עם i==2 ?
# עילאי הציע להוסיף -1 -2 
    
# הבנת מקרה הבסיס ע"י האיברים הראשונים של הסדרה
# fib(-2) = 1
# fib(-1) = 1
# fib(1) = 1

# מה קורה בפועל:
# fib(-2)=1
# fib(-1)=1
# fib(0) = fib(-1) + fib(-2) = 1 + 1 = 2 
# fib(1) = 1
# fib(2)= fib(1) + fib (0) = 3    
# fib(3) = 4
# fib(4) = 7

# (1,1,2,1,3,4,7)  # -> הסדרה שונה ממה שרצינו לקבל


# הבנת מקרה הבסיס ע"י האיברים הראשונים של הסדרה
# fib(-2) = 1
# fib(-1) = 1
# fib(0) = 1
# fib(1) = 1

# fib(2) = 2 
# (1,1,1,1,2,3,5,7)



# related exercises:
# מה יהיו 5 הערכים הראשונים של הסדרה שנובעת מהפונקציה הזאת
def fib_ex1(i):
    # x = ?                   # not 2 !
    if i == 1 : 
        return 2
    if i == 2 : 
        return 7
    return fib_ex1(i-1) + fib_ex1(i-2)


print('fib_ex2'+ str(list((fib_ex1(x) for x in range (1,6)))))


def fib_ex2(i):
    # x = ?                   # not 2 !
    if i == 1 or i == 2: 
        return 1
    return fib_ex2(i-1)*2 + fib_ex2(i-2)
(1,1,3,7)
print('fib_ex2' + str( list((fib_ex2(x) for x in range (1,6)))))




        
    