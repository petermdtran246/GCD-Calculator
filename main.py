m, n = map(int, input('Enter 2 nos: ').split())
while m!=n:
    if m > n:
        m = m - n
    elif n > m:
        n = n - m
print(f'GCD is {m}')