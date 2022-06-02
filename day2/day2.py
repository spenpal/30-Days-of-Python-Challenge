import random

def greatest_common_factor(x, y):
    factors_of_x = {i for i in range(1, x + 1) if x % i == 0}
    factors_of_y = {i for i in range(1, y + 1) if y % i == 0}
    gcf = max(factors_of_x & factors_of_y)
    return gcf

def least_common_multiple(x, y):
    gcf = greatest_common_factor(x, y)
    lcm = x * y // gcf
    return lcm

# Test Cases
for _ in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print(f"Least Common Multiple ({x}, {y}): {least_common_multiple(x, y)}")