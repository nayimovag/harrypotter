list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list[2][2].append(7000)
print(list)

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
#["h", "i", "j"]
#list1[2][1][2].append("h", "i", "j")
list2=['h', 'i', 'j']
list1[2][1][2].extend(list2)
print(list1)