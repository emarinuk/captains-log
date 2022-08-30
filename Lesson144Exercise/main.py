from functools import reduce

# 1 Capitalize all the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def my_capitalize(item):
    return str(item).capitalize()


print(list(map(my_capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.reverse()

print(list(zip(my_numbers, my_strings)))

# ZTM Solution

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_over_fifty(item):
    return item > 50


print(list(filter(is_over_fifty, scores)))


# 4 Combine all the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


my_numbers.extend(scores)
print(reduce(accumulator, my_numbers, 0))


