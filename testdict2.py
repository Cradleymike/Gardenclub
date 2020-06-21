# Experiment with using Dictionary to store the data and transfer to JSON to output to the file.

classes = {"number": 1, "description":"Large Onion", "voucher":[30,20,10,0,0,0],"money":[0,0,0,8,5,3],"section":"Vegetable" }


print(classes)


print(classes["description"])
print(classes["voucher"][0])

classes["money"][0] = 5

print(classes)





