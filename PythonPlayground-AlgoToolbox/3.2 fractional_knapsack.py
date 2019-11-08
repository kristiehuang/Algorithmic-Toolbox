# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    def highest_utility_helper(w, v):
        existing_max = 0.
        index = 0
        if (all(x == 0 for x in w)):
            return -1
        for i in range(len(w)):
            if (w[i] > 0) and (v[i] / w[i]) > existing_max:
                index = i
                existing_max = v[i] / w[i]
        return index

    while capacity > 0:
        #print(capacity, weights, values)
        i = highest_utility_helper(weights, values)
        #print("i is ", i)

        if i == -1:
            break
        elif (capacity > weights[i]):
            value += values[i]
            capacity -= weights[i]
            weights[i] = 0
        else:
            value += (capacity * values[i] / weights[i])
            weights[i] -= capacity
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
