input = int(input())

first3 = input // 1000000
two = input // 10000 % 100
last4 = input % 10000

print(f'{first3}-{two}-{last4}')