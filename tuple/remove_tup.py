tup = [('b', 100), ('c', 200), ('c', 45),('d', 876), ('e', 75)]
result = []
for i in tup:
    if i[1] <= 100:
        result.append(i)

print(str(result))