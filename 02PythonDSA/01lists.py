sequence_list = list(range(10))
print(sequence_list)

list1 = [1, 3, 5, 'seven']
print(list1)

# append {O(1)}
list1.append(9)
print(list1)

# insert {O(n)}
list1.insert(0, 2)
print(list1)

# remove {O(n)} searche and removes
list1.remove("seven")
print(list1)

# This will give runtime error (Cause 0 doesn't exist in the code)
# list1.remove(0)
# print(list1)

# pop {O(1)} removes the last element
list1.pop()
print(list1)

# pop {O(n)} removes the element at the index
list1.pop(2)
print(list1)

# reverse {O(n)}
list1.reverse()
print(list1)
