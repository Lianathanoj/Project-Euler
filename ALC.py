def problem_1(input):
    multiples = {}
    count3 = 3;
    count5 = 5;
    sum = 0;
    # while count3 < input:
        # multiples[count3] = count3;
        # sum += count3;
        # count3 += 3
    # while count5 < input:        # increment this at the same time as count3, e.g. count3 + 3, count5 + 5, still check for dictionary though
        # if count5 not in multiples:    
            # multiples[count5] = count5;
            # sum += count5;
        # count5 += 5
    # print("The sum is {}.".format(sum))
    # return sum;
    
    # More efficient, only need one loop but more conditionals
    multiples = {}
    sum = 0
    count = 1
    while count * 5 < input or count * 3 < input:
        if count * 5 < input:
            multiples[count * 5] = count * 5
            sum += count * 5
        if count * 3 < input and count * 3 not in multiples:
            multiples[count * 3] = count * 3
            sum += count * 3
        count += 1
    print("The sum is {}.".format(sum))
    return sum;
    
"""Assumptions: 
    1) The string does not contain a singular word with both letters and numbers, e.g. ab478c.
    2) Punctuation is syntactically correct.
    3) Punctuation only includes semicolons, colons, commas, periods, exclamation marks, and question marks."""    
def problem_2(input):
    returned_string = ""
    punctuation_string = ".,!;?:"
    split_string = input.split() # " ", ";, !, ?, ., :"
    for string in split_string:
        try:
            int(string)
            returned_string += string + " "
        except: # check the last character in each word, if that character in predefined string of punctuation symbols.
            if len(string) == 1 and string in punctuation_string:
                returned_string += string + " "
            elif string[-1] in punctuation_string:
                try:
                    int(string[:-1])
                    returned_string += string + " "
                except:    
                    returned_string += string[1:-1] + string[0] + "ay" + string[-1] + " "
            elif len(string) > 1:
                returned_string += string[1:] + string[0] + "ay " # if string not punctuation or numbers, piglatinify and add to returned_string, otherwise just add.
            else: # if len(string) == 1:
                returned_string += string + "ay "
    print(returned_string)
    return returned_string
    
def main():
    input_problem = input("Which problem would you like to do to? Type 1 or 2:\n")
    try:
        if int(input_problem) == 1:
            try:
                input_1 = int(input("Choose a number that you want to find the sum of all multiples of 3 or 5 less than it.\n"))
                if (input_1) < 0:
                    print("Not a natural number.")
                    raise ValueError
            except ValueError:
                print("Not a valid number.")
                raise
            return problem_1(input_1)
        if int(input_problem) == 2:
            input_2 = input("Choose a string to translate to Pig Latin.\n")
            return problem_2(input_2)
    except ValueError:
        print("Invalid input. Restarting.\n")
        main()
        
if __name__ == "__main__":
    main()