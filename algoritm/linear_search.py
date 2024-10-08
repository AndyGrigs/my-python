def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return arr[i]
   return -1

print(linear_search([5, 3, 8, 1, 4], 8))