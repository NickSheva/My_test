from sympy import isprime
def is_prime(d):
    return f'Это простое число' if isprime(d) else f'Это составное число'

d = 10
print(is_prime(d))