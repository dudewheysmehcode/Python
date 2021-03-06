'''
Created on Jun 20, 2013

@author: rmaharaj
@summary: This program will read a file and perform a linear regression.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# N/A
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# imported methods
from lib import prompts as prompts, maths as maths, files as files

# global variables
filename = ""

def main():
    print "Welcome! This program will read a file and perform a linear regression.\n"
    
    # prompt for entry of file name & entry mode, and set global variables
    set_filename(prompts.linear_regression_filename_prompt("Please enter the full file path & file name:"))
    body()

def body():
    maths.linear_regression(files.split_elements_of_array(files.load_file_to_array(filename)))

def get_filename():
    print "File Name:", filename
    return filename

def set_filename(value):
    global filename
    filename = value

main()