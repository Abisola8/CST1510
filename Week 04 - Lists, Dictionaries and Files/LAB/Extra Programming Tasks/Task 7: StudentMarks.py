"""
## Task 7: EDA Challenge: Student Marks Analysis
Perform Exploratory Data Analysis (EDA) using pure Python lists and functions.
You have been given a multidimensional list representing student performance data.
Each inner list contains: `[Student ID, Name, Math Score, Science Score, English Score]`

```python
student_data = [
    [101, 'Alice', 85, 92, 88],
    [102, 'Bob', 78, 81, 75],
    [103, 'Charlie', 90, 85, 89],
    [104, 'David', 65, 70, 72],
    [105, 'Eve', 88, 95, 90]
]
```

**Tasks:**
1. Write a function or use a list comprehension to calculate the average score for each student and add it as a new element to their list.
2. Find the highest and lowest average scores in the dataset.
3. Filter and print a list of students who have scored above 75 in all subjects.
"""

student_data = [
    [101, 'Alice', 85, 92, 88],
    [102, 'Bob', 78, 81, 75],
    [103, 'Charlie', 90, 85, 89],
    [104, 'David', 65, 70, 72],
    [105, 'Eve', 88, 95, 90]
]

def calc_average(student):
    return (student[2] + student[3] + student[4]) / 3

for student in student_data:
    student.append(calc_average(student))

average = [student[5] for student in student_data]
print(f"Highest average: {max(average)}")
print(f"Lowest average:  {min(average)}")

above_75 = [
    student[1] for student in student_data
    if student[2] > 75 and student[3] > 75 and student[4] > 75 
]
print(f"Students who have scored above 75 in all subjects: {above_75}")