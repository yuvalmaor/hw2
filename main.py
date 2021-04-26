from statistics import median, mean, variance, correlation, covariance
import csv
import numpy


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    file_path = './winequality.csv'
    data = load_data(file_path)
    print("corra")
    # print(correlation([1,2,4,5,8],[5,20,40,80,100]))
    # print(variance([1,2,4,5,8])**0.5)
    # print(variance([5,20,40,80,100])**0.5)
    print(correlation(data["free sulfur dioxide"], data["total sulfur dioxide"]))
    print(numpy.correlate(data["free sulfur dioxide"], data["total sulfur dioxide"]))
    # print(correlation(data["total sulfur dioxide"]))

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {}, Std: {:.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values) ** 0.5))

    # here you should compute correlations. Be careful, pair should be sorted before printing
    strongest_pair = ("aaa", "bbb")
    high_correlation = -0.9
    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {}'.format(strongest_pair[0], strongest_pair[1], high_correlation))

    weakest_pair = ("free sulfur dioxide", "total sulfur dioxide")
    low_correlation = 0.1
    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments

    #for feature_name1, list_of_values1 in sorted(data.items()):
     #   for feature_name2, list_of_values2 in sorted(data.items()):



if __name__ == '__main__':
    run_analysis()
