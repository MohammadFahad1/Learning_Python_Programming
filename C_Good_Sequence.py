N = int(input())
a = list(map(int, input().split()))

freq = {key: 0 for key in a}

for i in a:
    freq[i] = freq[i] + 1

removeCount = 0

arr = set(a)

for i in arr:
    if freq[i] > i:
        removeCount += freq[i] - i
    elif freq[i] < i:
        removeCount = abs(removeCount) + freq[i]

print(removeCount)