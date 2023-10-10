"""n = int(input())
nums = []
for i in range(n):
    num = input()
    nums.append(num)


mp = {}
for num in nums:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1

sum = 0
for key, value in mp.items():
    key = int(key)
    if value < key:
        sum += value
    elif value > key:
        sum += (value - key)
print(sum)"""

n = int(input())
a = list(map(int, input().split()))

nums = {}

for i in a:
    if i in nums:
        nums[i] += 1
    else:
        nums[i] = 1

res = 0

for element, count in nums.items():
    if count > element:
        res += count - element
    elif count < element:
        res += count

print(res)
