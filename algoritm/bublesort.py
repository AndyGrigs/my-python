# Suggested code may be subject to a license. Learn more: ~LicenseLog:3919317440.
def bubble_sort(list_):
    n = len(list_)
    for i in range(n-1):
        for j in range(n-i-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_

print(bubble_sort([5, 200, 4, 600, 100, 3]))
