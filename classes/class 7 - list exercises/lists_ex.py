# iterate list indexes
string = "asdv t sdv fvzsdv jy as"
print (len(string))



# ex2 
# find the 2 biggest numbers in the list
# [1,2,5,4,8,6,2,9,5] --> [8,9]
lst = [1,2,5,4,8,6,2,9,5]

max = lst[0]
for elem in lst:
    if max < elem :
        max = elem
print(max)

under_max = lst[0]
for elem in lst:
    if  elem > under_max and elem < max:
        under_max = elem
print(under_max)



