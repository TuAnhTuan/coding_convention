# Initialize the list of students
students = []

# Add a student to the list
def add_student(student_id, student_name, student_age, major):
    students .append({'id': student_id, 'name': student_name, 'age': student_age, 'major': major})
    print(student_name + " was added!")

# Update a student's information
def update_student(student_id, new_name, new_age, new_major):
    for student in range(len(students)):
        if students[student]['id'] == student_id: 
            students[student]['name'] = new_name
            students[student]['age'] = new_age
            students[student]['major'] = new_major
            print("Updated " + new_name)
            break
    else: 
        print("Not found student with ID: " + str(student_id))

# Increase a student's age by 1
def increment_student_age(student_id):
    for student in students:
        if student['id'] == student_id:
            student['age'] += 1
            print(student['name'] + " is now older, current age is " + str(student['age']))
            break

# Show list Students on Display
def display(): 
    print("Student list")
    for student in students:
        print("id: " + str(student['id']) + " name: " + student['name'] + " age: " + str(student['age']) + " major: " + student['major'])

# Add student to list
add_student(1,'Nguyen Van A',20,'Cong nghe thong tin')
add_student(2,'Nguyen Van B',21,'Hoa hoc')

# Update the information of a student
update_student(2,'Nguyen Van C',22,'Hoa hoc Ung Dung')

# Increment the age of a student
increment_student_age(2)

# Show list Students
display()
