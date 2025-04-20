def add_many_numbers(numbers: list)-> int:

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    sum_of_numbers: int = add_many_numbers(numbers)  
    print(sum_of_numbers)  
    

if __name__ == '__main__':
    main()