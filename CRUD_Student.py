# Initialize the list of students
s = []

# Add a student to the list
def Add_sinhvien(idSV, tenSV, tuoiSV, nganhhoc):
    s.append({'iD':idSV, 'Name':tenSV, 'Tuoi':tuoiSV, 'Major':nganhhoc})
    print(tenSV + " was added!")

# Update a student's information
def CapNhatSinhVien(ID, newTenSV, newTuoi, newNganhHoc):
    for X in range(len(s)):
            if s[X]['iD'] == ID: s[X]['Name'] = newTenSV; s[X]['Tuoi'] = newTuoi; s[X]['Major'] = newNganhHoc; print("Updated " + newTenSV); break
            else: print("Not found student with ID: " + str(ID))

# Increase a student's age by 1
def tang_tuoi(svID):
    for i in s:
        if i['iD'] == svID:
            i['Tuoi']+=1
            print(i['Name'] + " is now older, current age is " + str(i['Tuoi']))
            break

# Show list Students on Display
def Display(): 
    print("Student List");   
    for i in s:print("id:"+str(i['iD'])+" name:"+i['Name']+" age:"+str(i['Tuoi'])+" major:"+i['Major'])

# Add student to list
Add_sinhvien(1,'Nguyen Van A',20,'Cong nghe thong tin')
Add_sinhvien(2,'Nguyen Van B',21,'Hoa hoc')

# Update the information of a student
CapNhatSinhVien(2,'Nguyen Van C',22,'Hoa hoc Ung Dung')

# Increment the age of a student
tang_tuoi(2)

# Show list Students
Display()
