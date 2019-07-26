# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

#input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit_naive(n))
