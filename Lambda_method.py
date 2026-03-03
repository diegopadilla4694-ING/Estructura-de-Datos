list_1 = [x for x in range(5)]                   
print(list_1)
list_2 = list(map(lambda x: 2 ** x, list_1))        #The map() method is used here
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()