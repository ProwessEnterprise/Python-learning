test_list = ["Gorge", 3, "issabal", 8, "Bharathi", 10, "frank", 18, "madhu", 33, "chaitu", 40, "lahari", 44]
key_list = ["name", "number"]
n = len(test_list)
res = [{key_list[0]: test_list[i], key_list[1]: test_list[i + 1]}
for i in range(0, n,2)]
print("The constructed dictionary list : " , res)
