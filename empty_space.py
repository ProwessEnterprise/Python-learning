list1 = ['chaitu', ' ', 'mark', '', '         ', 'robert']

list2 = []
for i in list1:
    if i.strip():
        list2.append(i)

print(str(list2))
