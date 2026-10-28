#!/usr/bin/env python3
import sys

# Check if exactly two parameters are passed (sys.argv length will be 3 including the script name)
if len(sys.argv) == 3:
    # Convert the parameters from strings to integers
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    # Use range to get values from start to end (inclusive, so we add 1 to the end)
    # Convert the range object to a list (array)
    number_array = list(range(start, end + 1))
    
    # Display the array using the print function
    print(number_array)
else:
    # Display 'none' if the parameter count is incorrect
    print("none")