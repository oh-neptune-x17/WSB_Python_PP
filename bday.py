# This program uses a dictionary to keep friends'
# names and birthdays.
# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
SAVE = 6
READ = 7
READLOCAL = 8
FILENAME = 'birthdays.dat'

# + dla chętnych jako strukturę class
import pickle

# main function
def main():
    # Create an empty dictionary.
    birthdays = {}
    # Initialize a variable for the user's choice.
    choice = 0
    while choice != QUIT:
    # Get the user's menu choice.
        choice = get_menu_choice()
    # Process the choice.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
        elif choice == SAVE:
            save(birthdays)
        elif choice == READ:
            read(birthdays)
        elif choice == READLOCAL:
            read_fromloaded(birthdays)


def getChoice():
    choice = input('What do you want to do: ')
    while not choice.isdecimal():
        print('Please enter only decimals: ')
        choice = input('What do you want to do: ')
    return int(choice)

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print('6. Save the database')
    print('7. Read the database from file')
    print('8. Read from database')
    print()

    # Get the user's choice.
    choice = getChoice()

# Validate the choice.
    while choice < LOOK_UP or choice > READLOCAL:
      choice = int(input('Enter a valid choice: '))
    # return the user's choice.
    return choice


# The look_up function looks up a name in the
# birthdays dictionary.
def look_up(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')
    try: # tries to find the key in dictionary, else throw exception
        print(birthdays[name])
    except KeyError:
        print("Haven't found", name, 'in database')

# func run as condition for while loop in adding/changing records
# determines validity of inputs
# could have used dedicated library for all this of course (include datetime)
def checkDate(birthdays, bday):

    #check if user gives proper values
    #no alphanumerics are allowed for specific places in date
    if not (bday[0:2].isdecimal() and bday[3:5].isdecimal() and bday[6:10].isdecimal()):
        print('Please use only decimal values for DD, MM and YYYY')
        return False

    # checking if user gives proper format at all
    # this part of program can be hardcoded as DD/MM/YYYY format is static
    if len(bday) != 10:
        print('Exactly DD.MM.YYYY format is needed! ')
        return False

    # days check, conditions are obvious, prints explain everything
    if int(bday[0:2]) > 31 or int(bday[0:2]) <= 0:
        print('No month has more than 31 days, or 0 and less')
        return False

    # bday[3:5] is actually 02, casted to int returns 2
    # haven't added condition to check if inputted years are %4 to have 29 days
    if int(bday[3:5]) == 2 and int(bday[0:2]) > 29:
        print("February can't have more than 29 days")
        return False

    # February is already checked in condition above so that leaves us with months that have 30 days
    # same as above - 04, 06, 09 cast to int return 4, 6, 9 respectively
    if (int(bday[3:5]) == 4 or int(bday[3:5]) == 6 or int(bday[3:5]) == 9 or int(bday[3:5]) == 11) and int(bday[0:2]) > 30:
        print("These months can't have more than 30 days")
        return False

    #months check
    if int(bday[3:5]) > 12 or int(bday[3:5]) < 1:
        print('There are exactly 12 months, please correct')
        return False

    #specific format check for dots
    if bday[2] != '.' or bday[5] != '.':
        print('Please separate input with dots!')
        return False
    print()
    return True

# The add function adds a new entry into the
# birthdays dictionary.
def add(birthdays):
    # Get a name and birthday.
    name = input('Enter a name of your entry: ')
    bday = input('Enter a birthday in DD.MM.YYYY format: ')
    while not checkDate(birthdays, bday):
        bday = input('Enter a birthday in DD.MM.YYYY format: ')
    # If the name does not exist, add it.
    if name not in birthdays:
        birthdays[name] = bday
        print()
        print('Entry added!')
    else:
        print('That entry already exists.')

# The change function changes an existing
# entry in the birthdays dictionary.
def change(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')
    if name in birthdays:
        # Get a new birthday.
        bday = input('Enter the new birthday: ')
        while not checkDate(birthdays, bday):
            bday = input('Enter the new birthday: ')
        # Update the entry.
        birthdays[name] = bday
        print()
        print('Entry changed!')
    else:
        print('That name is not found.')


# The delete function deletes an entry from the
# birthdays dictionary.
def delete(birthdays):
    # Get a name to look up.
    name = input('Enter a name: ')
    # If the name is found, delete the entry.
    if name in birthdays:
       del birthdays[name]
    else:
       print('That name is not found.')


# Save function saves lookup map to .dat file using pickle library
def save(birthdays):
    output_file = open(FILENAME,'wb')
    pickle.dump(birthdays, output_file)
    output_file.close()


# Read the function to a birthdays dictionary
def read(birthdays):
    EOFFLAG = False
    input_file = open(FILENAME, 'rb')
    while not EOFFLAG:
        try:
           birthdays = pickle.load(input_file)
        except EOFError:
            EOFFLAG = True
    for keys in birthdays:
        print(keys, birthdays[keys])


def read_fromloaded(birthdays): # doesnt include pickle load
    for keys in birthdays:
        print(keys, birthdays[keys])


# Call the main function.
main()


