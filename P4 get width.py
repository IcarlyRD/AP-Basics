# How to get width
# Author Elaine
# Date 21/5/2025
# Version 1

# Ask the user for width and loop until
# enter a number that is more than Zero
 
error=(" Please enter a number that is more than zero\n")
while True:

    try:
        # ask the user of a number
        width= float(input("width :"))
        
        # Cheack the number is more than zero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)        



   