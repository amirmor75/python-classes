import random

# random.shuffle(lst)
# random.random()
# random.randrange(start,stop,step)
# random.sample(lst,k)


# ex1
# Generate 3 random integers between 100 and 999 which is divisible by 5
# sol:
# for i in range(0, 3):
#     print(random.randrange(100, 1000, 5))

# ex2
# Random Lottery Pick.
# Generate 100 random lottery tickets
# and pick two lucky tickets from it as a winner.
# sol:

lst = [random.randint(0, 10000) for _ in range(100)]
print(lst)
winners = random.sample(population=sorted(lst), k=2)
print("winners are" + str(winners))


# random.shuffle(lst)
# random.random()
# random.randrange(start,stop,step)
# random.sample(lst,k)

# ex3
# 7
# 6
# 5
# 4     X  X  X
# 3
# 2           X
# 1           X
# 0  1  2  3  4  5  6  7

sample1 = [(2, 4), (3, 4), (4, 4)]
sample2 = [(4, 1), (4, 2)]
# ex3
# generate a random point of 2d in a 7X7 grid
x, y = random.randint(0, 7), random.randint(0, 7)
random_p = (x, y)


# lst = [x, y]
# lst.append(3)
# random_p[0] = 1
# print(random_p)
# print(lst)
