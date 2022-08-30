# Square exercise
my_list = [5, 4, 3]

print(list(map(lambda item: item ** 2, my_list)))

# List sorting exercise

a = [(4, 3), (0, 2), (10, -1), (9, 9)]
a.sort(key=lambda item: item[1])
print(a)
