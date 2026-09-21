# ================================================================
# STUDENT MANAGEMENT SYSTEM AND RESULT ANALYZER
# Using Python Built-in Functions and Standard Libraries
# ================================================================

import statistics
from datetime import datetime
import math


# ================================================================
# PROJECT INFORMATION
# ================================================================

print("=" * 70)
print("       STUDENT MANAGEMENT SYSTEM & RESULT ANALYZER")
print("=" * 70)
print("Using Python Built-in Functions and Standard Libraries")
print("=" * 70)


# ================================================================
# DATA
# ================================================================

students = []

subjects = [
    "Mathematics",
    "Python",
    "DBMS",
    "Data Structures",
    "Computer Networks"
]

PASS_MARK = 40


# ================================================================
# CALCULATE GRADE
# ================================================================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


# ================================================================
# CALCULATE RESULT
# ================================================================

def calculate_result(student):

    # Get all marks
    marks = list(student["marks"].values())

    # Total marks
    total = sum(marks)

    # Number of subjects
    number_of_subjects = len(marks)

    # Average using statistics library
    average = statistics.mean(marks)

    # Percentage
    percentage = average

    # Highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

    # Check whether all subjects are passed
    passed = all(
        mark >= PASS_MARK
        for mark in marks
    )

    if passed:
        result = "PASS"
    else:
        result = "FAIL"

    # Calculate grade
    grade = calculate_grade(percentage)

    # Find failed subjects
    failed_subjects = []

    for subject, mark in student["marks"].items():

        if mark < PASS_MARK:
            failed_subjects.append(subject)

    return {
        "total": total,
        "number_of_subjects": number_of_subjects,
        "average": average,
        "percentage": percentage,
        "highest": highest,
        "lowest": lowest,
        "grade": grade,
        "result": result,
        "failed_subjects": failed_subjects
    }


# ================================================================
# ADD STUDENT
# ================================================================

def add_student():

    print("\n" + "=" * 60)
    print("                     ADD STUDENT")
    print("=" * 60)

    # ---------------- Student ID ----------------

    while True:

        try:

            student_id = int(
                input("Enter Student ID: ")
            )

            # Check duplicate ID
            duplicate = False

            for student in students:

                if student["id"] == student_id:

                    duplicate = True
                    break

            if duplicate:

                print(
                    "Student ID already exists."
                )

            else:

                break

        except ValueError:

            print(
                "Please enter a valid numeric ID."
            )

    # ---------------- Student Name ----------------

    while True:

        name = input(
            "Enter Student Name: "
        ).strip()

        if name:

            break

        print(
            "Student name cannot be empty."
        )

    # ---------------- Marks ----------------

    marks = {}

    print("\nEnter marks between 0 and 100.\n")

    for subject in subjects:

        while True:

            try:

                mark = float(
                    input(
                        f"Enter {subject} mark: "
                    )
                )

                if 0 <= mark <= 100:

                    marks[subject] = mark

                    break

                else:

                    print(
                        "Mark must be between 0 and 100."
                    )

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    # ---------------- Date and Time ----------------

    date_added = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    # ---------------- Student Dictionary ----------------

    student = {

        "id": student_id,

        "name": name,

        "marks": marks,

        "date_added": date_added
    }

    students.append(student)

    print("\n" + "-" * 60)
    print("Student added successfully!")
    print("-" * 60)


# ================================================================
# DISPLAY STUDENT RESULT
# ================================================================

def display_student(student):

    result = calculate_result(student)

    print("\n" + "=" * 60)
    print("                   STUDENT RESULT")
    print("=" * 60)

    print(
        f"Student ID   : {student['id']}"
    )

    print(
        f"Student Name : {student['name']}"
    )

    print(
        f"Date Added   : {student['date_added']}"
    )

    print("\nMarks")
    print("-" * 60)

    for subject, mark in student["marks"].items():

        print(
            f"{subject:<25} : {mark}"
        )

    print("-" * 60)

    print(
        f"Total Marks  : {result['total']}"
    )

    print(
        f"Average      : {round(result['average'], 2)}"
    )

    print(
        f"Percentage   : {round(result['percentage'], 2)}%"
    )

    print(
        f"Highest Mark : {result['highest']}"
    )

    print(
        f"Lowest Mark  : {result['lowest']}"
    )

    print(
        f"Grade        : {result['grade']}"
    )

    print(
        f"Result       : {result['result']}"
    )

    # Failed subjects

    if len(result["failed_subjects"]) > 0:

        print("\nFailed Subjects:")

        for subject in result["failed_subjects"]:

            print(
                f"  - {subject}"
            )

    else:

        print(
            "\nFailed Subjects : None"
        )


# ================================================================
# VIEW ALL STUDENTS
# ================================================================

