'''
Extract Every Other Character
Given a string, use slicing to create a new string that includes every other character of the original string.
Example String: "abcdefg" Expected Output: "aceg"
'''

original = "abcdefg"

#new_original = original[0::2]
print(original[0::2])

'''Domain name extraction:
Given a full URL, extract just the domain name.
Example String: "https://www.example.com/page" Expected Output: "www.example.com"'''

url = "https://www.example.com/page"
cutStart = url[url.find("www"):]
cutEnd = cutStart[0:cutStart.find("/")]
print(cutEnd)



my_dict = {
    'Nested Things': [{'name', 'thing one'}, {'name', 'thing two'}]


contacts = {
    'andrew' : [{"name":"Andrew", "phone number " : "1234567890",  }]


}

nested_dict = {
'dict1': {'key1': 1, 'key2': 2, 'key3': 3},
'dict2': {'keyA': 'A', 'keyB': 'B', 'keyC': 'C'},
'dict3': {'subdict1': {'subkey1': 'value1'}, 'subdict2': {'subkey2':
'value2'}}
}
# Accessing elements
print("Accessing a nested element:", nested_dict['dict1']['key2'])
# Adding new elements
nested_dict['dict1']['key4'] = 4
# Modifying elements
nested_dict['dict2']['keyA'] = 'Alpha'
# Iterating over nested dictionary
for outer_key, inner_dict in nested_dict.items():
print(f"Outer key: {outer_key}")
for inner_key, value in inner_dict.items():
print(f" Inner key: {inner_key}, Value: {value}")
