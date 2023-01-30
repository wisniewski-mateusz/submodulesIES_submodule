def is_it_prime(n: int) -> bool:
    for i in range(2, n):
        if not n % i:
            return False
    return True