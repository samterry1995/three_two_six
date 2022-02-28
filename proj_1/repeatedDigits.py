##Samuel Terry
##6786350


from gettext import find
import sys
import re


def conversion(base, integer):
        converted_numbers = []
        if integer == 0:
            return [0]
        while integer != 0:
            # Calculate the remainder which we append to list.
            remainder = integer % base
            converted_numbers.append(remainder)
            # This gives us a new quotient to divide by in the next equation.
            integer //= base

        return converted_numbers[::-1]


def findBlocks(base, integer):
    longest_block = 0
    block_length = 0
    digit = 0   #This variable grabs the number at the start of the longest block.  If integer <= base +1 this will always be 0 as we haven't reached [1,1]
    for n in range(1, integer):
        if findRepeats(conversion(base, n)) :  # If we have found a repeating digit.
            block_length += 1  # increment block_length variable.
                                            
        else:
            if block_length > longest_block:  # And block length is greater than longest_block.
                longest_block = block_length  # We get a new longest_block variable.
                digit = n  - block_length 
                block_length = 0

            else:
                block_length = 0  # This helps me properly reset the block_length variable
                                           # as I was encountering an issue where after I find my first repeated longest_block is properly incremented.  But if I find another block of length
                                           # one. Block length is never reset as it doesn't enter the found a bigger block method.  This means if I find a single repeat, followed by a not
    if (block_length > longest_block ):  #repeat. block_length still goes up to two as it wasn't properly reset.  Despite a block of length 1 being found, longest_block is stored as 2.
        longest_block = block_length
        digit = (integer ) - (block_length)

    return digit, longest_block

def findRepeats(list):  # This method iterates through individual base conversions and finds repeats.
    return len(list) != len(set(list))

def findMatchingRepeats(baseA, baseB):
    if baseA > baseB:       ##The smallest occuring repeat is 1,1 so we skip all the numbers below
        i = baseA + 1       # 11 to save ourselves time.
    else:
        i = baseB + 1
    notFound = False

    while notFound == False: 
        firstBase = conversion(baseA, i)                      ##Convert numbers from 0 and up until we find a common repeat for
        secondBase = conversion(baseB, i)                      ##both bases.
        if (findRepeats(firstBase) and findRepeats(secondBase)):##This picks up the first occurence of repeats in both bases.
            foundMatchingRepeat = i                            #Save the current integer in base 10 where repeat is happening.
            notFound = True;                                    ##Leave the while loop.
           
        else:                                                   ##If we haven't found the number at i in base 10, go to 1 +=1.
            i +=1
            notFound == False
    return foundMatchingRepeat

def main():


        for line in sys.stdin:
            tokens = line.rsplit()
            try:
                if (len(tokens) == 3):
                    if((tokens[0] == ('A')) and (int(tokens[1])) and (int(tokens[2]) > 0)):
                        a, b = findBlocks(int(tokens[1]),int(tokens[2]))
                        print(str(a) + " " + str(b))
                    elif((tokens[0] == ('B')) and (int(tokens[1]) >0) and (int(tokens[2]) > 0)):
                        c = findMatchingRepeats(int(tokens[1]), int(tokens[2]))
                        print(str(c))
                    else:
                        raise Exception()  
                else:
                    raise Exception()
            except:
                print("Bad line:  " + line.rstrip())
    
main()

