some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicates2 = {item for item in some_list if some_list.count(item) > 1}
duplicates3 = [item for item in some_list if some_list.count(item) > 1]
duplicates4 = list({item for item in some_list if some_list.count(item) > 1})

print(duplicates2)  # result as a set to remove duplicates in duplicates :)
print(duplicates3)  # result as list shows all duplicates
print(duplicates4)  # printing set as a list
