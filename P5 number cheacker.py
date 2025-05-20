# How to get width
# Author Elaine
# Date 21/5/2025
# Version 1

# Ask the user for width and loop until
# enter a number that is more than Zero
def num_cheak(question):



    error=(" Please enter a number that is more than zero\n")
    while True:

        try:
            # ask the user of a number
            response= float(input(question))
            
            # Cheack the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)        



#Main Routine Goes here
for item in range( 0, 2):
    width =num_cheak("Width: ")   
print=(width)

for item in range( 0, 2):
    height =num_cheak("Height: ")   
print=(height)