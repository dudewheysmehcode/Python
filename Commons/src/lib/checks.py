'''
Created on Jun 15, 2013

@author: rmaharaj
@summary: This file contains functions to check if certain things are valid.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# Ensure that project references the Commons project
# add:
#     import lib.checks as checks
#   or
#     from lib import checks as checks
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# imports
import re

def is_valid_number(num):
    pattern = re.compile(r'-?[1-9]+\d*[.]?[0-9]*\Z|0{1}|[0.0]{1}')
    if pattern.match(num):
        return True
    else:
        print "Invalid number entered."
        return False
    
def is_valid_number_no_print(num):
    pattern = re.compile(r'-?[1-9]+\d*[.]?[0-9]*\Z|0{1}|[0.0]{1}')
    if pattern.match(num):
        return True
    else:
        return False

def is_valid_integer(num):
    if (num.find("-") == -1) and (num.find(".") == -1) and (int(num) > 0):
        return True
    else:
        print "Invalid integer entered."
        return False
    
def is_valid_array(array, maxArraySize):
    pattern = re.compile(r'(-?[1-9]+\d*[.]?[0-9]*){1}\Z|(-?[1-9]+\d*[.]?[0-9]*\s{1}){1,%s}(-?[1-9]+\d*[.]?[0-9]*)\Z'%(maxArraySize-1))
    if pattern.match(array):
        return True
    else:
        print "Invalid array entered."
        return False
    
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

