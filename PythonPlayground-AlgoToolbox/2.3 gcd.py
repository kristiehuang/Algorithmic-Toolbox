# Uses python3
import sys

def gcd(a, b):
    current_gcd = 1
    first = a
    second = b
    while (second != 0):
        first, second = second, first % second
    current_gcd = first

    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
