# writing split for string program


my_object = input("give string\n")
delimiter= input("give delimiter\n")
#### variables
lst = []
start_of_word = 0 
####
for i in range(len(my_object)):
    if my_object[i] == delimiter:
        word = my_object[start_of_word:i]
        lst.append(word)
        start_of_word = i+1
word = my_object[start_of_word:]
lst.append(word)


print(lst)