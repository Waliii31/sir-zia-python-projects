def average(a: float, b: float):
    sum = a + b
    return sum / 2

def main():
    num1: float = float(input("Enter first number: "))
    num2: float = float(input("Enter second number: "))
    final = average(num1, num2)
    
    print("The average of", num1, "and", num2, "is", final)
    

if __name__ == '__main__':
    main()