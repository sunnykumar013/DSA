import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_numbers(lst):
    result = []
    for num in lst:
        root = int(math.sqrt(num))
        if root**2 == num:
            base = int(math.sqrt(root))
            if is_prime(base):
                result.append(num)
    return result



lst = [16, 8, 27, 81, 256, 125, 243, 1024, 36, 64]
res = find_numbers(lst)
print(res)