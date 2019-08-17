# python3
import sys


def compute_min_refills(distance, tank, stops):

    # 100 miles
    # 30 tank
    # 4 stops -- 20, 50, 60, 80
    # 20, 50, 80
    #
    # 2 stops -- 20, 60


    refills = 0
    currentStop = 0

    n = len(stops)

    while currentStop <= n:

        lastStop = currentStop
        #print("current stop distance is",stops[currentStop])

        if currentStop + 1 < n:
            while (currentStop < n) and (stops[currentStop+1] - stops[lastStop]) <= tank:
                    currentStop += 1
                    #print("new stop distance is", stops[currentStop])
                    if currentStop + 1 == n:
                        break
                    #finding stop as forward as you can

        if currentStop == lastStop and stops[currentStop] + tank < distance: #if no possible stop is ahead
            return -1
        if currentStop <= n:
            refills += 1

        if stops[currentStop] + tank >= distance:
            refills +=1
            break

    # while stops[currentStop] < distance:
    #     lastStop = currentStop
    #     while (stops[lastStop] + tank) < distance and (stops[currentStop-1] - stops[lastStop]) <= tank:
    #             currentStop += 1
    #             #finding stop as forward as you can
    #
    #     if currentStop == lastStop: #if no possible stop is ahead
    #         refills = -1
    #     if stops[currentStop] < distance:
    #         refills += 1




    return refills





if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
