def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes(limit):
    primes = [2]
    for candidate in range(3, limit, 2):
        if is_prime(candidate):
            primes.append(candidate)
    return primes


def find_prime(n):
    counter = 1
    candidate_prime = 3
    while counter < n:
        if is_prime(candidate_prime):
            counter += 1
        candidate_prime += 2
    return candidate_prime - 2
