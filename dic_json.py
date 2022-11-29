import json 
dictionary = {
 'fruit':{"Grapes": "10","color": "green"},
 'vegetable':{"chilli": "4","color": "red"},
}
result = json.dumps(dictionary, indent = 3)
print(result) 
