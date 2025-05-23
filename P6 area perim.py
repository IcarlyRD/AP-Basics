# How to get the area
# Author Elaine
# Date 21/5/2025
# Version 1


# Ask the user for the width and the Height 
# #(assume they put in valid data)
Width=float(input("Width: " ))
Height=float(input("Height: " ))

#catcultae the area/ perimeter
area = Width* Height
perimeter = 2 * (Width + Height)

# Output the area and pertimeter
print()
print(f"Perimeter:{perimeter} units")
print(f"Area: {area} square units")