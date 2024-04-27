# lists introduction


thislist = ["milk", "bread", "eggs","milk"]
print(thislist)

# List items are ordered, changeable, and allow duplicate values.
# 1. מסודרת 
# 2. ניתנות לשינוי
# 3. ערכים זהים שחוזרים על עצמם
# List items are indexed, the first item has index [0], the second item has index [1] etc.




list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# A list with strings, integers and boolean values:
list4 = ["abc", 34, True, 40, "male"]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


thislist = list( ("apple", "banana", "cherry") )  # note the double round-brackets why??????
print(thislist)


for element in thislist: #()
    print(element)
    




















# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.