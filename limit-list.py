n = int(input("Enter the size of list : "))

lst = list(map(int, input("Enter the elements:").split()))[:n]

print('The list is:', lst)
