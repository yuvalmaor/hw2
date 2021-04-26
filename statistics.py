import math
def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values) / 2)  # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index - 1]) / 2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values) / len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average) ** 2 for x in list_of_values])
    return squared_sum / (len(list_of_values) - 1)


def covariance(first_list_of_values, second_list_of_values):
    result = 0
    sum = 0
    mean_first = mean(first_list_of_values)
    mean_second = mean(second_list_of_values)
    for i in range(len(first_list_of_values)):
        
        sum = sum + (first_list_of_values[i] - mean_first) * (second_list_of_values[i] - mean_second)

    return sum/(len(first_list_of_values)-1)


def correlation(first_list_of_values, second_list_of_values):
    result = 0
    mycovariance=covariance(first_list_of_values, second_list_of_values)
    # Place your code here
    return float(covariance(first_list_of_values, second_list_of_values))/(math.sqrt(variance(first_list_of_values))*math.sqrt(variance(first_list_of_values)))
