import random
from math import floor, sqrt


def ext_factors(x):
    prime_set = []
    prime_set_count = []
    fact = factors(x)
    for y in fact:
        if y not in prime_set:
            prime_set.append(y)
            prime_set_count.append(fact.count(y))
    return prime_set, prime_set_count


def factors(x: int) -> [int]:
    max_q = floor(sqrt(x))
    cur_q, step = 5, 2

    if x % 2 == 0:
        cur_q = 2
    elif x % 3 == 0:
        cur_q = 3
    else:
        while cur_q <= max_q:
            if x % cur_q == 0:
                break
            cur_q += step
            step = 6 - step

    if cur_q <= max_q:
        return [cur_q] + factors(x // cur_q)
    else:
        return [x]


def gen_generator(m: int) -> int:
    g = None

    if not is_prime(m):
        return g
    else:
        r = random.choice(range(1, m // 4))
        found = False
        while not found:
            g = 2 * r + 1
            if g < m and is_prime(g):
                found = True
            else:
                r += 1

    return g


def gen_prime(a, b):
    result_list = []
    for i in range(a, b):
        if is_prime(i):
            result_list.append(i)

    if len(result_list) == 0:
        raise IndexError("No prime number found between {} and {}".format(a, b))
    else:
        return random.choice(result_list)


# trivial algorithm to test conditions of an element
# being a generator of the group
def is_generator_simple(g: int, m: int) -> bool:
    if g >= m:
        return False
    elif not is_prime(m):
        return False
    elif is_prime(g):
        return True
    return False


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    max_q = floor(sqrt(x))
    cur_q, step = 5, 2

    while cur_q <= max_q:
        if x % cur_q == 0:
            return False
        cur_q += step
        step = 6 - step

    return True


def phi(primes):
    result = 1
    for i in range(len(primes[0])):
        result *= primes[0][i] ** (primes[1][i] - 1) * (primes[0][i] - 1)

    return result
