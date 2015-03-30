"""
    Author : Sumit Kumar - timus@vt.edu
    Authored on : 3/28/2015

    Details : To run this test script, comment out the last line in chocolateDivider.py, so that its function-driver is disabled.

    To Run : python ./chocolateDivider_test.py

    Notes : Add your own sets of inputs below to test.
"""

from chocolateDivider import checkForValidDivision

inputList = [

    # Test 1
    [
        3, # Rows
        4, # Columns
        [6,3,2,1], # List of pieces in different parts.
        True # Expected answer
    ],

    # Test 2
    [
        2, # Rows
        3, # Columns
        [1,5], # List of pieces in different parts.
        False # Expected answer
    ],

    # Test 3
    [
        0, # Rows
        0, # Columns
        [0,0], # List of pieces in different parts.
        True  # Expected answer - or false. This test is just to ensure that the function doesn't crash even without
                # input error checking.
    ],

    # Test 4
    [
        5, # Rows
        7, # Columns
        [9,10,16],
        False # This test makes use of the second check - i.e. at least one part has smaller number of pieces than the
                # greater of the two dimension (row/column) to ensure that it is indeed possible to break it.
    ],

    # Test 5
    [
        2, # Rows
        3, # Columns
        [1,1,1,1,1,1], # List of pieces in different parts.
        True # Expected answer
    ],

    # Test 6
    [
        4, # Rows
        4, # Columns
        [9,2,2,3], # List of pieces in different parts.
        True # Expected answer
    ],

    # Test 7
    [
        2, # Rows
        2, # Columns
        [3,1], # List of pieces in different parts.
        False # Expected answer
    ],

    # Test 8
    [
        2, # Rows
        2, # Columns
        [2,2], # List of pieces in different parts.
        True # Expected answer
    ],

    # Test 9
    [
        10, # Rows
        7, # Columns
        [42,28], # Test to ensure that a large piece was not wrongly handled.
        True # Expected answer
    ],

]

caseID = 1
for currentInput in inputList:

    if checkForValidDivision(currentInput[0],currentInput[1],currentInput[2]) == currentInput[3]:
        print "Passed test :", caseID
    else:
        print "************************************"
        print "Failed test",caseID,".Case details :"
        print "************************************"
        print "Rows :", currentInput[0]
        print "Columns :", currentInput[1]
        print "Pieces sizes :", currentInput[2]
        print "Expected Answer :", currentInput[3]
        print "***End Of Case***"

    caseID += 1
