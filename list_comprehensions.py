# # SqStudent Marks Analyzer
std_marks = [45, 78, 96, 23, 67]

min_marks = 40

grace_marks = [mark + 5 if mark < 96 else 100 for mark in std_marks]
passed_stds = [mark for mark in grace_marks if mark >= min_marks]
failed_stds = [mark for mark in grace_marks if mark < min_marks]

print(grace_marks, passed_stds, failed_stds, sep="\n")


#Factorial  Finder
def calculate_factorial(number):
    """
    Calculates factorial of a number using
    list comprehension and loops.
    """

    # Handle negative numbers
    if number < 0:
        return "Factorial does not exist for negative numbers."

    # Handle 0
    if number == 0:
        return 1

    # Generate numbers using list comprehension
    numbers = [num for num in range(1, number + 1)]

    # Calculate factorial
    factorial = 1

    for num in numbers:
        factorial *= num

    return factorial


# User Input
number = int(input("Enter a number: "))

# Function Call
result = calculate_factorial(number)

# Output
print(f"Factorial of {number} is: {result}")