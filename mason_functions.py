

#1
#is_two defines a single parameter, x (whatever user input), and determines whether or not that input is
#two (it returns a Boolean value of True or False)

def is_two(x):
    #check to make sure the input is explicitly the integer two or the numerical string for two
    if x == 2 or x == '2': 
        #return bool True if it is two
        return True
    else:
        #return bool False if not
        return False

is_two('2')




#2
#is_vowel defines a single parameter, x (assuming it is a string of one character), and determines whether the input 
#is a vowel or not (returns Boolean True or False)
def is_vowel(x):
    #check to see if the input (lowercased just in case input is uppercased) is in this complete string of vowels
    if x.lower() in 'aeiou':
        #return bool True if it's in the string
        return True
    else:
        #return bool False if not
        return False
    
is_vowel('A')




#3
#is_consonant defines a single parameter, x (string of one character), and returns a Boolean True or False
def is_consonant(x):
    #check to see if the input character is in this complete list of consonants
    if x.lower() in 'bcdfghjklmnpqrstvwxyz':
        #return bool True if it is a consonant
        return True
    else:
        #return bool False if it is not a consonant
        return False
    
is_consonant('B')




#4
#capitalize_consonant_words defines a single parameter, a string, and returns a string capitalized
#if it begins with a consonant
def capitalize_consonant_words(string):
    #check to see if the first letter of the string is a consonant
    if is_consonant(string[0]) == True:
        #return the string capitalized if the first letter checks out
        return string.capitalize()
    else:
        #return the string as it was input; does not capitlize string if first letter not a consonant
        return string
    
capitalize_consonant_words('success')




#5
#calculate_tip defines two parameters, a float and another float, and returns a float value
def calculate_tip(percentage, bill):
    #set identifier 'tip' to the value of the product for the percentage (float 1) and the bill (float 2) 
    tip = bill * percentage
    #we just want the tip (rounded to two decimal places)
    return round(tip, 2)

calculate_tip(.22, 18.24)




#6 
#apply_discount defines two parameters, two floats, and returns a float value
def apply_discount(price, disc):
    #return the discounted price (price minus discount) as a float, rounded to two decimals
    return round(price * (1 - disc), 2)

apply_discount(24.99, .8)




#7
#my handle_commas defines a single parameter, a string, and returns a float value
def handle_commas(string):
    #assign a variable to an empty string to work with
    c_handled = ''
    #start a loop to check every character in string input
    for c in string:
        #if the character is a number, add to the variable (string)
        if c.isdigit():
            c_handled += c
        #if the character is a decimal, add to the string
        elif c == '.':
            c_handled += '.'
    #return the string as a float
    return float(c_handled)

handle_commas('12,345,678.9')




#8
#get_letter_grade determines a single parameter, an integer, and returns a string value
def get_letter_grade(x):
    #check if the integer is above the value of 89, return string value 'A' if it is
    if x > 89:
        return 'A'
    #since we are checking if the input is greater than a certain value, and python reads top-to-bottom, we can 
    #just check if the input is above a value less than the previous if-clause value and return the 
    #appropriate/ corresponding string value
    elif x > 79:
        return 'B'
    elif x > 69:
        return 'C'
    elif x > 64:
        return 'D'
    else:
        return 'F'   
    
get_letter_grade(69)




#9
#remove_vowels determines a single parameter, a string, and returns a string
def remove_vowels(string):
    #assign a variable to an empty string
    v_removed = ''
    #start a loop to check if characters in input string are not vowels
    for l in string:
        if not is_vowel(l):
            #only add vowel-opposite characters to the string variable
            v_removed += l
    #return the string variable with characters that are not vowels
    return v_removed

remove_vowels('Nnnnooooooooooo!!!!')




