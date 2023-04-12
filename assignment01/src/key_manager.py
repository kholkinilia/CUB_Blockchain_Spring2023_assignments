import primes
import random
import math


def extended_euclid(a, b):
    px, x = 1, 0
    py, y = 0, 1
    while b:
        q = a // b
        x, px = px - q * x, x
        y, py = py - q * y, y
        a, b = b, a % b
    return a, px, py


def modular_inverse(n, mod):
    g, x, y = extended_euclid(n, mod)
    if g != 1:
        raise RuntimeError('No modular inverse')
    return x % mod


KEY_DELIMITER = 'e'


def convert_to_key(lhs: int, rhs: int):
    return f'{lhs}{KEY_DELIMITER}{rhs}'


def is_valid_key(string):
    tokens = string.split(KEY_DELIMITER)
    return len(tokens) == 2 and tokens[0].isdigit() and tokens[1].isdigit()


def parse_key(string):
    if not is_valid_key(string):
        raise RuntimeError('The key is invalid.')
    tokens = string.split(KEY_DELIMITER)
    return int(tokens[0]), int(tokens[1])


def generate_keys(n_bits=1024):
    p = primes.generate_large_prime(n_bits)
    q = primes.generate_large_prime(n_bits)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    d = random.randint(2, phi_n - 1)
    while math.gcd(d, phi_n) != 1:
        d = random.randint(2, phi_n - 1)

    e = modular_inverse(d, phi_n)

    return convert_to_key(e, n), convert_to_key(d, n)


def read_key(key_type):
    while True:
        print(f'Please input {key_type} key:')
        key = input()
        if is_valid_key(key):
            break
        print('The key is invalid')
    return key


def input_key(key_type, key_filename=None):
    if key_filename:
        with open(key_filename, 'r') as file:
            key = file.readline()
        if is_valid_key(key):
            return key

        print('The key in the file is not valid.')
    return read_key(key_type)


def input_private_key(private_key_filename=None):
    return input_key('private', private_key_filename)


def input_public_key(public_key_filename=None):
    return input_key('public', public_key_filename)


def output_keys(private_key, public_key, public_key_filename=None, private_key_filename=None):
    try:
        with open(public_key_filename, 'w') as file:
            file.write(public_key)
    except (TypeError, FileNotFoundError):
        print(f'Public key:\n{public_key}')

    try:
        with open(private_key_filename, 'w') as file:
            file.write(private_key)
    except (TypeError, FileNotFoundError):
        print(f'Private key:\n{private_key}')
