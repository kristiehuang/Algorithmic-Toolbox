# python3
import sys


# def compute_min_refills(distance, tank, stops):
#     # write your code here
#     count_stops, i = 0, 0
#     while i < len(stops): #not out of stops
#         this_stop = stops[i]
#         second_closest_dist = -1
#         for index in range(i, len(stops)):
#             distance_next = distance between this and up stop if reachable else -1
#             second_closest_dist = max(second_closest_dist, distance_next)
#             if second_closest_dist == -1:
#                 return -1
#             elif second_closest_dist == distance_next: #IF NEXT STOP IS FARTHEST REACHABLE
#                 count_stops += 1
#                 i = index
#             else: #unsure if next stop farthest reachable
#                 distance -= 

#         if distance <= 0: #destination reached
#             return count_stops

#     return -1
    


def compute_min_refills(distance, tank, stops):

    count = 0
    i = 0
    wow = [0] + stops
    while i<=len(wow) and distance - wow[i] > tank and tank >= (wow[i+1] - wow[i]): #last stop willbe out of bounds and can reach next stop
        print("start here:", wow[i])
        if distance <= 0: #destination reachable
            return count
        else: #destination not reached yet
            farthest_feasible_index = i
            for index in range(i+1, len(wow)): #for index of all remaining stops
                if tank >= (wow[index] - wow[i]):  #if stop index is feasible
                    farthest_feasible_index = index

            i = farthest_feasible_index
            count += 1
            distance -= wow[i]
        print("am here now:", wow[i])

    if distance <= 0: #destination reachable
        return count 
    else:
        return -1 #cannot reach next stop.


    
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print("STOPS", stops)
    print(compute_min_refills(d, m, stops))
