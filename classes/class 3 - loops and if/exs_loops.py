import string
import random


# from last week:
# get a number from the user and print its אחדות ומאות
# remember //,%,/
# fix this like how we said (no if and ahadot is right)
number_in = int(input("give str pls\n"))
print ( "meot:" + str((number_in//100)%10) )    # 1342//100 => 13   %10 => 3
                                                # 1348392813//100 => 13483928%10 => 8
                                                # 13//100 => 0   %10 => 0
print("ahadot:" + str((number_in % 10 ))   ) # 642 => 2

print("alaphim: ??" + str((number_in//10**3)%10) ) # 124332 -> 124  -> 4 

#for today:

# while 
# rand()



# pseudo-random
# תדפיס מספרים בין 0-9 רנדומליים עד שיוצא 4 
# 1 5 4 exit

rnd_n = random.randint(0,9) # 3
# print(rnd_n)
while rnd_n!= 4:
    print(rnd_n)
    rnd_n = random.randint(0,9) # 4 
print(str(rnd_n) +'\nexit' ) # print(4)
##############################################################

# rnd_n = random.randint(0,9) # 3
# print(rnd_n)
# while rnd_n!= 4:
#     rnd_n = random.randint(0,9)
#     print(rnd_n)
#      # 4 
# print('exit' ) 



# Count the Number of matching characters in a pair of string
str1 = input("give str1\n")
str2 = input("give str2\n")
#str1 abale koko
#str2 yoyo kaka
# a-z -> 3
matching_chars= 0
for char in list(string.ascii_lowercase):
    if (char in str1) and (char in str2):
        matching_chars+=1
print(matching_chars)




