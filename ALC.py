def problem_1(input):
    """Assumptions:
    
    1) The inputted value is greater than 0 (this is still checked for in the main method regardless).
    2) The inputted value is a number and not a string (this is still checked for).
    
    """
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
    return sum;
     
def problem_2(input):
    """Assumptions: 
    
    1) The string does not contain a singular word with both letters and numbers, e.g. ab478c.
    2) Punctuation is syntactically correct.
    3) Punctuation only includes semicolons, colons, commas, periods, exclamation marks, and question marks.
    
    """
    returned_string = ""
    punctuation_string = ".,!;?:"
    split_string = input.split()
    for string in split_string:
        try:
            int(string)
            returned_string += string + " "
        except:
            if len(string) == 1 and string in punctuation_string:
                returned_string += string + " "
            elif string[-1] in punctuation_string:
                try:
                    int(string[:-1])
                    returned_string += string + " "
                except:    
                    returned_string += string[1:-1] + string[0] + "ay" + string[-1] + " "
            elif len(string) > 1:
                returned_string += string[1:] + string[0] + "ay "
            else:
                returned_string += string + "ay "
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
            print("The sum is {}.".format(problem_1(input_1)))
        if int(input_problem) == 2:
            input_2 = input("Choose a string to translate to Pig Latin.\n")
            print(problem_2(input_2))
    except ValueError:
        print("Invalid input. Restarting.\n")
        main()
        
if __name__ == "__main__":
    main()