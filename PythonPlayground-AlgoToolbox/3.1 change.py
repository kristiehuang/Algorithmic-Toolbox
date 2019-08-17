# Uses python3
import sys

def get_change(m):
    #write your code here

    tens = int(m/10)
    remTen = m % 10
    fives = int(remTen / 5)
    remFives = int(remTen % 5)

    change = tens + fives + remFives
    return change

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
