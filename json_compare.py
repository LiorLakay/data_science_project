import json

# Read the contents of the two JSON files
with open('output.json', 'r') as f1, open('new_output.json', 'r') as f2:
    json1 = json.load(f1)
    json2 = json.load(f2)

# Extract the keys from each dictionary
keys1 = json1.keys()
keys2 = json2.keys()

# Compare the two lists of keys
if keys1 == keys2:
    with open("json_keys.txt", "w") as file:
        for key in keys1:
            file.write(key + "\n")
else:
    print("The keys in the two JSON files are different.")
