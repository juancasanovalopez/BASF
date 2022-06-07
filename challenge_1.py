# -------------------------------
# Date: 6th July 2022
# -------------------------------
# Given three ordered arrays of arbitrary length containing random capital letters, write an algorithm which
# returns the longest ordered array which all arrays share.
# -------------------------------
# EX.1: Given the sequence ADDB and CDDE and EDDF the longest shared array is DD.
# EX.2: Given the sequence UIBAZDBSIAHFB, PQACIZDBIBDLAG and QIDBCZDBKSHDVF, the longest shared
# array is ZDB.
# -------------------------------
# inputs: 3 ordered array of arbitrary length containing only capital letters
# outputs: longest ordered array which all arrays share
# -------------------------------

# INPUT FUNCTION
# Obtain n=3 ordered array of arbitrary length
# Containing only capital letters
def read_input_strings(n):
    strings = []
    for i in range(0,n):
        string = (input("Please enter array data, hit enter when finished: ")).upper()
        strings.append(string)
    return strings

# TODO: data process function
# get 1st element from 1st string and compare with 1st element of 2nd string
# get 1st element from 1st string and compare with 2nd element of 2nd string
# if they are equal then store element in temporary array
def process_(strings):
    n = len(strings)
    for j in range(0,n):

        for string in strings:
            print(list(string))

# TODO: show results
process_(read_input_strings(3))

