# -------------------------------
# Date: 6th July 2022
# -------------------------------
# Assume an array of arbitrary length whose elements represent colors of the set blue (b), green (g) or red (r).
# Write an algorithm which returns the number of subsets in which the array can be split so that every subset
# contains equal color representations.
# Remark: The colors do not have to appear in equal order within the subsets.
# -------------------------------
# EX.1: Given the array r-r-b-b-g-g, the algorithm will     return 1
# since the array can be split into one subset of length 6 which contains 2r, 2b and 2g elements.
# EX.2: Given the array r-r-b-b-g, the algorithm will       return 0
# since no equal subsets can be found.
# EX.3: Given the array r-b-g-g-b-r, the algorithm will     return 3
# since array of length 6 itself features equal color representation. When splitting the array into two sections of
# length three, two equal subsets can be identified: r-b-g and g-b-r.
# -------------------------------
# inputs: r-g-b array of arbitrary length
# outputs: number of r-g-b subsets found
# -------------------------------

# TODO: input function
# INPUT FUNCTION
# Get an array only with rgb data.
# Help user to input correct data.
def input_rgb():
    allow_input = False
    while not allow_input:
        allowed_values = ['r','g','b']
        rgb_data = input("Enter rgb data: ")
        for x in rgb_data:
            if x not in allowed_values: allow_input = False
            else: allow_input = True
        print("Please input only r-g-b values (ex: rrggbb).")
    return rgb_data

# TODO: data process function
# PROCCESS FUNCTION
# get rgb data and calculate the number of r-g-b subsets
def process_rgb(rgb_data):
    subset_rgb = [0, 0, 0]
    for x in rgb_data:
        print(x)
        if x == 'r':
            subset_rgb[0] += 1
        if x == 'g':
            subset_rgb[1] += 1
        if x == 'b':
            subset_rgb[2] += 1

    return subset_rgb


# TODO: show results
print(process_rgb(input_rgb()))



