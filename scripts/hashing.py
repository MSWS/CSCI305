def hash_linear(k, i, m = 11):
    return (h_prime(k) + i) % m

def hash_quadratic(k, i, m = 11, c1 = 1, c2 = 3):
    return (h_prime(k) + c1 * i + c2 * i ** 2) % m

def hash_double(k, i, m = 11):
    return (h_one(k) + i * h_two(k)) % m

def h_prime(k):
    return k

def h_one(k):
    return k

def h_two(k, m = 11):
    return 1 + (k % (m - 1))

array = [None] * 11
elements = [10, 22, 31, 4, 15, 28, 17, 88, 59]

for element in elements:
    i = 0
    while True:
        index = hash_double(element, i)
        if array[index] is None:
            array[index] = element
            break
        else:
            i += 1

print(array)