#10
#normalize_name defines a single parameter, a string, and returns a string value
def normalize_name(string):
    #python identifiers can not start with numbers. Loop through string until first character of string is not 
    #a number. move numbers to the back
    while string[0].isdigit():
        string = string[1:] + string[0]
    #assign a variable to: the input string stripped of all leading or trailing white space, as well as with all
    #lowercased characters
    f_name = string.strip().lower() 
    #assign a variable to an empty string
    e_name = ''
    #twice
    end_game = ''
    #start a loop to see if string characters are python identifer compliant
    for char in f_name:
        #include space so we don't have random underscores at the beginning or end if original string input includes
        #invalid characters for python-identifier compliance at the beginning or end of original input and spaces
        #inbetween those invalid characters and valid ones. check to see if characters are in approved list
        if char in 'abcdefghijklmnopqrstuvwxyz_0123456789 ':
            #add all the approved characters to the first empty string variable
            e_name += char
    #assign a variable to the result stripped of all the leftover leading or trailing whitespace
    g_name = e_name.strip()
    #start another for loop to get a cleaner string
    for char in g_name:
        #check to see if character is py-id compliant
        if char in 'abcdefghijklmnopqrstuvwxyz_0123456789':
            #add py-id compliant characters to second empty string variable
            end_game += char
        #check to see if character is a space
        if char == ' ':
            #add an underscore to the second string variable in a space's stead
            end_game += '_'
    #return the python-identifier-compliant second string variable value
    return end_game

if __name__ == '__main__':
    print(normalize_name('First name'))
    print(normalize_name('Name'))
    print(normalize_name('% Completed'))
    print(normalize_name('1man'))




#Example code
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

#interpretation
#if A = [1, 1, 1], then cumulative_sum(A) = [(A[0]), (A[0] + A[1]), (A[0] + A[1] + A[2])]
#cumulative_sum(A) = [sum(A[:1]), sum(A[:2]), sum(A[:3])]
#cumulative_sum(A) = [sum(A[:0 + 1]), sum(A[:1 + 1]), sum(A[:2 + 1])]
#range(len(A)) = range(0, 3) --> which is zero to two (0, 1, 2)--> which is the complete index for A

#cumulative_sum defines a single parameter, a list, and returns a list
def cumulative_sum(L):
    #return a list of numbers that are each the sum of a number in the input list plus all of the numbers prior to
    #this number in the index. use python's zero-indexing to format the individual sums for the return list. 
    #use a for loop to run through the index of the input list and generate sums for each item on the return list.
    return [sum(L[:n + 1]) for n in range(len(L))]

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cumulative_sum(c)




#Mason's personal functions
#import mason_functions as mf




#pull a number from a string with one number 
def pull_an_integer_from_a_string_with_one_integer(string):
    number = ''
    for char in string:
        if char.isdigit():
            number += char
    return int(number)

pull_an_integer_from_a_string_with_one_integer('Yo! You have 38 unread messages!')
#good to alias it as 'pin'
#can copy and paste below after '#' marker:
#from mason_functions import pull_an_integer_from_a_string_with_one_integer as pin




#get an average of one list (take one paramater and return a float)
def average(n):
    return sum(n) / len(n)

a = [1, 2, 3, 4,]
average(a)




#move the first item in an sequence to the last position of a sequence (take one parameter and return a list)
def first_to_last(s):
    #assign a variable to the first item of the sequence
    x = s[0]
    #assign a variable to the sequence starting with the second item and add the first item to the end of the sequence
    s = s[1:] + [x]
    #return the new sequence with the first item at the end and the second item in front
    return s

first_to_last([1, 2, 3, 4, 5,])




#get the median of a list of numbers (take one parameter and return a float)
def median(x):
    #sort the list so function code can slice into an appropriate data set
    x.sort()
    #assign a variable to the total number of items in the list (how many data points do we have?)
    l = len(x)
    #assign a variable to half of the total of numbers(data points) in the list. If the list is even or odd, the
    #value of this variable is an integer that represents how many times the value two goes into the total of
    #numbers, i.e., 9 // 2 = 4 and 8 // 2 = 4
    n = l // 2
    #introduce an 'if' conditional to determine if the total number of datapoints is odd
    if l % 2 == 1:
        #if it is, return the middle datapoint
        return x[n]
    #otherwise, just return the value in the middle of the two middlest points
    return (x[n - 1] + x[n]) / 2 

#condensed
#def median(x):
    #x.sort()
    #l = len(x)
    #n = l // 2
    #if l % 2 == 1:
        #return x[n]
    #return (x[n - 1] + x[n]) / 2

