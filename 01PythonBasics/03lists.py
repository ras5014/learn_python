l1 = [3, 5, 56, 23, "Harry"]

print(f"List : {l1}")
print(l1[0:3])

l1.remove("Harry")
print(f"Harry removed : {l1}")

print(f"Count of 23 : {l1.count(23)}")

l1.sort()
print(f"After sorting : {l1}")

l1.pop()
print(f"Pop : {l1}")

l1.append(45)
print(f"Appending 45 : {l1}")

l1.extend([45, 67, 89])
print(f"Extending : {l1}")

l1.clear()
print(f"Clearing : {l1}")
