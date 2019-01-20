M = list(range(10))
I = list(range(10))
T = list(range(10))
S = list(range(10))
lists = []
for m in M:
    for i in I:
        if i != m:
            for t in T:
                if t != i and t != m:
                    for s in S:
                        if s != i and s != m and s != t:
                            if (t*m+t) >= 10 and (m*t + i) <= 12 and (s**2 + t) <= 31:
                                lists.append(f'{t*m+t} {t*m+i} {s*s+t}')
lists = sorted(list(set(lists)))
print(lists)