'''
Created on Jun 15, 2013

@author: rmaharaj
@summary: This program will either read a file, write to a file, or modify a file.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# N/A
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# imported methods
import re, os

# define global variables
# filename will hold the file which will be opened
# entryMode will be 0 for Read, 1 for Write
# maxArraySize represents the maximum number of elements in an inputted array (K)
filename = ""
entryMode = 0
maxArraySize = 10

# the main method will prompt the user for the filename, the entry method,
# and verify that the values entered by the user are valid
# if it is, it will pass control to the body() method
# otherwise, the program will end.
def main():
    print "Welcome! This program will either read from, write to, or modify a file of numbers.\n"
    
    # prompt for entry of file name & entry mode, and set global variables
    set_entryMode(entry_mode_prompt("\nPlease enter the mode: Read, Write, or Modify"))
    set_filename(filename_prompt("Please enter the full file path & file name:", False))
    body()
    
def body():
    if entryMode == 0:
        read_from_file()
    elif entryMode == 1:
        write_to_file()
    elif entryMode == 2:
        modify_file()
    else:
        print "Entry mode error in body."
        
def read_from_file():
    fileToRead = open(filename, 'r')
    print fileToRead.read()
    fileToRead.close()

def write_to_file():
    fileToWrite = open(filename, 'w')
    
    # prompt for quantity of numbers
    n = int(numberQuantity_prompt("\nPlease enter n, the quantity of records to be entered. (INTEGERS ONLY)"))
    print "Please note that arrays should only contain numbers and spaces..."
    
    numbers = []
    for _ in range(0,n):
        numbers.append(number_prompt(True))
  
    with fileToWrite as f:
        f.writelines("\n".join(numbers))
    fileToWrite.close()

def modify_file():
    fileToModify = open(filename, 'r+')
    numbers = []
    for line in fileToModify:
        numbers.append(' '.join(line.split()))
    fileToModify.close()
#     print numbers
    
    print "\nFor each of the following numbers/arrays, please choose Accept, Replace, or Delete"
    
    acceptAll = False
    # for each num in file, read -> accept, replace, delete
    for i, num in enumerate(numbers):
        if not acceptAll:
            print "\nPosition:", i + 1, ";   Number:", num
            modifyAction = modify_prompt()
            
            if modifyAction == "accept":
                pass
            elif modifyAction == "replace":
                numbers[i] = number_prompt(False)
            elif modifyAction == "delete":
                numbers.pop(i)
            else:
                print "Error with action:", modifyAction
            
        # insert new num after, or before any other num
            countNumbersLeft = len(numbers) - (i + 1)
            if countNumbersLeft > 0:
                print "\nThere are", str(countNumbersLeft), "numbers between this number and the end of the file."
                doInsert = yes_no_prompt("Would you like to insert a number? Yes or No:")
            
                if doInsert == "yes":
                    insertWhere = insert_where_prompt(countNumbersLeft)
                    numbers.insert(int(insertWhere)+i, number_prompt(True))
                elif doInsert == "no":
                    pass
                else:
                    print "Error with entry:", doInsert
            
        # accept all numbers after
                shouldAcceptAll = yes_no_prompt("\nWould you like to Accept all remaining numbers? Yes or No:")
                if shouldAcceptAll == "yes":
                    acceptAll = True
                    continue
        
        # save or save as
    saveOrSaveAs = save_or_saveAs_prompt("\nWould you like to save the current file, or save as a new file? Save / SaveAs / No (ONE WORD):")
    if saveOrSaveAs[0]:
        fileToSave = ""
        if saveOrSaveAs[1] == "no":
            pass
        elif saveOrSaveAs[1] == "save":
            fileToSave = filename
        elif saveOrSaveAs[1] == "saveas":
            fileToSave = filename_prompt("\nPlease enter the new full file path & file name:", True)
        else:
            print "Error, incorrect save/saveas entry. Not saving file."
            
        if fileToSave != "":
            savedFile = open(fileToSave, 'w')
            savedFile.truncate()
            with savedFile as f:
                f.writelines("\n".join(numbers))
                savedFile.close()
        
def get_filename():
    print "File Name:", filename
    return filename

def set_filename(value):
    global filename
    filename = value

def get_entryMode():
    print "Entry Mode:", entryMode
    return entryMode

def set_entryMode(value):
    global entryMode
    if value == "write":
        entryMode = 1
    elif value == "modify":
        entryMode = 2
    else:
        entryMode = 0

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
        if is_valid_number(num) or is_valid_array(num):
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
        if check_entryMode(mode):
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
        if is_valid_integer(numberQuantity):
            validNumberQuantity = True
        else:
            print "Invalid number quantity entered."
            if not fix_end_prompt():
                validNumberQuantity = True
    return numberQuantity.lower()

def modify_prompt():
    validAction = False
    while not validAction:
        modifyAction = raw_input("\nPlease enter a valid action: Accept, Replace, or Delete.")
        if check_modifyAction(modifyAction):
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
        if check_filename(name, saveas):
            validFilename = True
        else:
            print "Invalid filename entered."
            if not fix_end_prompt():
                validFilename = True
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
        if is_valid_integer(where) and int(where) > 0 and int(where) <= end:
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

def is_valid_number(num):
    pattern = re.compile(r'-?[1-9]+\d*[.]?[0-9]*\Z')
    if pattern.match(num):
        return True
    else:
        return False

def is_valid_integer(num):
    if (num.find("-") == -1) and (num.find(".") == -1) and (int(num) > 0):
        return True
    else:
        print "That was not a valid number."
        return False

def is_valid_array(array):
    pattern = re.compile(r'(-?[1-9]+\d*[.]?[0-9]*){1}\Z|(-?[1-9]+\d*[.]?[0-9]*\s{1}){1,%s}(-?[1-9]+\d*[.]?[0-9]*)\Z'%(maxArraySize-1))
    if pattern.match(array):
        return True
    else:
        return False

def check_filename(value, saveas):
    result = False
    pattern = re.compile(r'\w{1}:{1}[\\|/]{1}.*[^\\/:*?"<>|]*[\.]*[.]{1}[\w]{3}')
    if type(value) == str:
        if pattern.match(value):
            if entryMode == 0:
                if os.path.exists(value):
                    result = True
                else:
                    print "You are trying to read a file which does not exist."
                    result = False
            elif entryMode == 1:
                if not os.path.exists(value):
                    result = True
                else:
                    print "You are trying to write to a file which already exists."
                    result = False
            elif entryMode == 2:
                if os.path.exists(value) or saveas:
                    result = True
                else:
                    print "You are trying to modify a file which does not exist."
                    result = False
        else:
            print "Invalid file.  You have probably missed the filename or extension."
    else:
        print "Invalid file.  Not a string."
        result = False
    return result

def check_entryMode(value):
    if (value == "read") or (value == "write") or (value == "modify"):
        return True
    else:
        print "There is an error in your entry mode:", value
        return False

def check_modifyAction(value):
    if (value == "accept") or (value == "replace") or (value == "delete"):
        return True
    else:
        print "There is an error in your modify Action:", value
        return False

main()
