# How to get the area
# Author Elaine
# Date 21/5/2025
# Version 2


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

keep_going=''
while keep_going=='':


# Ask the user for the width and the Height 
#(assume they put in valid data)
Width=float(input("Width: " ))
Height=float(input("Height: " ))

#catcultae the area/ perimeter
area = Width* Height
perimeter = 2 * (Width + Height)
# Output the area and pertimeter
print()
print(f"Perimeter:{perimeter} units")
print(f"Area: {area} square units")