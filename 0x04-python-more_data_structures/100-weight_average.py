#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = 0
    weighted_sum = 0

    for score, weight in my_list:
        total_weight += weight
        weighted_sum += score * weight

    if total_weight == 0:
        return 0

    return weighted_sum / total_weight
