list1 = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
 
K = 2
 
extra = []
for i in list1:

    freq = list1.count(i)

    if freq > K and i not in extra:
        extra.append(i)

print("after freq:",extra)
