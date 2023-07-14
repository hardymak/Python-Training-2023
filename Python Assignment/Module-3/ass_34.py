# Write a Python script to check if a given key already exists in a dictionary.


dic1 = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}

key = "key1"

if key in dic1:
    print("key exists")
else:
    print("key does not exists")