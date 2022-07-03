# sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# convert the list into sets using set function
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
Set=set(basket)
print(Set)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
# unique letters in a
print(a)
# letters in a but not in b
print(a-b)
# letters in a or b or both
print(a or b)
# letters in both a and b
print(a & b)
#letters in a or b but not both
print(a^b)

print(r'c:\home\home')