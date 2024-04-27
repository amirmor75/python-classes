
# n*(n-1)*....*1
def fact( x = 2 ):
    # print('x:'+ str(x))
    if(x == 1):           # בסיס הרקורסיה/ מקרה בסיס 
        return 1            
    return fact(x-1) * x  # קריאה רקורסיבית


if __name__ == '__main__':
    val = fact(3)
    
    print ( 'val: ' + str(val) )
    




