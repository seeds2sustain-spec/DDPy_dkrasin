#!/usr/bin/env python3
import sys
import re

# Check if there are no parameters (sys.argv only has the script name)
if len(sys.argv) == 1:
    print("none")
else:
    # Loop through all parameters starting from index 1
    for param in sys.argv[1:]:
        # Use regex matching to check if the string ends with "ism"
        # The '$' symbol means the end of the string
        if not re.search(r'ism$', param):
            print(f"{param}ism")