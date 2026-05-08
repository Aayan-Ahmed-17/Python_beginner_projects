# # SqStudent Marks Analyzer
# std_marks = [45, 78, 96, 23, 67]

# min_marks = 40

# grace_marks = [mark + 5 if mark < 96 else 100 for mark in std_marks]
# passed_stds = [mark for mark in grace_marks if mark >= min_marks]
# failed_stds = [mark for mark in grace_marks if mark < min_marks]

# print(grace_marks, passed_stds, failed_stds, sep="\n")


#Factorial  Finder
def calculate_factorial():
    u_num = int(input("Enter a number: "))
    
    # if u_num <= 1:
    #     print("Please Enter number greater than 1")
        
    multipliers = [num for num in range(u_num, 0, -1)]
    print(multipliers)
    factorial = [num * num for num in multipliers]
    
calculate_factorial()