# Filled in rect area from for functionality
def rect_area(x, y):
    return x * y


###Jackson Manriquez's function
def rect_surface_area(x, y, z):
    length_width = rect_area(x, y)*2
    length_height = rect_area(x, z)*2
    width_height = rect_area(y, z)*2

    surface_area = length_width + length_height + width_height
    return surface_area


# The request for dimenisions
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

surface_area = rect_surface_area(length, width, height)
# Finishing of functions
print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)
