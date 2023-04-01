buffer = []
notUniq = []
for i in range(0, 3):
    askInfo = input("Enter some words: ").split(", ")
    buffer.append(askInfo)
    for items in askInfo:
        if askInfo.count(items) > 1:
            notUniq.append(items)
print(buffer)
print(notUniq)

# a = input("Enter: ").split(", ")
# buffer = []
# for x in a:
#     if a.count(x) > 1:
#         buffer.append(x)
# print(buffer)
