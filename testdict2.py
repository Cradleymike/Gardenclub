import json


# Experiment with using Dictionary to store the data and transfer to JSON to output to the file.



classes = { 1: {"description":"Large Onion", "voucher":[30,20,10,0,0,0],"money":[0,0,0,8,5,3],"section":"Vegetable" },
2 : {"description":"Longest Runner Bean","voucher":[0,0,0,0,0,0],"money":[1.00,0.75,0.50,0,0,0], "section":"Vegetable"}
}


print(classes)


print(classes[1]["description"])
print(classes[1]["voucher"][0])


print(classes)

classesfile = open("classfile.txt", "w")
json.dump(classes, classesfile)
classesfile.close()








