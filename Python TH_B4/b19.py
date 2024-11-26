def sieve_of_eratosthenes(n):
    is_prime = [True] * n
    p = 2
    while p * p < n:
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if is_prime[p]]
    return prime_numbers
primes_less_than_1_million = sieve_of_eratosthenes(1_000_000)
P = tuple(primes_less_than_1_million)
print("Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu:")
print(P)
