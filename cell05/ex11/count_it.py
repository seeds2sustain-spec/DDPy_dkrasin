#!/usr/bin/env python3
import sys

# Check if there are no parameters passed (sys.argv only contains the script name at index 0)
if len(sys.argv) == 1:
    print("none")
else:
    # Calculate the number of actual parameters by subtracting 1 from the total length of sys.argv
    num_params = len(sys.argv) - 1
    print(f"parameters: {num_params}")
    
    # Loop through each parameter starting from index 1 using a 'for' loop
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")