from collections import Counter

N = int(input())
a = list(map(int, input().split()))

freq = Counter()

for i in a:
    freq[i] = freq[i] + 1

