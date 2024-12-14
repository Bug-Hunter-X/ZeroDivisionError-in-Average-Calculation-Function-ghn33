def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example of the function working
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Example that causes ZeroDivisionError
empty_list = []
average = calculate_average(empty_list)
print(f"The average is: {average}")#This will not throw an error now