def view_all_students():

    print("\n" + "=" * 85)
    print("                         ALL STUDENTS")
    print("=" * 85)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    print(
        f"{'No.':<5}"
        f"{'ID':<10}"
        f"{'Name':<25}"
        f"{'Percentage':<15}"
        f"{'Grade':<10}"
        f"{'Result':<10}"
    )

    print("-" * 85)

    for number, student in enumerate(
        students,
        start=1
    ):

        result = calculate_result(student)

        print(
            f"{number:<5}"
            f"{student['id']:<10}"
            f"{student['name']:<25}"
            f"{round(result['percentage'], 2):<15}"
            f"{result['grade']:<10}"
            f"{result['result']:<10}"
        )


# ================================================================
# SEARCH STUDENT BY ID
# ================================================================

def search_student():

    print("\n" + "=" * 60)
    print("                  SEARCH STUDENT")
    print("=" * 60)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    try:

        student_id = int(
            input("Enter Student ID: ")
        )

    except ValueError:

        print(
            "Please enter a valid Student ID."
        )

        return

    found = False

    for student in students:

        if student["id"] == student_id:

            display_student(student)

            found = True

            break

    if not found:

        print(
            "\nStudent not found."
        )


# ================================================================
# SEARCH STUDENT BY NAME
# ================================================================

def search_by_name():

    print("\n" + "=" * 60)
    print("                SEARCH BY NAME")
    print("=" * 60)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    name = input(
        "Enter student name: "
    ).strip().lower()

    found = False

    for student in students:

        if name in student["name"].lower():

            display_student(student)

            found = True

    if not found:

        print(
            "\nNo student found with that name."
        )


# ================================================================
# UPDATE STUDENT
# ================================================================

def update_student():

    print("\n" + "=" * 60)
    print("                  UPDATE STUDENT")
    print("=" * 60)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    try:

        student_id = int(
            input("Enter Student ID: ")
        )

    except ValueError:

        print(
            "Please enter a valid Student ID."
        )

        return

    for student in students:

        if student["id"] == student_id:

            print(
                f"\nCurrent Name: {student['name']}"
            )

            new_name = input(
                "Enter new name "
                "(press Enter to keep current): "
            ).strip()

            if new_name:

                student["name"] = new_name

            print("\nEnter updated marks.")

            for subject in subjects:

                while True:

                    try:

                        mark = float(
                            input(
                                f"{subject} "
                                f"[Current: "
                                f"{student['marks'][subject]}]: "
                            )
                        )

                        if 0 <= mark <= 100:

                            student["marks"][subject] = mark

                            break

                        else:

                            print(
                                "Mark must be between 0 and 100."
                            )

                    except ValueError:

                        print(
                            "Please enter a valid number."
                        )

            print(
                "\nStudent updated successfully!"
            )

            return

    print(
        "\nStudent not found."
    )


# ================================================================
# DELETE STUDENT
# ================================================================

