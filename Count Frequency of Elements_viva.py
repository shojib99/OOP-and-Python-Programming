nums = [1, 2, 3, 2, 1, 4, 2, 6, 7]

freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

for k, v in freq.items():
    print(k, ":", v)
