# sets - it contains the unique values and we can not update the values

sets={1,2,3,4,5,5,5}
print(sets)
print(type(sets))
sets.add(69)
print(sets)
print(len(sets))
sets.remove(5)
print(sets)
#pop it will delete any random element from the set and it will return which element is deleted
print(sets.pop())
print(len(sets))
#discard it will does not give key error if element is not present in the set
print(sets.discard(98))
#clear - it will clear the set
sets.clear()
print(sets)
