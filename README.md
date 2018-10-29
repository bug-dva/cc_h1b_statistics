
# Insight h1b Statistics Code Challenge

## Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify **the occupations and states with the most number of approved H1B visas**. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data.]( https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis)But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years.

The goal of this project is to create a mechanism to analyze past years data, specifically calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications. The code need to be modular and reusable.

## Approach

### Prerequisites
[Python 3.6.5](https://www.python.org/downloads/release/python-365/)

### Step 0: Preparation
1. Review [**File Structure**](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis) for all past years' available data (from 2008 to 2018) and collect all column names for occupation, state and approval status. Save all possible names in according lists in **constant.py**.
2. Collect all possible descriptions for the approval status of "certified", including "CERTIFIED", "Certified", and "certified". Save into **constant.py**.

**Note: This script is designed to process data for past years,based on the 'File Structure' of the year. It can be used to process future data, if the data comes with proper column names.**

### Step 1: Process Raw Data for Needed Information
1. Read raw data header and search column indexes for case approval status, occupation, and work state
2. Process each line to extract the occupation and work state information for every certified case, and save the information into two dictionaries:
  * occupations_counts dictionary: 
    * key: occupation
    * value: count
  * states_counts dictionary:
    * key: state
    * value: count

### Step 2: Get the Top 10 Lists and Percentage
In this step, two helper functions are called:

1. `get_top_k(full_dict, k)`: Given an input dictionary with key-value pair as (string, integer) and an integer k, return a list of first k key-value pairs sorted by value in descending order. If values are the same, sort by key in alphabetical order.
2. `get_percentage(top_k_result, total_count)`: Given an input list of (element, count) pairs and an integer as totalCount, calculate the percentage for each element by calculating count/totalCount. Return a list of (element, count, percentage) tuples.

### Step 3: write result to output files in required format
In this step, for both top 10 occupations and top 10 states, one helper function is called to write the result into an output file:
1. `write_to_file(output_filename, file_header, input_list)`: Write given list of tuple to given output file path with given file_header

## Run Instructions
1. Put you input file in the input folder, name it as "h1b_input.csv"
2. Run below command to start the process  
```
$ ./run.sh
```
3. The results should be in the output folder:
  * top_10_occupations.txt - the file containing the information of top 10 occupations for certified visa applications
  * top_10_states.txt - the file containing the information of top 10 states for certified visa applications

