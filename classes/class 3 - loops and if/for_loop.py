# for i in (data): 
#   somthing to do in the loop
  
# range(start,end,step)
# range(end) => the default number for 'start' is 0 range(0,end,1)
# range(start,end)

# most basic example
for k in range(1,10,1): #(1,2,3,4,5,6,7,8,9)
    print(k)



# לולאת פור משמשת לריצה על מבנה נתונים מסויים 
# range אם נרצה לרוץ ממספר עד מספר נוכל להשתמש במבנה המוכר של 

for i in range(5): # (0,1,2,3,4)
    print(i)

# "אי אפשר לשנות את איי איך שבא לנו הלולאה "שולטת בו"
for i in range(5): # (0,1,2,3,4)
    print(i)
    i=10
# אפשר לכתוב את טווח המספרים ממש כמו שנרצה (זה לא יכלול את המספר האחרון)
for i in range(3,2*5): # (3,4,5,6,7,8,9)
    print(i)


for i in range(4,11,2): # (4,6,8,10)
    print(i)
    
for x in range(97,123) : #()
  print(chr(x))