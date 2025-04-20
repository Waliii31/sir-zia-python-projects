def in_range(n, low, high):
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):
        print(f"{n} is in range {low} to {high}.")
    else:
        print(f"{n} is NOT in range {low} to {high}.")

if __name__ == '__main__':
    main()
