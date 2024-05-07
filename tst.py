def MergeSort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2 # Split list in half
        
        left = list_[:mid]
        right = list_[mid:]
        print("I'm before MergeSort")
        MergeSort(left)
        MergeSort(right)
        print("I'm after MergeSort")
        print(f"Left is {left}")
        print(f"Right is {right}")
        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list_[c] = left[a]
                a += 1
            else:
                list_[c] = right[b]
                b += 1
            c += 1
            
        while a < len(left):
            list_[c] = left[a]
            a += 1
            c += 1
            
        while b < len(right):
            list_[c] = right[b]
            b += 1
            c += 1
        print("Heeey") 
    return list_
            
p = [44, 16, 63, 7, 67, 21, 34, 45, 10]            

import pdb
pdb.set_trace()
print(MergeSort(p)) 