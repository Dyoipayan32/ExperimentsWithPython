listItem = ["Bob", "Bharath", "Murthy", "Peter", "Murthy", "Bob"]
setItem = set(listItem)
# count = 0
# for i in setItem:
#     for j in listItem:
#         if i == j and str(i).lower().startswith("b"):
#             count += 1
#     if count > 0:
#         print("Name %s is present for %d times." % (i, count))
#         count = 0
#     else:
#         continue

dictItem = {}

for i in listItem:
    if i in dictItem and str(i).lower().startswith("b"):
        dictItem[i] += 1
    elif i not in dictItem and str(i).lower().startswith("b"):
        dictItem[i] = 1

print(dictItem)
