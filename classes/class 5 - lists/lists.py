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
    


x = ["apple", "banana", "cherry"]
x.insert(1, "orange")
print(x)



# EX3      0 1 2 3 4
my_list = [1,2,3,4,5]
#1
for i  in my_list:
    print(i ) 
#4
for i in range(len(my_list)):
    print(i)

print(range(5)) # 0 1 2 3 4
print(range(3,7)) # 3 4 5 6  
print(range(0,5,2)) # 0 2 4

print  (range(1,4))

my_list[:3] # [1,2,3]
my_list[1:4] # [2,3,4]
my_list[1:5:2] #  1 3    ->    [2,4]



a = '1 2'
# print(a * 2.5) # error 
print(a * 2) # '1 21 2' 

print(a * 0 == '') # true 
print( '' != ' ' ) # true 

print(a * -2 == '') # true
# print(a * 2.5) # error 



print(int(6 == 6.0) * 3 + 4 % 5)

print (type(6))
print (type(6.0))
print(6 == 6.0) # true

print(int(True))    # 1
print(int(False))   # 0
print(bool(1))      # True 
print(bool(7))      # True - any number but 0 or None
print(bool(0))      # False
print(bool(None))   # False


mytuple1 = (2,4,3)
mytuple3 = mytuple1 * 2
print(mytuple3)


s1 = {1, 2, 3, 4, 5}
s2 = {2, 4, 6}
print(type(s1 ^ s2))
print ({1,1,1}=={1})


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["model"]           # access
thisdict.get("model")       # access
thisdict["color"] = "red"   # adding element
thisdict.update({"color1": "red","color2": "yellow" })   # adding elemnt/s
thisdict["brand"] = "Honda" # change value
thisdict.update("brand","Ford") # change value


# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.3