# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.


# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

#access
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#update
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#unpack
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits


#loop tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  

#join
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple1*3)