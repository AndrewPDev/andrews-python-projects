"""
Task Brief

The program should allow users to perform the following operations:
Add a new student's information.
Display the list of all students and their information.
Search for a student by name and display their information.
Update a student's information.
Delete a student's information.
Exit the program.
Each student's information should be stored in a tuple containing their name, age, and grade. 
For each operation, provide clear prompts and handle user input appropriately.

Instructions

Adding a New Student

Prompt the user to enter the student's name, age, and grade.
Create a tuple with this information and add it to the list of students.
Confirm to the user that the student has been added successfully.

Displaying All Students

Iterate through the list of students.
For each student, display their name, age, and grade.
Use enumeration to display the index of each student.

Searching for a Student

Prompt the user to enter the name of the student they want to search for.
Iterate through the list of students.
If a student with the given name is found, display their information (name, age, grade).
If not found, inform the user that the student is not in the list.

Updating Student Information

Prompt the user to enter the name of the student they want to update.
Iterate through the list of students.
If a student with the given name is found, prompt the user to enter the new age and grade.
Update the student's information with the new values.
Confirm to the user that the information has been updated successfully.
If the student is not found, inform the user that the student is not in the list.

Deleting Student Information

Prompt the user to enter the name of the student they want to delete.
Iterate through the list of students.
If a student with the given name is found, delete the student's information from the list.
Confirm to the user that the student has been deleted successfully.
If the student is not found, inform the user that the student is not in the list.

Exiting the Program

Provide an option to exit the program gracefully when the user is done.
Display an appropriate message before exiting.
"""

import sys
import os

# Need to manually tell the script where a_lib is located.
sys.path.append( os.path.dirname( os.path.dirname( __file__ ) ) )
from a_lib import *

student_grades = ["A", "B", "C", "D", "E", "F"]

student_index = 0

filename = "save_data.json"

def AddStudent():
    curr_data = LoadData( filename )
    name = input( "Please enter the students name: " )
    while True:
        age = input( "Please enter the students age: " )
        if not IsNum( age ):
            print( "Error: Age must be a number." )
        else:
            break

    while True:
        grade = input( "Please enter the students grade: " )
        if grade.capitalize() not in student_grades and ( grade.lower() != "no grade" ):
            print( "Error: Grade must be between A-F or 'No Grade'" )
        else:
            break
        
    data = ( name, age, grade )
    curr_data = LoadData( filename )
    student_index = len( curr_data ) + 1
    new_data = [student_index, list( data )]
    curr_data.append( new_data )
    SaveData( filename, curr_data )
    print( "-" * 20 )
    print( "Student information save successfully." )
    print( "-" * 20 )

def DisplayStudents():
    curr_data = LoadData( filename )
    if not curr_data:
        print( "Error: No student data found." )
    else:
        print( "List of students:" )
        for index, student in enumerate( curr_data, start = 1 ):
            print( f"{index}. Name: {student[1][0]}, Age: {student[1][1]}, Grade: {student[1][2]}" )

def StudentSearch():
    curr_data = LoadData( filename )
    if not curr_data:
        print( "Error: No student data found." )
        return
    
    name = input( "Please enter the name of the student to search for: " )
    
    matches_found = [
        ( index, student ) for index, student in enumerate( curr_data, start = 1 ) if student[1][0].lower() == name.lower()
    ]
    
    if not matches_found:
        print( "Error: No students found with that given name." )
    else:
        print( "-" * 40 )
        print( f"Students found with the name '{name}':" )
        for index, student in matches_found:
            print( f"{index}. Name: {student[1][0]}, Age: {student[1][1]}, Grade: {student[1][2]}" )
        print( "-" * 40 )

        return matches_found
    
def UpdateStudent():
    curr_data = LoadData( filename )
    if not curr_data:
        print( "Error: No student data found." )
        return
    
    name = input( "Please enter the name of the student to search for: " )
    
    matches_found = [
        ( index, student ) for index, student in enumerate( curr_data, start = 1 ) if student[1][0].lower() == name.lower()
    ]
    
    if not matches_found:
        print( "Error: No students found with that given name." )
    else:
        print( f"Students found with the name '{name}':" )
        for index, student in matches_found:
            print( f"{index}. Name: {student[1][0]}, Age: {student[1][1]}, Grade: {student[1][2]}" )

    while True:
        student = input( "Please enter the number of the student you wish to update: " )
        if not IsNum( student ):
            print( "Error: Please enter a valid number from the list." )
            continue
        student = int( student )
        if 0 <= student < len( matches_found ) + 1:
            break
        else:
            print( "Error: Invalid selection, try again." )
            continue
    
    user_choice = matches_found[student][1]
    print( f"Selected student: Name - {user_choice[1][0]}, Age - {user_choice[1][1]}, Grade - {user_choice[1][2]}" )

    while True:
        age = input( "Please enter the new age: " )
        if not IsNum( age ):
            print( "Error: Age must be a number" )
        else:
            break

    while True:
        grade = input( "Please enter the new grade: " )
        if grade.capitalize() not in student_grades and ( grade.lower() != "no grade" ):
            print( "Error: Grade must be between A-F or 'No Grade'" )
        else:
            break

    user_choice[1][1] = age
    user_choice[1][2] = grade
    SaveData( filename, curr_data )

def DeleteStudent():
    curr_data = LoadData( "save_data.json" )
    if not curr_data:
        print( "Error: No student data found." )
        return
    
    name = input( "Please enter the name of the student to search for: " )
    
    matches_found = [
        ( index, student ) for index, student in enumerate( curr_data, start = 1 ) if student[1][0].lower() == name.lower()
    ]
    
    if not matches_found:
        print( "Error: No students found with that given name." )
    else:
        print( f"Students found with the name '{name}':" )
        for index, student in matches_found:
            print( f"{index}. Name: {student[1][0]}, Age: {student[1][1]}, Grade: {student[1][2]}" )

    while True:
        student = input( "Please enter the number of the student you wish to delete: " )
        if not IsNum( student ):
            print( "Error: Please enter a valid number from the list." )
            continue
        student = int( student )
        if 0 <= student < len( matches_found ) + 1:
            break
        else:
            print( "Error: Invalid selection, try again." )
            continue
    
    selected_index = matches_found[student][0] - 1
    selected_student = curr_data[selected_index]
    print( f"Selected student: Name - {selected_student[1][0]}, Age - {selected_student[1][1]}, Grade - {selected_student[1][2]}" )
    confirmation = input( "Are you sure you want to delete this students information (Yes/No): " )
    if confirmation.lower() == "yes":
        curr_data.pop( selected_index )
        SaveData( "save_data.json", curr_data )
        print( "Students information deleted successfully." )
    else:
        print( "Cancelled. No information was deleted." )

while True:

    print( """
        1. Add a new students information.
        2. Display all stored students information.
        3. Search for a student by name.
        4. Update a students information.
        5. Delete a students information.
        6. Exit the program.
    """ )

    user_choice = input( "Please select an option from the above list: " )

    if not IsNum( user_choice ):
        print( "Error: Please choose a valid number from the list." )
        continue
    
    user_choice = int( user_choice )

    if not 1 <= user_choice <= 6:
        print( "Error: Choice but be between 1-6." )
        continue

    if user_choice == 6:
        print( "Goodbye.." )
        break

    if user_choice == 1:
        AddStudent()
    elif user_choice == 2:
        DisplayStudents()
    elif user_choice == 3:
        StudentSearch()
    elif user_choice == 4:
        UpdateStudent()
    elif user_choice == 5:
        DeleteStudent()