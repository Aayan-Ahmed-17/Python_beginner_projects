# SqStudent Marks Analyzer
std_marks = [45, 78, 96, 23, 67]

min_marks = 40

grace_marks = [mark + 5 if mark < 96 else 100 for mark in std_marks]
passed_stds = [mark for mark in grace_marks if mark >= min_marks]
failed_stds = [mark for mark in grace_marks if mark < min_marks]

print(grace_marks, passed_stds, failed_stds, sep="\n")