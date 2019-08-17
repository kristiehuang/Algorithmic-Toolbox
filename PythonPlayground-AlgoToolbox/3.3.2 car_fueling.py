# python3
import sys


def compute_min_refills(distance, tank, stops):

    refills = 0
    tankMiles = tank


    if distance <= tankMiles:
        refills = 0
    else:
        stop = -1
        while distance > tankMiles:
            nextStop = getNextStop(stop, tankMiles, stops)

            print("Stop at", nextStop)
            if nextStop < 0:
                break
            else:
                refills+=1
                tankMiles = stop + tank

    return refills

def getNextStop(_stop, _tankMiles, _stops):
    nextStop = -1;
    for x in _stops:
        if x <= _tankMiles and x > _stop:
            nextStop = x

    return nextStop

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
