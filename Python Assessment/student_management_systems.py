welcome = """
                                                WELCOME TO STUDENT MANAGEMENT SYSTEM

                                                1) COUNSELLOR

                                                2) FACULTY

                                                3) STUDENT
"""

counsellor_display = """

                                                WELCOME COUNSELLOR

                                                1) ADD STUDENT

                                                2) REMOVE STUDENT

                                                3) VIWE ALL STUDENT

                                                4) VIWE SPECIFIC STUDEN
"""

faculty_display = """

                                                WELCOME FACULTY

                                                1) ADD MARKS TO STUDENT

                                                2) VIWE ALL STUDENT
"""

student_display = """

                                                WELCOME STUDENT
"""


def faculty():
    pass
def student():
    pass

student_main = {}

status = True
while status :
    
    student_details = {}

    print(welcome)
    role = int(input("Select Role By Entering Role : "))
    
    match role:

        case 1:
            counsellor_status = True
            while counsellor_status : 
                print(counsellor_display)
                counsellor_role = int(input("Select Operation : "))
                
                if counsellor_role == 1:

                    rollno = int(input("Enter Roll No. : "))

                    if rollno in student_main :
                        print("Roll No. Already Exist")
                
                    else:
                        student_subject = {}

                        print("Roll No. Available for Register ")

                        fname = input("Enter First Name : ").upper()
                        lname = input("Enter Last Name : ").upper()
                        contact = int(input("Enter Contact No. : "))
                        student_details['fname'] = fname
                        student_details['lname'] = lname
                        student_details['contact'] = contact
                        
                        add_subject = True
                        while add_subject:
                            
                            student_marks={}

                            subject = input("Enter Subject Name : ").upper()
                            marks = int(input("Enter Marks : "))
                            fees = int(input("Enter Fees : "))
                            
                            student_marks['marks'] = marks
                            student_marks['fees'] = fees
                            
                            student_subject[subject]=student_marks
                            student_details['subject'] = student_subject

                            check = input("Add More Subjects (y/n) : ").upper()
                            if check == "Y":
                                add_subject = True
                            elif check == "N":
                                add_subject = False
                            else:
                                print("Enter Valid Input")
                                
                        faculty = input("Enter Faculty Name : ").upper()
                        student_details['faculty'] = faculty
                                
                        student_main[rollno] = student_details
                        print("Student Registration Succsefully Completed :)")
                elif counsellor_role == 2:
                    pass
                elif counsellor_role == 3:
                    pass
                elif counsellor_role == 4: 
                    pass
                else :
                    print("Enter Valid Input")

                check = input("Perform More Operaion (y/n) : ").upper()
                if check == "Y":
                    counsellor_status = True
                elif check == "N":
                    counsellor_status = False
                else:
                    print("Enter Valid Input")

        case 2:
            print(faculty_display)
            faculty()
        case 3 :
            print(student_display)
            student()
        case _:
            print("Enter Valid Input")


    check = input("Want to Exit (y/n) : ").upper()
    if check == "Y":
        status = False
    elif check == "N":
        status = True
    else:
        print("Enter Valid Input")