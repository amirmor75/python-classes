# ex1:
#       Write a Python program to get a string from a given string where all occurrences 
#       of its first char have been changed to '$', except the first char itself
# Sample String : 'restart'
# Expected Result : 'resta$t'

# solution
# txt = input("give me a string\n")
# first_char = txt[0]
# txt = txt[1:].replace(first_char,'$')
# txt = first_char + txt
# print(txt)


# ex2:
#       Write a Python program to get a single 
#       string from two given strings, separated by a space and swap the first two characters of each string
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

#solution
# a = input("give me a string\n")
# b = input("give me a string\n")
# first_pair_a =    a[0:2]
# first_pair_b =    b[0:2]
# a = first_pair_b + a[2:]
# b = first_pair_a + b[2:]
# result = a + " " + b
# print( result)


# ex3:
#       Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#       If the given string already ends with 'ing' then add 'ly' instead.
#       If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# solution
# txt = input("give me a string\n")
# if len(txt) >= 3 : 
#     if txt[-3:] == 'ing':
#         result = txt + 'ly'
#     else: 
#         result = txt + 'ing'
# else: 
#     result = txt 
# print(result)
 


#ex4:
#       Write a program to split a given string on hyphens (-) and display each substring.
# str1 = Emma-is-a-data-scientist
# Displaying each substring
# Emma
# is
# a
# data
# scientist

#solution
txt = input("give me a string\n")
last = 0
for i in range(len(txt)): # 0  1 2...... len(txt)
    if txt[i] == '-':
        print(txt[last:i]) 
        last = i+1
        


txt = "a very beautiful dog"

# for x in txt:
#     x
    
for i in range(len(txt)):
    print(i)
    print(txt[i])
    
# for i in range(txt):
#     print(i)



# 0123456789
# Emma-is-a-data-scientist
txt[5]