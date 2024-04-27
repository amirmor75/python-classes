#ex1
# Write a Python program to sum all the items in a list
# [1 ,2 ,3, 4] --> 10

# solution
# lst = [1 ,2 ,3, 4]
# sum = 0

# for elem in lst:
#     sum = sum + elem 
# print (sum)


# ex2
# Write a Python program to multiply all the items in a list
# [1 ,2 ,3 ,4] --> 24

# solution
# lst = [1 ,2 ,3, 4]
# prod = 1
# for elem in lst:
#     prod = prod * elem 
# print (prod)


# ex3
# Write a Python program to get the largest number from a list
# [1 ,2 ,3 ,4, -1, 5, 3, 2] --> 5
# lst = [1 ,2 ,3 ,4, -1, 5, 3, 2]
# max = lst[0]
# for elem in lst:
#     if elem > max :
#         max = elem
# print(max)


# ex4 
# Write a Python program to get the smallest number from a list
# [1 ,2 ,3 ,4, -1, 5, 3, 2] --> -1
#solution
# lst = [1 ,2 ,3 ,4, -1, 5, 3, 2]
# min = lst[0]
# for elem in lst:
#     if elem < min :
#         min = elem
# print(min)


#ex5
            #  Write a Python program to count 
            #  the number of strings where the string 
            #  length is 2 or more and the first and last 
            #  character are same from a given list of strings
#   Sample List : ['abc', 'xyz', 'aba', '1221']
#   Expected Result : 2

# solution
# source = ['a','b','c']
# lst = ['abc', 'xyz', 'aba', '1221']
# count = 0 

# for elem in lst:
#     if len(elem) > 2:
#         if (elem[0] in source) and (elem[-1] in source):
#             count += 1
#     # print(count)
# print(count)
    
    
    
# old unsolved ex:
# כתוב תוכנית בה תקבל מספר מהמשתמש ותן לו את השם n. תדפיס את כל המספרים בין 0 עד n אשר n מתחלק בהם ללא שארית. 
# לדוגמה: 
# המשתמש מכניס 12. 
# יודפס למסך: 
# 1
# 2
# 3
# 4
# 6
# 12

n = int(input("give number\n"))

for i in range(1,n+1):
    if n%i == 0:
        print (i)












