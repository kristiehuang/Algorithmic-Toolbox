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
    nextStop = index 0
    currentStop = index 0
    n = 4 total stops before final
    if nextStop == 0: #if very first stop
        if stops[nextStop] > tank: #if distance from first stop is too far
            return -1
        else:
            nextStop +=1
    else: #if first stop is not next stop
        while currentStop < n  #destination not reached, last stop just went to, get ready to find next step
            while stops[nextStop + 1] - stops[currentStop] <= tank and stops[nextStop] + tank < distance: #while enough gas for NEXT stop + NEXT stop is not farther than goal
                nextStop += 1

            currentStop = nextStop
            refills += 1


    return refills





    refills = 0
    currentStop = 0
    n = len(stops)

    while currentStop < n:

        lastStop = currentStop
        #print("current stop distance is",stops[currentStop])

        while (currentStop < n) and (stops[currentStop] - stops[lastStop]) <= tank:
                    currentStop += 1
                    #print("new stop distance is", stops[currentStop])
                    # if currentStop == n:
                    #     break
                    #finding stop as forward as you can

        if currentStop == lastStop:
            return -1
        if currentStop < n:
            refills += 1


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
