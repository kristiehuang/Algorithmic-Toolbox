# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)
#
# n = int(input())
# print(calc_fib(n))

def calc_fib2(n):
    array = [0 for x in range(n+1)]
    array[0] = 0
    if n >= 1:
        array[1] = 1
        for i in range(2, n+1):
            array[i] = array[i-2] + array[i-1]
    return array[n]

n = int(input())
print(calc_fib2(n))
