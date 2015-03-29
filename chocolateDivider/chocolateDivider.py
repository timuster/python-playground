"""
    Author : Sumit Kumar - timus@vt.edu
    Authored on : 3/28/2015
    Version : 1.0

    Details: The following script solves the chocolate division problem.

    To Run : python ./chocolateDivider.py

    Associated files: chocolateDivider_Test.py

    Notes:
        * The following script should be compatible with both Python 2 and 3.
        * Added verbose mode for prompts.
        * Added chocolateDivider_Test.py for test cases.
"""

# Global Variables:
verboseMode = False

# The following fix is needed to make this script compatible with both Python 2.x. and Python 3.x.
# since "raw_input" was changed to "input" in Python 3.x.
try:
    input = raw_input
except NameError:
    pass


def customPrintForVerbose(printString):
    """
        Prints the given string if verbose mode is enabled.
        :param printString: String to be printed.
        :return:
    """
    if verboseMode == True:
        print printString


def printOutput(outputSequence):
    """
        Prints the program's output in the expected format.
        :param outputSequence: Sequence of true/false based on results.
        :return:
    """
    outputCounter = 1

    if len(outputSequence) == 0:
        print "No output to show!"
        return

    for output in outputSequence:

        if output == True:
            answer = "Yes"
        else:
            answer = "No"

        print "Case", outputCounter, ":", answer
        outputCounter += 1


def get_user_input():
    """
        Gets user input for the various input parameters.

            First input : The number of parts the bar is supposed to be split in.
                            Constraint:  1 <= n <= 15

            Second input : The number of parts the bar is supposed to be split in.
                            Constraint:  1 <= n <= 100

            Third input : The number of parts the bar is supposed to be split in.
                            Constraint:  Must be equal to First input.

        :return: Returns a list with number of rows, number of columns, and a list of number of pieces in each part.


        Note :  Program continuously takes the above 3 inputs for separate sets.
                Enter 0 to terminate, and show output.
    """
    returnList = []

    try:

        ########## Get first input ##########
        customPrintForVerbose("Enter number of parts - You may enter 0 to show output.")
        numberOfParts = int(input(''))

        if numberOfParts == 0:

            #If 0 has been entered as the first input, we have reached the end of user input.
            #Return None so that the calling function terminates.

            customPrintForVerbose("0 detected. Terminating user input, and showing Output (if any) : ")
            return None

        if numberOfParts < 1 or numberOfParts > 15:
            #Ensure that the number is between 1 and 15 - raise an error otherwise.
            raise Exception

        ########## Get second input ##########
        customPrintForVerbose("Enter the dimensions of the chocolate bar: ")
        inputRaw = input("").split()

        if len(inputRaw) < 2:
            # Ensure that at least 2 values have been entered. Ignore anything extra.
            print "Oops! Expecting 2 numbers. Rows x Columns"
            chocolate_divider()

        # Two integers : Dimension of chocolate bar.
        numRows = int(inputRaw[0])
        numColumns = int(inputRaw[1])

        if numRows < 1 or numRows > 100 or numColumns < 1 or numColumns > 100:
            #Ensure that the numbers are between 1 and 100 - raise an error otherwise.
            raise Exception

        ########## Get third input ##########
        sizesArray = []
        customPrintForVerbose("Enter the sizes: ")
        inputRaw = input("").split()

        if len(inputRaw) < numberOfParts:
            #Ensure number of sizes entered matches the first input. Ignore anything extra.
            print "Oops! Expecting sizes for %d parts." %numberOfParts
            chocolate_divider()

        for x in inputRaw:
            sizesArray.append(int(x))

        returnList.extend((numRows,numColumns,sizesArray))
        return returnList

    except ValueError:
        # Print error if input is not type-compatible (int), or if it is out of range, i.e. not between
        # 1 and 15 - as mentioned in the problem statement.
        print "Oops! A valid integer was expected. Please try again!"

        #Call the function again.
        chocolate_divider()

    except:
        #Restart program after any exception for the user to try again.
        print "An error has occurred. Kindly check your input. Restarting program."
        chocolate_divider()



def checkForValidDivision(numRows,numColumns,sizesArray):
    """
        Checks for valid division of chocolate bar

        :param numRows: Number of rows.
        :param numColumns: Number of columns.
        :param sizesArray: List of
        :return: True, if valid. False, if invalid.
    """
    returnValue = True
    minimumOneNotTooBig = False # Bool to ensure at least one size is small enough to accommodate all pieces.

    # First, check if the sum of pieces equals the dimensions.
    if sum(sizesArray) != (numRows*numColumns):
        return False # Don't proceed, and just return False.

    for numPiece in sizesArray:

        if (numPiece > numRows) and (numPiece > numColumns) :

            returnValue = False

            larger = numRows
            smaller = numColumns

            if numColumns > numRows:
                larger = numColumns
                smaller = numRows

            for n in range(larger,0,-1):
                if (numPiece % n) == 0:
                    if (numPiece / n) < smaller:
                        returnValue = True
                        break

        else:
            minimumOneNotTooBig = True
            continue

    return (returnValue and minimumOneNotTooBig)


def chocolate_divider():
    """
        Driver function. Calls the appropriate functions to get input, and show output.
        :return:
    """
    global verboseMode
    verboseReply = input("Would you like to enable verbose mode? Y/N ")
    verboseEnable = ["y","Y","YES","yes","Yes","1"]

    if str(verboseReply) in verboseEnable:
        verboseMode = True
    else:
        verboseMode = False

    outputSequence = []

    while True:
        currentSequence =  get_user_input()
        if currentSequence is None:
            # currentSequence is returned as None when user enters 0 for first input.
            break
        else:
            # Perform calculation
            outputSequence.append(checkForValidDivision(currentSequence[0],currentSequence[1],currentSequence[2]))

    printOutput(outputSequence)


# Call the driver function.
if __name__ == '__main__':
    chocolate_divider()