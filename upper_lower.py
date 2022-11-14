def word(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in w:
        if i.isupper():
           d["UPPER_CASE"]+=1
        elif i.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("upper case : ", d["UPPER_CASE"])
    print (" lower case : ", d["LOWER_CASE"])

word('AbCdEfGhIjKlMn')
