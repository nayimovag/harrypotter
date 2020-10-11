#Lists
#1.Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [i + j for i, j in zip(list1, list2)]

print(list3)

#2.Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]

sq=[number**2 for number in aList]

print(sq)

#3.Remove empty strings from the list of strings
names = ["Mike", "", "Emma", "Kelly", "", "Brad"]

while('' in names):
    names.remove("")

print(names)

#Tuples
#1.Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)

tuple3=tuple1
tuple1=tuple2
tuple2=tuple3

print(tuple1, tuple2)

#2.Copy element 33, 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:5]

print(tuple2)

#Sets
#1.Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set.intersection(set1, set2)

print(set3)