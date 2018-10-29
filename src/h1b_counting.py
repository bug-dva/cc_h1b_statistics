from constants import ColumnNameList, CaseStatusList, OutputFileHeader
import sys
from csv import reader


def h1b_counting(input_filename, top_10_occupation_output_filename, top_10_state_output_filename):
    # read csv file and get column names
    with open(input_filename) as raw_file:
        raw_file_handle = reader(raw_file, delimiter=';')
        header = next(raw_file_handle)

        # get occupation, state and status column index

        occupation_index, state_index, status_index = None, None, None
        for index, column_name in enumerate(header):
            if column_name in ColumnNameList.SOC_NAME_COLUMN_NAME_LIST:
                occupation_index = index
            elif column_name in ColumnNameList.STATE_COLUMN_NAME_LIST:
                state_index = index
            elif column_name in ColumnNameList.STATUS_COLUMN_NAME_LIST:
                status_index = index

        # check if all indexes are found, if not, report error and exit
        if not (occupation_index and state_index and status_index):
            print('data not found, please check input file header')
            return

        # process each line and save occupation counts and state counts into two dictionaries
        certified_case_sum = 0
        occupations_counts = {}
        states_counts = {}

        for line in raw_file_handle:
            case_status = line[status_index]
            if case_status in CaseStatusList.CERTIFIED_CASE_STATUS_LIST:
                certified_case_sum += 1
                occupation = line[occupation_index].replace('\"', '')
                state = line[state_index]
                occupations_counts[occupation] = occupations_counts.get(occupation, 0) + 1
                states_counts[state] = states_counts.get(state, 0) + 1

        print(str(certified_case_sum) + ' certified cases have been processed')

        # call function get_top_k() to get the top 10 occupations and states

        top_10_occupations = get_top_k(occupations_counts, 10)
        top_10_states = get_top_k(states_counts, 10)

        # get top_K result with percentage

        top_10_occupations_w_percentage = get_percentage(top_10_occupations, certified_case_sum)
        top_10_states_w_percentage = get_percentage(top_10_states, certified_case_sum)

        # output to files
        print('Got top 10 results, start producing output files')

        write_to_file(top_10_occupation_output_filename, OutputFileHeader.TOP_10_OCCUPATION,
                      top_10_occupations_w_percentage)
        write_to_file(top_10_state_output_filename, OutputFileHeader.TOP_10_STATE, top_10_states_w_percentage)

        # Completed
        print('Job Completed. Please check output folder for results.')


def get_top_k(full_dict, k):
    """
    Given an input dictionary with key-value pair as (string, integer) and an integer k,
    return a list of first k key-value pairs sorted by value in descending order.
    If values are the same, sort by key in alphabetical order.

    :param full_dict: dictionary with key-value pair as (string, integer)
    :param k: an integer specifying the max size of returned list
    :return: a list of first k key-value pairs sorted by value in descending order
    """
    top_k_result = sorted(full_dict.items(), key=lambda item: (-item[1], item[0]))[:k]
    return top_k_result


def get_percentage(top_k_result, total_count):
    """
    Given an input list of (element,count) pairs and an integer as totalCount, calculate the percentage for each
    element by calculating count/totalCount
    Return a list of (element,count, percentage)

    :param top_k_result: a list of (element, count) pairs
    :param total_count: an integer, being the denominator when calculating the percentage
    :return: a list of (element, count, percentage)
    """
    result_with_percentage = []
    for element, count in top_k_result:
        ele_percentage = float(count / total_count)
        formatted_percentage = '{:.1%}'.format(ele_percentage)
        result_with_percentage.append((element, count, formatted_percentage))
    return result_with_percentage


def write_to_file(output_filename, file_header, input_list):
    """
    Write given list of tuple to given output file path with given file_header

    :param output_filename: name and path of output_file, if exist, overwrite
    :param file_header: header of output file, will be the first line
    :param input_list: a list of tuple, each tuple will be presented in a line joined by ';'
    :return:
    """
    output_file = open(output_filename, 'w')
    output_file.write(file_header + '\n')
    output_list = [';'.join(map(str, tup)) for tup in input_list]
    for output_line in output_list:
        output_file.write(output_line + '\n')
    output_file.close()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Insufficient arguments, please provide the arguments in the format of [input_filename] '
              '[top_10_occupation_output_filename] [top_10_state_output_filename]')
        exit(1)

    h1b_counting(sys.argv[1], sys.argv[2], sys.argv[3])
