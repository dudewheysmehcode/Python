'''
Created on Jun 15, 2013

@author: rmaharaj
@summary: This file contains functions to manipulate files.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# Ensure that project references the Commons project
# add:
#     import lib.files as files
#   or
#     from lib import files as files
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# imports
import os, re
import checks

def check_filename(value, saveas, entryMode):
    result = False
    pattern = re.compile(r'\w{1}:{1}[\\|/]{1}.*[^\\/:*?"<>|]*[\.]*[.]{1}[\w]{3}')
    if type(value) == str:
        if pattern.match(value):
            if entryMode == 0:
                if os.path.exists(value):
                    result = True
                else:
                    print "You are trying to read a file which does not exist.\n"
                    result = False
            elif entryMode == 1:
                if not os.path.exists(value):
                    result = True
                else:
                    print "You are trying to write to a file which already exists.\n"
                    result = False
            elif entryMode == 2:
                if os.path.exists(value) or saveas:
                    result = True
                else:
                    print "You are trying to modify a file which does not exist.\n"
                    result = False
        else:
            print "Invalid file.  You have probably missed the filename or extension."
    else:
        print "Invalid file.  Not a string.\n"
        result = False
    return result

def check_is_valid_file(value):
    result = False
    pattern = re.compile(r'\w{1}:{1}[\\|/]{1}.*[^\\/:*?"<>|]*[\.]*[.]{1}[\w]{3}')
    if type(value) == str:
        if pattern.match(value):
            result = True
        else:
            print "Invalid file.  You have probably missed the filename or extension.\n"
    else:
        print "Invalid file.  Not a string.\n"
        result = False
    return result

def check_file_for_valid_LR_data(filename):
    result = True
    f = split_elements_of_array(load_file_to_array(filename))
    if len(f) == 0:
        result = False
    for i in range(0,len(f)):
        if len(f[i]) == 3:
            for j in range(0,3):
                if checks.is_valid_number_no_print(f[i][j]):
                    pass
                else:
                    result = False
                    break
        else:
            result = False
            break
    
    return result

def load_file_to_array(filename):
    fileToOpen = open(filename, 'r+')
    f = [' '.join(line.split()) for line in fileToOpen]
    fileToOpen.close()
    return f

def split_elements_of_array(array):
    return [(item.split()) for item in array] 