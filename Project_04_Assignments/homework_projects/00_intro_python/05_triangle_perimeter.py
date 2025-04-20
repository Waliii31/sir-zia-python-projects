def triangle_parameter():
    side1: float = float(input("Enter the length of side 1: "))
    side2: float = float(input("Enter the length of side 2: "))
    side3: float = float(input("Enter the length of side 3: "))
    
    parameter: float = side1 + side2 + side3
    print(f"The perimeter of the triangle is: {parameter} units")

triangle_parameter()