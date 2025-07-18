shape = input("Shape (circle/rectangle/triangle): ")

if shape.lower() == "circle":
    radius = float(input("Radius: "))
    area = 3.14159 * radius ** 2
elif shape.lower() == "rectangle":
    l = float(input("Length: "))
    w = float(input("Width: "))
    area = l * w
else:
    b = float(input("Base: "))
    h = float(input("Height: "))
    area = 0.5 * b * h

print("Area =", area)
