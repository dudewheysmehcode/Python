'''
Created on Jun 15, 2013

@author: rmaharaj
@summary: This file contains functions to prompt for user entry.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# Ensure that project references the Commons project
# add:
#     import lib.prompts as prompts
#   or
#     from lib import prompts as prompts
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# imports
import checks, files

def fix_end_prompt():
    validOption = False
    while not validOption:
        option = raw_input("\nWould you like to fix your entry or end the program? 1 = Fix, 0 = End:")
        if option == "1":
            validOption = True
            return True
        elif option == "0":
            validOption = True
            quit()
        else:
            print "Invalid option..."
            validOption = False

def number_prompt(firstTime):
    validEntry = False
    if firstTime:
        msg = "\nPlease enter a number/array:"
    else:
        msg = "\nPlease enter a replacement number/array:"
    
    # test for space
    while not validEntry:
        num = raw_input(msg)
        if checks.is_valid_number(num) or checks.is_valid_array(num):
            validEntry = True
        else:
            print "Invalid number/array entered."
            if not fix_end_prompt():
                validEntry = True
    return num

def entry_mode_prompt(msg):
    validMode = False
    while not validMode:
        mode = raw_input(msg)
        if checks.check_entryMode(mode):
            validMode = True
        else:
            print "Invalid mode entered."
            if not fix_end_prompt():
                validMode = True
    return mode.lower()

def numberQuantity_prompt(msg):
    validNumberQuantity = False
    while not validNumberQuantity:
        numberQuantity = raw_input(msg)
        if checks.is_valid_integer(numberQuantity):
            validNumberQuantity = True
        else:
            print "Invalid number quantity entered."
            if not fix_end_prompt():
                validNumberQuantity = True
    return numberQuantity.lower()

def modify_prompt(msg):
    validAction = False
    while not validAction:
        modifyAction = raw_input(msg)
        if checks.check_modifyAction(modifyAction):
            validAction = True
        else:
            print "Invalid action entered."
            if not fix_end_prompt():
                validAction = True
    return modifyAction.lower()
    
def filename_prompt(msg, saveas):
    validFilename = False
    while not validFilename:
        name = raw_input(msg)
        if files.check_filename(name, saveas):
            validFilename = True
        else:
            print "Invalid filename entered."
            if not fix_end_prompt():
                validFilename = True
    return name

def linear_regression_filename_prompt(msg):
    validFilename = False
    validContents = False
    while not validFilename:
        name = raw_input(msg)
        if files.check_is_valid_file(name):
            validFilename = True
        else:
            print "Invalid filename entered."
            if not fix_end_prompt():
                validFilename = True
    while not validContents:
        if files.check_file_for_valid_LR_data(name):
            validContents = True
        else:
            print "Improperly formatted file chosen."
            if not fix_end_prompt():
                validContents = True
    return name

def save_or_saveAs_prompt(msg):
    validAnswer = False
    while not validAnswer:
        answer = raw_input(msg)
        if str(answer.lower()) == "save" or str(answer.lower()) == "saveas" or str(answer.lower()) == "no":
            validAnswer = True
        else:
            print "Invalid option entered."
            if not fix_end_prompt():
                validAnswer = True
    return [True, answer.lower()]

def insert_where_prompt(end):
    validWhere = False
    while not validWhere:
        msg = "Where do you want to insert the number? 1 = after this number, ..., " + str(end) + ", before last number."
        where = raw_input(msg)
        if checks.is_valid_integer(where) and int(where) > 0 and int(where) <= end:
            validWhere = True
        else:
            print "Invalid choice entered."
            if not fix_end_prompt():
                validWhere = True
    return where.lower()
    
def yes_no_prompt(msg):
    validAnswer = False
    while not validAnswer:
        answer = raw_input(msg)
        if str(answer.lower()) == "yes" or str(answer.lower()) == "no":
            validAnswer = True
        else:
            print "Invalid choice entered."
            if not fix_end_prompt():
                validAnswer = True
    return answer.lower()