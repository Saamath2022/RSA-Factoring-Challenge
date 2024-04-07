#!/usr/bin/python3
import sys
import random


def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == -1:
                break
        else:
            return False
    return True


def is_prime(n):
    return miller_rabin(n)


def factorize_rsa(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
