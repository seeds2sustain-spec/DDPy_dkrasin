#!/usr/bin/env python3

try:
    # Prompt the user to enter a number
    number = float(input())
    
    # Check if the number is exactly zero
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
        
except ValueError:
    # If the user types something that isn't a number (like text)
    print("This number is different from zero.")