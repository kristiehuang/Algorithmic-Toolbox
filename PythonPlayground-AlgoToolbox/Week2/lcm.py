# Uses python3
import sys
#from gcd import gcd

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(lcm_naive(a, b))
def gcd(a, b):
    current_gcd = 1
    first = a
    second = b
    while (second != 0):
        first, second = second, first % second
    current_gcd = first

    return current_gcd


def lcm(a, b):
    current_gcd = gcd(a, b)

    return a*b / current_gcd


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
