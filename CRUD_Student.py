# Initialize the list of students
students = []

# Add a student to the list
def Add_sinhvien(student_id, student_name, student_age, major):
    students .append({'id':student_id, 'name':student_name, 'age':student_age, 'major':major})
    print(student_name + " was added!")

# Update a student's information
def CapNhatSinhVien(student_id, new_name, new_age, new_major):
    for student in range(len(students)):
            if students[student]['id'] == student_id: students[student]['name'] = new_name; students[student]['age'] = new_age; students[student]['major'] = new_major; print("Updated " + new_name); break
            else: print("Not found student with ID: " + str(id))

# Increase a student's age by 1
def tang_tuoi(student_id):
    for student in students:
        if student['id'] == student_id:
            student['age']+=1
            print(student['name'] + " is now older, current age is " + str(student['age']))
            break

# Show list Students on Display
def Display(): 
    print("Student List");   
    for student in students:print("id:"+str(student['id'])+" name:"+student['name']+" age:"+str(student['age'])+" major:"+student['major'])

# Add student to list
Add_sinhvien(1,'Nguyen Van A',20,'Cong nghe thong tin')
Add_sinhvien(2,'Nguyen Van B',21,'Hoa hoc')

# Update the information of a student
CapNhatSinhVien(2,'Nguyen Van C',22,'Hoa hoc Ung Dung')

# Increment the age of a student
tang_tuoi(2)

# Show list Students
Display()
