import json
#Reading JSON

with open('data.json','r') as f:
    data=json.load(f)
    print(data)

    #Writing JSON

data= {'name': 'Alice', 'age': 30} 
with open('output.json', 'w') as f: 
    json.dump(data, f, indent=2)


#Binary Files

# Reading binary file

with open('image.png', 'rb') as f:
    binary_data= f.read()

# Writing binary file

with open('copy.png', 'wb') as f:
    f.write(binary_data)