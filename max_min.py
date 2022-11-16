list1 = []
 
num = int(input("How many elements in list? :"))
 

for x in range(num):
  numbers = int(input('Enter number: '))
  list1.append(numbers)
 
print("Maximum element:", max(list1))
print("Minimum element  :", min(list1))
