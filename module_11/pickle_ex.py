# import pickle

# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# byte_string = pickle.dumps(some_data)
# unpacked = pickle.loads(byte_string)

# print(unpacked == some_data)  # True
# print(unpacked is some_data)  # False
# # print(byte_string)
# print(unpacked)

import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

file_name = 'data.bin'

with open(file_name, "wb") as fh:
    pickle.dump(some_data, fh)

with open(file_name, "rb") as fh:
    unpacked = pickle.load(fh)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False