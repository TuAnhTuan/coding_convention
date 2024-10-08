s = []

#THÊM vào list
def Add_sinhvien(idSV, tenSV, tuoiSV, nganhhoc):
    s.append({'iD':idSV, 'Name':tenSV, 'Tuoi':tuoiSV, 'Major':nganhhoc})
    print(tenSV + " was added!")

def CapNhatSinhVien(ID, newTenSV, newTuoi, newNganhHoc):
    for X in range(len(s)):
            if s[X]['iD'] == ID: s[X]['Name'] = newTenSV; s[X]['Tuoi'] = newTuoi; s[X]['Major'] = newNganhHoc; print("Updated " + newTenSV); break
            else: print("Not found student with ID: " + str(ID))

#Toán tử và Toán hạng cho Cập nhật Tuổi
def tang_tuoi(svID):
    for i in s:
        if i['iD'] == svID:
            i['Tuoi']+=1
            print(i['Name'] + " is now older, current age is " + str(i['Tuoi']))
            break
def Display(): 
    print("Student List");   
    for i in s:print("id:"+str(i['iD'])+" name:"+i['Name']+" age:"+str(i['Tuoi'])+" major:"+i['Major'])

#Add student to list
Add_sinhvien(1,'Nguyen Van A',20,'Cong nghe thong tin')
Add_sinhvien(2,'Nguyen Van B',21,'Hoa hoc')

CapNhatSinhVien(2,'Nguyen Van C',22,'Hoa hoc Ung Dung')


tang_tuoi(2)

Display()
