#!/usr/bin/env python3
import sys
import re

# Check if exactly one parameter is provided (sys.argv length is 2)
if len(sys.argv) == 2:
    # Use re.findall to extract all lowercase "z" characters
    matches = re.findall("z", sys.argv[1])
    
    # If "z" is found at least once
    if len(matches) > 0:
        # Print "z" for each occurrence on a single line
        for match in matches:
            print(match, end="")
        # Print a newline at the end
        print()
    else:
        # If no "z" is found, print "none"
        print("none")
else:
    # If the number of parameters is not 1, print "none"
    print("none")