INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def inch_to_foot():
    feet: float = float(input("Enter number of feet: "))  
    inches: float = feet * INCHES_IN_FOOT  
    print(f"That is {inches} inches!")
    

inch_to_foot()