# python3
import sys


def compute_min_refills(distance, tank, stops):

    refills = 0
    tankMiles = tank

    while distance > tankMiles:
        stop = -1
        for x in stops:
            if x <= tankMiles:
                stop = x
            else:
                break

        if stop < 0:
            refills = -1
            break
        else:
            refills+=1
            tankMiles = stop + tank

    return refills




if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
