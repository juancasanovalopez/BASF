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

# TODO: input function
def get_input():
    # Obtain the data from user
    print("Please enter array data (spacebar will separate strings):")
    words = list(input("Enter variables: ").split())
    # process the data
    n = 0
    # separate words
    for word in words:
        print(words[n])
        # separe characters (named letter, as char is a reserved word)
        for letter in word:
            print(letter)
        # compare letter and store when a coincidence occurs

        n+1
    # show result


# TODO: data process function
# TODO: show results
if __name__ == '__main__':
    get_input()

