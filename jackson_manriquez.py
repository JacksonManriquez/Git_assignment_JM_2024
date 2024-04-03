# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object

# The following four lines are just there to make the code work without errors until functions are added
def rect_area(x, y):
    return 1


###Jackson Manriquez's function
def rect_surface_area(x, y, z):
    length_width = rect_area(x, y)*2
    length_height = rect_area(x, z)*2
    width_height = rect_area(y, z)*2

    surface_area = length_width + length_height + width_height
    return surface_area


# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

surface_area = rect_surface_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)
