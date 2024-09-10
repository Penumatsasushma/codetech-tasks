# Student Grade Tracker

def get_letter_grade(average):
    if average >= 90:
        return 'A', 4.0
    elif average >= 80:
        return 'B', 3.0
    elif average >= 70:
        return 'C', 2.0
    elif average >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def grade_tracker():
    # Dictionary to store subject names and their corresponding grades
    grades = {}

    while True:
        # Ask the user to input subject and grade
        subject = input("Enter the subject (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            grades[subject] = grade
        except ValueError:
            print("Invalid input. Please enter a valid number for the grade.")

    if len(grades) == 0:
        print("No grades entered.")
        return

    # Calculate the average grade
    total = sum(grades.values())
    average = total / len(grades)

    # Get letter grade and GPA based on average
    letter_grade, gpa = get_letter_grade(average)

    # Display results
    print("\nGrades entered:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

# Run the grade tracker
grade_tracker()
