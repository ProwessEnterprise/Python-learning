List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]

def Count(test_list):

empty_dict = {}
for i in test_list:

empty_dict[i] = empty_dict.get(i, 0) + 1
return empty_dict


print(Count(List1))
