# deictionary 
data={
    "name":["Rohan","Husen","Mahesh","Dhananjay"],
    "rollNo":[1,2,3,4]
}
data["newcomponent"]=[11,22,33,44]
data["sets"]=(99,88,77)

#printing dictionary
#print(data)

#sorted dictioanry
print(sorted(data))

#check the element is present or not
print("Rohan" in  data["name"])
print((99,88,77) in data["sets"])
print(33 in data["newcomponent"])

# creating dictionary using dict method

df=dict([("name",["Rohan","bablu"]),("roll no",[6,7])])
print(df)

#dictionary comprensions
dictionary={
    x: x*3 for x in (2,4,6)
}
print(dictionary)

#when the keys the keys are string then sometimes it easier to declare using keyword argument
dff=dict(
    name=["Rohan","bablu"],
    game=['free fire',"fire"]
)

print(dff)