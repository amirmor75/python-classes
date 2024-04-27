# while(boolean):
#   do this as long as boolean==true

#  לולאת "כל עוד" היא מאפשרת לנו לרוץ כל עוד תנאי מסויים מתקיים.

# first explanation ex1
laps = 0
while (laps<5) :
    print(laps<5)                          
    print("now i'm in lap number {} ".format(laps))
    laps = laps+1
print(laps<5)
print("i finished the run")


# first explanation ex2 this while will never stop
# while True:
#     print("i'm hyped i'll never stop")
#     print("why you sont stop")