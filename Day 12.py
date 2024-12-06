def is_prime(num):
    if num <= 1:
        return False  # 1 and numbers less than 1 are not prime
    if num == 2:
        return True  # 2 is a prime number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True