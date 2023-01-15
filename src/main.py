from itertools import product


def de_bruijn(k, n):
    alphabet = list(map(str, range(k)))

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return ''.join(alphabet[i] for i in sequence)


def check_solution(k, n, sol):
    """Check against the solution sol"""
    for p in product(''.join(map(str, range(k))), repeat=n):
        code = ''.join(p)
        if code not in sol:
            return False
    return True


ls = de_bruijn(10, 4)
ls += ls[:3]  # wrap around
print('Good solution?', check_solution(10, 4, ls))
