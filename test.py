def find_prime(n):
    prime = []
    for i in range(2, n + 1):
        test = []
        for j in range(2, round((n + 1) ** (1/2))):
            if i > j and i % j == 0:
                test.append(i)
        if i not in test:
                prime.append(i)
    return prime

print(find_prime(1000))
