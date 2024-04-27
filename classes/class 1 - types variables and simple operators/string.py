#    01234567890
a = "Hello, World!"

first_char_of_string = a[0]
print(a[5])

# a = "Hello, World!10%$^"
print(len(a))

for x in "banana":
  print(x)
  
#special characters
# print("amir mor is having fun\why am i here")
# print("my site is in the address https\\amir\\mysite.com")
# print("\a")



txt = "The best things in life are free!"
print("free" in txt) # boolean

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
  
  
txt = "The best things in life are free!"
print( "expensive" not in txt) 
# print( "expensive" not in txt == not ("expensive"  in txt) )
# slicing
#    0123456789
b = "Hello, World!"
print(b[0:4])
# b[ start :  end : step ]
b = "Hello, World!"
print(b[:5]) # 0:5

b = "Hello, World!"
print(b[2:]) # til the end of the string

b = "Hello, World!"
print(b[-5:-2])

# #Upper Case
a = "Hello, World!"
print(a.upper())
# #Lower Case
a = "Hello, World!"
print(a.lower())

# #Remove Whitespace " " "\t" enter 
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# # Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello danihoware you?"
print(a.split("o")) # returns 








