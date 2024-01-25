pi = 3.14159


def get_input():
    radius = float(input("Enter the radius: "))
    return radius


def calculate_circle_circumference(radius):
    circumference = 2 * pi * radius
    return round(circumference, 5)


def calculate_circle_area(radius):
    area = pi * radius ** 2
    return round(area, 5)


def calculate_circle_volume(radius):
    volume = 4 / 3 * pi * radius ** 3
    return round(volume, 5)


# I know I could add these directly to the string, but I like to keep each line doing two or less thing if I can. It
# just keeps things more obvious for everyone, including myself.
radius = get_input()
circumference = calculate_circle_circumference(radius)
area = calculate_circle_area(radius)
volume = calculate_circle_volume(radius)

print("The circumference of a circle with a radius of {} is {}".format(radius, circumference))
print("The area of a circle with a radius of {} is {}".format(radius, area))
print("The volume of a sphere with a radius of {} is {}".format(radius, volume))
print("The formulas for calculating the circumference, C, area, A, and volume, V, for a radius, r, are as follows: \n "
      "C = 2πr \n A = πr\u00b2 \n V = 4/3 πr\u00b3")
