# ex : 
# writre a recursive function f  that computes the sum of the digits of the argument
# f(23)= 5
# f(1923)= 15


# איך נחשוב על הבעיה?
# ננסה להקטין קושי חישוב הדוגמהת כלומר במקום לחשב 
# כל 1953 ננסה לחשב מספר יותר קטן או קצר שמקרב אותנו לפתרון
# 1923 => 15
# ננסה להוסיף חישוב ביניים קל יותר 
# r_sum_digit(1923) => r_sum_digit(x) + y => 15
# עילאי הציע: r_sum_digit(1923) => r_sum_digit(19) + 23 => הבעיה היא ש 23 פוגע בנכונות החישוב
# r_sum_digit(1923) => r_sum_digit(192) + 3  => 
# => r_sum_digit(19) + 2  + 3 =>
# => r_sum_digit(1) + 9 + 2  + 3



def r_sum_digit(num):
    num_div = num%10
    if( num == 0 ):      # מקרה הבסיס
        return 0
    return num_div + r_sum_digit(num//10)    # קריאה רקורסיבית











#  while num > 0 : # we stop the loop when num=<0
#         sum_of_digits += num % 10
#         num = num//10     


    
    
##################

# home work!!!
# iterative solution with a for loop 

def iterative_sum_of_digits_for(num):  # iterative solution
    # we won't write the ifs because its less readable and redundant
    # (the code is true without it)
    # if (num < 10):
    #     return num
    # elif (num<100):
    #     return (num/10)+num%10
    plus = 0
    num = str(num)
    for i in range(len(num)):
        plus += int(num[i])
    return plus



   
##################      


# iterative solution with a while loop 

def iterative_sum_of_digits_while(num):  # iterative solution
    
    sum_of_digits = 0
    while num > 0 : # we stop the loop when num<10
        sum_of_digits += num % 10
        num = num//10           
   
    return sum_of_digits

if __name__ == '__main__':
    print(iterative_sum_of_digits_while(1923))

   
##################      
  