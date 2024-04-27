# accessing elements
#              0         1        2
thislist = ["apple", "banana", "cherry"]
print(thislist[0])

# get real size of list
print(len(thislist)) # 3 

# get last element of list
print(thislist[len(thislist)-1])

# Negative Indexing
print(thislist[-1])
# print(thislist[-4])  # error 

# # Range of Indexes - slicing
#               0                          -4  
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # includes first but excludes last
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
print(thislist[-4:])



# Check if Item Exists
thislist = ["milk", "bread", "eggs"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# Change Item Value

thislist = ["milk" ,"bread", "eggs"]
thislist[1] = "banana"
print(thislist)


# Append Items
thislist.append("orange") #  הוספה לסוף
print(thislist)


# Insert Items
thislist = ["milk" ,"bread", "eggs"]
thislist.insert(1, "sugar")
print(thislist)


# # Extend List.......