if __name__ == '__main__':
    print(median([1, 2, 70, 80, 90, 100]))
    print(median([1, 2, 3, 4, 5]))
    print(median([4, 8, 1, 2, 38]))
    print(median([1, 100, 2, 90]))




#count some vowels m8
def count_vowels(string):
    count = 0
    for x in string:
        if is_vowel(x):
            count += 1
    return count

count_vowels('Hadouken!')




#count some consonants m9
def count_consonants(string):
    count = 0
    for x in string:
        if is_consonant(x):
            count += 1
    return count

count_consonants('Shoryuken!')




#Is it true, Brutus? Ay tu?
def count_Trues(list):
    count = 0
    for bool in list:
        if bool == True:
            count += 1
    return count

count_Trues([True, False, True, False, True, False, True])




#Thank you, Ryan Orsinger
def get_db_url(db_name):
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'




#is it 3?
def is_three(x):
    if x == 3 or x == '3' or x.lower() == 'three':
        return True
    else:
        return False
if __name__ == '__main__':        
    print(is_three('ThREe'))
    print(is_three('3'))
    print(is_three(3))




#I would like to see these numbers more clearly-- faster

#add_commas defines a single parameter, x (a float or integer up to 13 digits long), and returns a string
def add_commas(x):
    
    #if there are 3 digits or less, we don't need to add commas
    if len(str(x)) < 4:
        return str(x)
    
    #if there are 4 digits, return the string appropriately formatted
    elif len(str(x)) == 4:
        return str(x)[:1] + ',' + str(x)[1:]
    
    #else if there are 5 digits...
    elif len(str(x)) == 5:
        return str(x)[:2] + ',' + str(x)[2:]
    
    #what's here?
    elif len(str(x)) == 6:
        return str(x)[:3] + ',' + str(x)[3:]
    
    #what's here?
    elif len(str(x)) == 7:
        return str(x)[:1] + ',' + str(x)[1:4] + ',' + str(x)[4:]
    
    #what's here?
    elif len(str(x)) == 8:
        return str(x)[:2] + ',' + str(x)[2:5] + ',' + str(x)[5:]
    
    #if it's a kitty
    elif len(str(x)) == 9:
        return str(x)[:3] + ',' + str(x)[3:6] + ',' + str(x)[6:]
    
    #if it's in the billions
    elif len(str(x)) == 10:
        return str(x)[:1] + ',' + str(x)[1:4] + ',' + str(x)[4:7] + ',' + str(x)[7:]
    
    #if it's in the tens of billions
    elif len(str(x)) == 11:
        return str(x)[:2] + ',' + str(x)[2:5] + ',' + str(x)[5:8] + ',' + str(x)[8:]
    
    #if it's in the hundreds of billions
    elif len(str(x)) == 12:
        return str(x)[:3] + ',' + str(x)[3:6] + ',' + str(x)[6:9] + ',' + str(x)[9:]
    
    #lookifanythingmakesitpast the trillions, I am done adding commas
    elif len(str(x)) == 13:
        return str(x)[:1] + ',' + str(x)[1:4] + ',' + str(x)[4:7] + ',' + str(x)[7:10] + ',' + str(x)[10:]

#testing, attention please
if __name__ == '__main__':
    print(add_commas(100))
    print(add_commas(1000))
    print(add_commas(10000))
    print(add_commas(100000))
    print(add_commas(1000000))
    print(add_commas(10000000))
    print(add_commas(100000000))
    print(add_commas(1000000000))
    print(add_commas(10000000000))
    print(add_commas(100000000000))
    print(add_commas(1000000000000))

    
    
#reference for splitting data    
def split_data(df):
    '''
    Takes in a dataset and returns the train, validate, and test subset dataframes.
    Dataframe size for my test set is .2 or 20% of the original data. 
    Validate data is 30% of my training set, which is 24% of the original data. 
    Training data is 56% of the original data.
    '''
    #import splitter
    from sklearn.model_selection import train_test_split
    
    #get my training and test data sets defined, stratify my target variable
    train, test = train_test_split(df, test_size = .2, random_state = 421)
    
    #get my validate set from the training set, stratify target variable again
    train, validate = train_test_split(train, test_size = .3, random_state = 421)
    
    #return the 3 dataframes
    return train, validate, test