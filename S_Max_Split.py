string = input()
count = 0
total = 0
start = 0
sString = []
for i, char in enumerate(string):
    if char == 'L':
        count+=1
    elif char == 'R':
        count-=1

    if count == 0:
        total+=1
        sString.append(string[start:i+1])
        start = i+1

print(total)
for subStr in sString:
    print(subStr)
    