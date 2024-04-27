import random


# random.random()
# 7 + 6 = 13
# plus(7,6) -> 13
# random() -> x   ( 0 < x < 1 )

for i in range(10):
    print(int(random.random()*100))




# shuffle()
# Shuffle list x in place, and return None.
lst = []
random.shuffle(lst)


# randrange()
# Choose a random item from range(start, stop[, step]).
# This fixes the problem with randint() which includes the endpoint; 
# in Python this is usually not what you want.
random.randrange(start=0,stop=20,step=1)
# [0,1,2,3,...,19]

# randint()
# Return random integer in range [a, b], including both end points.
random.randint(a=0,b=20)
# [0,1,2,3,4,..,20]

# 10+3
# plus(10,3)
# random.sample(lst, 10)
# Chooses k unique random elements from a population sequence or set.

# Repeated elements can be specified one at a time or with the optional counts parameter. For example:
    # sample(['red', 'blue'], counts=[4, 2], k=5)
# is equivalent to:
    # sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
lst = ['amir','kid','elay','kk','tho']
print(random.sample(lst, 2))







