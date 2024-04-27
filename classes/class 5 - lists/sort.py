# #sorting
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)


lst = [ 2,5,4,6,8,-1,-6,8,60,10,50,60,30]
lst.sort()
print(lst)

# finding highest value in list
max = lst[0]
for elem in lst:
    if elem > max :
        max = elem
print(max)