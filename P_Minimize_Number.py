n = int(input())
a = list(map(int, input().split()))

flag = 0
count = 0

while True:
    if flag == 1:
        break
    for i in range(n):
        if(a[i] % 2 == 0):
            a[i] //= 2
        else:
            flag = 1
            break
    count += 1

print(count-1)