from collections import Counter

def min_removals_to_good_sequence(N, a):
    freq = Counter(a)
    removals = 0
    
    for x, count in freq.items():
        if count > x:
            removals += count - x
        else:
            removals += count
    
    return removals

# Input
N = int(input())
a = list(map(int, input().split()))

# Output
print(min_removals_to_good_sequence(N, a))
