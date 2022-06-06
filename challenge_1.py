
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
if __name__ == '__main__':
    get_input()

