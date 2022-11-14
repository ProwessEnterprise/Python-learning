def merge(dic1, dic2, dic3):
for d in (dic1, dic2, dic3):
dic1.update(d)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(merge(dic1,dic2,dic3))
print(dic1)
