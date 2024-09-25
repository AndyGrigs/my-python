import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(arr+2)

arr1 = np.array([1, 2, 3, 79])
arr2 = np.array([4, 5, 6, 9000])
# print(arr1 + arr2) 

# print(np.sum(arr1))
# print(np.mean(arr1))


arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr3)

my_list = [1, 2, 3, 4, 5]
# print(my_list)

my_list.append(12)
my_list.insert(1, 100000)
my_list.insert(5, 1555500)
my_list.remove(1)
my_list.sort()

# print(my_list)

my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 100
del my_dict['age']
# print(my_dict)

my_set = set([1, 2, 3, 4, 5])
my_set.add(129)
my_set.remove(1)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}