def delete_student():

    print("\n" + "=" * 60)
    print("                  DELETE STUDENT")
    print("=" * 60)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    try:

        student_id = int(
            input("Enter Student ID: ")
        )

    except ValueError:

        print(
            "Please enter a valid Student ID."
        )

        return

    for student in students:

        if student["id"] == student_id:

            print(
                f"\nStudent Found: {student['name']}"
            )

            confirmation = input(
                "Are you sure? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":

                students.remove(student)

                print(
                    "Student deleted successfully!"
                )

            else:

                print(
                    "Deletion cancelled."
                )

            return

    print(
        "\nStudent not found."
    )


# ================================================================
# CLASS STATISTICS
# ================================================================

def class_statistics():

    print("\n" + "=" * 65)
    print("                    CLASS STATISTICS")
    print("=" * 65)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    percentages = []

    passed_students = 0

    failed_students = 0

    for student in students:

        result = calculate_result(student)

        percentages.append(
            result["percentage"]
        )

        if result["result"] == "PASS":

            passed_students += 1

        else:

            failed_students += 1

    number_of_students = len(students)

    # Statistics library

    class_average = statistics.mean(
        percentages
    )

    median_percentage = statistics.median(
        percentages
    )

    highest_percentage = max(
        percentages
    )

    lowest_percentage = min(
        percentages
    )

    # Pass and fail percentage

    pass_percentage = (
        passed_students /
        number_of_students
    ) * 100

    fail_percentage = (
        failed_students /
        number_of_students
    ) * 100

    print(
        f"Number of Students : {number_of_students}"
    )

    print(
        f"Class Average      : "
        f"{round(class_average, 2)}%"
    )

    print(
        f"Median Percentage  : "
        f"{round(median_percentage, 2)}%"
    )

    print(
        f"Highest Percentage : "
        f"{round(highest_percentage, 2)}%"
    )

    print(
        f"Lowest Percentage  : "
        f"{round(lowest_percentage, 2)}%"
    )

    print(
        f"Passed Students    : "
        f"{passed_students}"
    )

    print(
        f"Failed Students    : "
        f"{failed_students}"
    )

    print(
        f"Pass Percentage    : "
        f"{round(pass_percentage, 2)}%"
    )

    print(
        f"Fail Percentage    : "
        f"{round(fail_percentage, 2)}%"
    )


# ================================================================
# STUDENT RANKING
# ================================================================

def student_ranking():

    print("\n" + "=" * 85)
    print("                       STUDENT RANKING")
    print("=" * 85)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    ranking = sorted(
        students,
        key=lambda student:
        calculate_result(student)["percentage"],
        reverse=True
    )

    print(
        f"{'Rank':<8}"
        f"{'ID':<10}"
        f"{'Name':<25}"
        f"{'Percentage':<15}"
        f"{'Grade':<10}"
        f"{'Result':<10}"
    )

    print("-" * 85)

    for rank, student in enumerate(
        ranking,
        start=1
    ):

        result = calculate_result(student)

        print(
            f"{rank:<8}"
            f"{student['id']:<10}"
            f"{student['name']:<25}"
            f"{round(result['percentage'], 2):<15}"
            f"{result['grade']:<10}"
            f"{result['result']:<10}"
        )


# ================================================================
# TOP STUDENT
# ================================================================

def top_student():

    print("\n" + "=" * 60)
    print("                       TOP STUDENT")
    print("=" * 60)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    top = max(
        students,
        key=lambda student:
        calculate_result(student)["percentage"]
    )

    result = calculate_result(top)

    print(
        f"Student ID : {top['id']}"
    )

    print(
        f"Name       : {top['name']}"
    )

    print(
        f"Percentage : "
        f"{round(result['percentage'], 2)}%"
    )

    print(
        f"Grade      : {result['grade']}"
    )


# ================================================================
# SUBJECT-WISE ANALYSIS
# ================================================================

def subject_analysis():

    print("\n" + "=" * 65)
    print("                   SUBJECT-WISE ANALYSIS")
    print("=" * 65)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    for subject in subjects:

        marks = []

        for student in students:

            marks.append(
                student["marks"][subject]
            )

        average = statistics.mean(
            marks
        )

        highest = max(marks)

        lowest = min(marks)

        print("\n" + subject)

        print(
            f"Average : {round(average, 2)}"
        )

        print(
            f"Highest : {highest}"
        )

        print(
            f"Lowest  : {lowest}"
        )


# ================================================================
# OVERALL REPORT
# ================================================================

def overall_report():

    print("\n" + "=" * 70)
    print("                    OVERALL REPORT")
    print("=" * 70)

    if len(students) == 0:

        print(
            "No student records available."
        )

        return

    total_students = len(students)

    passed = 0

    failed = 0

    percentages = []

    for student in students:

        result = calculate_result(student)

        percentages.append(
            result["percentage"]
        )

        if result["result"] == "PASS":

            passed += 1

        else:

            failed += 1

    average = statistics.mean(
        percentages
    )

    pass_rate = (
        passed / total_students
    ) * 100

    fail_rate = (
        failed / total_students
    ) * 100

    print(
        f"Total Students : {total_students}"
    )

    print(
        f"Passed         : {passed}"
    )

    print(
        f"Failed         : {failed}"
    )

    print(
        f"Class Average  : {round(average, 2)}%"
    )

    print(
        f"Pass Rate      : {round(pass_rate, 2)}%"
    )

    print(
        f"Fail Rate      : {round(fail_rate, 2)}%"
    )


# ================================================================
# MAIN MENU
# ================================================================

def main_menu():

    while True:

        print("\n")

        print("=" * 70)
        print(
            "       STUDENT MANAGEMENT & RESULT ANALYZER"
        )
        print("=" * 70)

        print("1.  Add Student")
        print("2.  View All Students")
        print("3.  Search Student by ID")
        print("4.  Search Student by Name")
        print("5.  View Student Result")
        print("6.  Update Student")
        print("7.  Delete Student")
        print("8.  Class Statistics")
        print("9.  Student Ranking")
        print("10. Top Student")
        print("11. Subject-wise Analysis")
        print("12. Overall Report")
        print("13. Exit")

        print("=" * 70)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            view_all_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            search_by_name()

        elif choice == "5":

            search_student()

        elif choice == "6":

            update_student()

        elif choice == "7":

            delete_student()

        elif choice == "8":

            class_statistics()

        elif choice == "9":

            student_ranking()

        elif choice == "10":

            top_student()

        elif choice == "11":

            subject_analysis()

        elif choice == "12":

            overall_report()

        elif choice == "13":

            print("\n" + "=" * 60)

            print(
                "Thank you for using the system!"
            )

            print(
                "Program terminated successfully."
            )

            print("=" * 60)

            break

        else:

            print(
                "\nInvalid choice!"
            )

            print(
                "Please select a number from 1 to 13."
            )


# ================================================================
# START PROJECT
# ================================================================

print("\nProject initialized successfully.")

print(
    "\nLibraries used:"
)

print(
    "1. statistics"
)

print(
    "2. datetime"
)

print(
    "3. math"
)

print(
    "\nPython built-in functions used:"
)

print(
    "sum(), len(), max(), min(), round(), "
    "sorted(), enumerate(), all(), list(), "
    "int(), float(), input(), print()"
)

print(
    "\nStarting Student Management System..."
)

main_menu()