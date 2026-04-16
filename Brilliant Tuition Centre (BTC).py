import os

# File names
USER_FILE = "users.txt"
TUTOR_FILE = "tutors.txt"
INCOME_FILE = "income.txt"
STUDENT_FILE = "students.txt"
PAYMENT_FILE = "payments.txt"
REQUEST_FILE = "requests.txt"
CLASS_FILE = "classes.txt"

# Ensure required files exist with initial data
def initialize_files():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as file:
            file.write("Amin,amin123,admin\n")  # Default admin user
            file.write("Ray,ray123,receptionist\n")  # Default receptionist user
            file.write("Jane,jane123,tutor\n")  
            file.write("Jack,jack123,tutor\n")
            file.write("Emma,emma123,tutor\n") 
            file.write("Sofia,sofia123,tutor\n")
            file.write("Nancy,nancy123,tutor\n")  
            file.write("Bob,bob123,tutor\n")
            file.write("Elise,elise123,tutor\n")
            
    if not os.path.exists(TUTOR_FILE):
        with open(TUTOR_FILE, "w") as file:
            file.write("Jane,jane123,Malay,Form3\n")
            file.write("Jack,jack123,English,Form4\n")
            file.write("Emma,emma123,Chinese,Form2\n")
            file.write("Sofia,sofia123,Science,Form1\n")
            file.write("Nancy,nancy123,Physics,Form4\n")
            file.write("Bob,bob123,Mathematics,Form2\n")
            file.write("Elise,elise123,Chemistry,Form5\n")
    
    if not os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "w") as file:
            file.write("Form1,Science,RM50\n")
            file.write("Form2,Chinese,RM65\n")
            file.write("Form2,Mathematics,RM50\n")
            file.write("Form3,Malay,RM70\n")
            file.write("Form4,English,RM60\n")
            file.write("Form4,Physics,RM55\n")
            file.write("Form5,Chemistry,RM55\n")
    
    if not os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "w") as file:
            file.write("John,john123,Science,,,Form1,120123010123,john@gmail.com,01114356789,Johor,May\n")
            file.write("Ben,ben123,Chinese,Mathematics,,Form2,110123060223,ben@gmail.com,0143257689,Pahang,May\n")
            file.write("Ivy,ivy123,Malay,,,Form3,100123130146,ivy@gmail.com,0183456789,Sarawak,May\n")
            file.write("Emily,emily123,English,Physics,,Form4,090123070348,emily@gmail.com,0165432789,Penang,May\n")
            file.write("Joseph,joseph123,Chemistry,,,Form5,080123020569,joseph@gmail.com,0137654389,Kedah,May\n")

    if not os.path.exists(PAYMENT_FILE):
        with open(PAYMENT_FILE, "w") as file:
            file.write("John,RM1000,2025-04-01\n")  
            file.write("Ben,RM250,2025-02-25\n")  
            file.write("Ivy,RM300,2025-03-09\n")
            file.write("Emily,RM250,2025-01-18\n")  
            file.write("Joseph,RM300,2025-1-23\n")

    if not os.path.exists(CLASS_FILE):
        with open(CLASS_FILE, "w") as file:
            file.write("Jane,Malay,Form3,RM70,Monday\n")
            file.write("Jack,English,Form4,RM60,Tuesday\n")
            file.write("Emma,Chinese,Form2,RM65,Wednesday\n")
            file.write("Sofia,Science,Form1,RM50,Thursday\n")
            file.write("Nancy,Physics,Form4,RM55,Friday\n")
            file.write("Bob,Mathematics,Form2,RM50,Saturday\n")
            file.write("Elise,Chemistry,Form5,RM55,Sunday\n")
            
    if not os.path.exists(REQUEST_FILE):
        with open(REQUEST_FILE, "w") as file:
            file.write("John,Mathematics,Science\n")
            file.write("Ben,English,Malay\n")
            file.write("Ivy,Mathematics\n")
            file.write("Emily,Chinese\n")
            file.write("Joseph,Chemistry,Physics\n")
        
# Load all users from three files (user.txt, tutor.txt, student.txt)
def load_users():
    users = {}

    # Load users from users.txt (admin, receptionist, tutor)
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                username, password, role = line.strip().split(",")
                users[username] = {"password": password, "role": role}
    
    # Load tutors from tutors.txt and include subject and level
    if os.path.exists("tutors.txt"):
        with open("tutors.txt", "r") as file:
            for line in file:
                values = line.strip().split(",")
                if len(values) == 4:  
                    username, password, subject, level = values
                    users[username] = {"password": password, "role": "tutor", "subject": subject, "level": level}

    return users

#Save tutor and user data
def save_user(username, password, role, subject=None, level=None):
    if role == "tutor":
        with open(TUTOR_FILE, "a") as file:
            file.write(f"{username},{password},{subject},{level}\n")
    else:
        with open(USER_FILE, "a") as file:
            file.write(f"{username},{password},{role}\n")

#Login system with maximum 3 login attempts          
def login():
    users = load_users()
    students = load_students()  
    attempts = 3  
    
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Check for admin, receptionist, or tutor roles
        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login successful!")
            
            if role == "tutor":
                return role, username
            else:
                return role, None

        # Check for student role
        elif username in students and students[username]["password"] == password:
            print(f"Login successful!")
            return "student", username  

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid credentials. You have {attempts} attempts remaining.")
            else:
                print("Login failed. Too many attempts.")
                return None, None  

    # If login fails after 3 attempts, return None, None and go back to main menu
    print("Returning to the Welcome page...")
    return None, None

#ADMIN
def admin_menu():
    while True:
        print(f"\nWelcome Admin!\n")
        print("1. Register Tutor")
        print("2. Delete Tutor")
        print("3. View Income Report")
        print("4. Register Receptionist")
        print("5. Delete Receptionist")  
        print("6. Update Admin Profile")
        print("7. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_tutor()
        elif choice == "2":
            delete_tutor()
        elif choice == "3":
            view_income_report()
        elif choice == "4":
            register_receptionist()
        elif choice == "5":
            delete_receptionist()  
        elif choice == "6":
            update_admin_profile()
        elif choice == "7":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")
            
#Define function register tutor
def register_tutor():
    name = input("Enter tutor's name: ")
    password = input("Enter a password for tutor registration: ")
    subject = input("Enter subject: ")
    level = input("Enter level (Form1 - Form5): ")

    save_user(name, password, "tutor", subject, level)

    print(f"Tutor {name} registered successfully!")

#Define function delete tutor
def delete_tutor():
    name = input("Enter tutor's name to delete: ")
    if os.path.exists(TUTOR_FILE):
        with open(TUTOR_FILE, "r") as file:
            tutors = file.readlines()
        with open(TUTOR_FILE, "w") as file:
            found = False
            for tutor in tutors:
                if not tutor.startswith(name):
                    file.write(tutor)
                else:
                    found = True
            if found:
                print(f"Tutor {name} deleted successfully!")
            else:
                print("Tutor not found.")
                
#Define function view income report               
def view_income_report():
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "r") as file:
            print("\n--- Monthly Income Report ---")
            print(file.read())
    else:
        print("\nNo income data available.")

#Define function register receptionist
def register_receptionist():
    username = input("Enter receptionist username: ")
    password = input("Enter receptionist password: ")
    save_user(username, password, "receptionist")
    print(f"Receptionist {username} registered successfully!")

#Define function delete receptionist
def delete_receptionist():
    username = input("Enter receptionist username to delete: ")
    users = load_users()
    
    if username in users and users[username]["role"] == "receptionist":
        del users[username]  # Remove the receptionist from the users dictionary
        with open(USER_FILE, "w") as file:
            for user, details in users.items():
                file.write(f"{user},{details['password']},{details['role']}\n")
        print(f"Receptionist {username} deleted successfully!")
    else:
        print("Receptionist not found.")

#Define function update admin profile       
def update_admin_profile():
    users = load_users()
    admin_username = input("Enter your current username: ")
    if admin_username in users and users[admin_username]["role"] == "admin":
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        users[new_username] = {"password": new_password, "role": "admin"}
        del users[admin_username]
        with open(USER_FILE, "w") as file:
            for user, details in users.items():
                file.write(f"{user},{details['password']},{details['role']}\n")
        print("Admin profile updated successfully!")
    else:
        print("Admin user not found.")


#RECEPTIONIST
def receptionist_menu():
    while True:
        print(f"\nWelcome Receptionist!\n")
        print("Receptionist Menu:")
        print("1. Register Student")
        print("2. Accept Payment and Generate Receipt")
        print("3. Delete Student")
        print("4. Update Student Subjects")  
        print("5. Update Profile")
        print("6. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_student()  
        elif choice == "2":
            accept_payment()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_student_subjects()  
        elif choice == "5":
            update_receptionist_profile()
        elif choice == "6":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")

#Define function register student
def register_student():
    
    name = input("Enter student's name: ")

    
    password = input("Enter a password for student registration: ")
    level = input("Enter student's level (Form1 - Form5): ")
    ic_or_passport = input("Enter student's IC/Passport number: ")
    email = input("Enter student's email: ")
    contact_number = input("Enter student's contact number: ")
    address = input("Enter student's address: ")

 
    enrollment_month = input("Enter the month of enrollment: ")
    
    subject1 = input("Enter subject 1 (required): ")
    if not subject1:
        print("Subject 1 is required!")
        return

    subject2 = input("Enter subject 2 (optional, 0 to skip): ")
    if subject2 == "0":
        subject2 = ""
        subject3 = ""
    else:
        subject3 = input("Enter subject 3 (optional, 0 to skip): ")
        if subject3 == "0":
            subject3 = ""

    # Save student details into the 'students.txt' file
    with open(STUDENT_FILE, "a") as file:
        file.write(f"{name},{password},{subject1},{subject2},{subject3},{level},{ic_or_passport},{email},{contact_number},{address},{enrollment_month}\n")

    print(f"Student {name} registered successfully!")

#Define function delete student
def delete_student():
    name = input("Enter student's name to delete: ")
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            students = file.readlines()
        with open(STUDENT_FILE, "w") as file:
            found = False
            for student in students:
                if not student.startswith(name):
                    file.write(student)
                else:
                    found = True
            if found:
                print(f"Student {name} deleted successfully!")
            else:
                print("Student not found.")

#Define function update student subject
def update_student_subjects():
    student_name = input("Enter student's name to update subjects: ")
    found = False
    updated_data = []

    with open(STUDENT_FILE, "r") as file:
        students = file.readlines()

    for student in students:
        student_info = student.strip().split(",")

        if student_info[0].lower() == student_name.lower(): 
            found = True
            print(f"\nStudent Found: {student_info[0]}")

            if len(student_info) >= 9:
                name, password, subject1, subject2, subject3, level, ic_or_passport, email, contact_number, address, enrollment_month = student_info[:11]

                 # Filter out empty subjects
                current_subjects = [subject for subject in [subject1, subject2, subject3] if subject]
                print(f"Current Enrollment: {', '.join(current_subjects)}") 

                # Ask for new subjects (Subject 1 is required, Subject 2 and 3 are optional)
                subject1 = input("Enter subject 1 (required): ").strip()
                if not subject1: 
                    print("Subject 1 is required!")
                    return

                subject2 = input("Enter subject 2 (optional, 0 to skip): ").strip()
                if subject2 == "0":
                    subject2 = ""  
                    subject3 = ""  
                else:
                    subject3 = input("Enter subject 3 (optional, 0 to skip): ").strip()
                    if subject3 == "0":
                        subject3 = ""  

                # Prepare updated student info
                updated_student_info = [name, password, subject1, subject2, subject3, level, ic_or_passport, email, contact_number, address, enrollment_month]

                # Rebuild the student line
                updated_data.append(",".join(updated_student_info) + "\n")
            else:
                print(f"Student {student_name} does not have enough information to update.")
                return
        # Keep all other students unchanged 
        else:
            updated_data.append(student)  

    # If student was not found
    if not found:
        print("Student not found!")
        return

    # Write the updated data back to the file
    with open(STUDENT_FILE, "w") as file:
        file.writelines(updated_data)

    print(f"Student {student_name}'s subjects updated successfully!")

#Define function accept payment                
def accept_payment():
    student_name = input("Enter student's name for payment: ")
    amount = input("Enter payment amount: ")
    date = input("Enter payment date (YYYY-MM-DD): ")
    with open(PAYMENT_FILE, "a") as file:
        file.write(f"{student_name},{amount},{date}\n")
    print(f"Payment of {amount} received from {student_name}.")

#Define function update receptionist profile
def update_receptionist_profile():
    users = load_users()
    receptionist_username = input("Enter your current username: ")
    if receptionist_username in users and users[receptionist_username]["role"] == "receptionist":
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        users[new_username] = {"password": new_password, "role": "receptionist"}
        del users[receptionist_username]
        with open(USER_FILE, "w") as file:
            for user, details in users.items():
                file.write(f"{user},{details['password']},{details['role']}\n")
        print("Receptionist profile updated successfully!")
    else:
        print("Receptionist user not found.")

# Tutor menu
def tutor_menu(tutor_name):
    found = False
    subject = ""
    level = ""

    # Load tutors from tutors.txt
    if os.path.exists("tutors.txt"):
        with open("tutors.txt", "r") as file:
            for line in file:
                tutor_info = line.strip().split(",")
                if tutor_info[0].lower() == tutor_name.lower():  
                    subject = tutor_info[2]  
                    level = tutor_info[3]    
                    found = True
                    break

    while True:
        if found:
            print(f"\nWelcome Tutor! You are teaching {subject} for {level}.")
        else:
            print(f"Error: Tutor not found.")
            return
        
        print("\nTutor Menu:")
        print("1. Add Class Information")
        print("2. Update Class Information")
        print("3. Delete Class Information")
        print("4. View Students Enrolled")
        print("5. Update Profile")
        print("6. Logout")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_class_information(tutor_name)
        elif choice == "2":
            classes = load_classes()  
            update_class_information(tutor_name, classes)  
        elif choice == "3":
            delete_class_information(tutor_name)
        elif choice == "4":
            view_students_enrolled(tutor_name)
        elif choice == "5":
            update_tutor_profile()
        elif choice == "6":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Please try again.")
            
#Define Function load classes
def load_classes():
    classes = {}
    if os.path.exists("classes.txt"):
        with open("classes.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    tutor, subject, level, charges, schedule = parts
                    if tutor not in classes:
                        classes[tutor] = []
                    classes[tutor].append({
                        "subject": subject,
                        "level": level,
                        "charges": charges,
                        "schedule": schedule
                    })
    return classes

# Define Function Add class information function
def add_class_information(tutor_name):
    subject_name = input("Enter the subject name: ")
    charges = input("Enter the charges for the class: ")
    schedule = input("Enter the class schedule: ")
    level = input("Enter the subject level (Form1-Form5): ")  

    # Save class information to a file (e.g., 'classes.txt')
    with open("classes.txt", "a") as file:
        file.write(f"{tutor_name},{subject_name},{level},{charges},{schedule}\n")  

    print(f"Class information for {subject_name} added successfully!")

#Define Function Update class information function
def update_class_information(tutor_name, classes):
    if tutor_name not in classes or not classes[tutor_name]:
        print("You have no classes to update.")
        return

    print("Your current classes:")
    for i, cls in enumerate(classes[tutor_name], 1):
        print(f"{i}. {cls['subject']} - {cls['charges']} - {cls['schedule']}")

    try:
        choice = int(input("Enter the number of the class you want to update: ")) - 1
        if 0 <= choice < len(classes[tutor_name]):
            subject = input("Enter new subject name: ")
            level = input("Enter new level: ")
            charges = input("Enter new charges: ")
            schedule = input("Enter new schedule: ")

            classes[tutor_name][choice] = {
                "subject": subject,
                "level": level,
                "charges": charges,
                "schedule": schedule
            }

            save_classes(classes)
            print("Class information updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
#Define Function Save Classes
def save_classes(classes):
    with open("classes.txt", "w") as file:
        for tutor, class_list in classes.items():
            for cls in class_list:
                file.write(f"{tutor},{cls['subject']},{cls['level']},{cls['charges']},{cls['schedule']}\n")
        
# Define Function Delete class information
def delete_class_information(tutor_name):
    classes = load_classes()  

    if tutor_name not in classes or not classes[tutor_name]:
        print("You have no classes to delete.")
        return

    print("Your current classes:")
    for i, cls in enumerate(classes[tutor_name], 1):
        print(f"{i}. {cls['subject']} - {cls['charges']} - {cls['schedule']}")

    try:
        choice = int(input("Enter the number of the class you want to delete: ")) - 1
        if 0 <= choice < len(classes[tutor_name]):
            deleted_class = classes[tutor_name].pop(choice)
            print(f"Deleted class: {deleted_class['subject']}")

            # Save the updated class list
            save_classes(classes)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Define Function View enrolled students for a subject 
def view_students_enrolled(tutor_name):
    users = load_users()
    tutor_info = users.get(tutor_name)
    
    if not tutor_info or tutor_info["role"] != "tutor":
        print("Tutor not found.")
        return

    tutor_subjects = [tutor_info.get("subject")]  
    tutor_level = tutor_info.get("level")
    
    students_enrolled = []

    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            for line in file:
                student_info = line.strip().split(",")
                
                # Extract the student's level and subjects
                student_level = student_info[5]  
                student_subjects = student_info[2:5]  
                
                # Check if the tutor's subject matches any of the student's subjects and if the levels match
                if tutor_level == student_level and any(subject == tutor_info['subject'] for subject in student_subjects):
                    students_enrolled.append(student_info[0])

    if students_enrolled:
        print("\nList of students enrolled in your subject(s):")
        for student in students_enrolled:
            print(student)
    else:
        print("No students enrolled in your subjects.")

# Define Function Update tutor profile 
def update_tutor_profile():
    users = load_users()  
    tutor_username = input("Enter your current username: ")

    # Proceed if the user is found and is a tutor
    if tutor_username in users and users[tutor_username]["role"] == "tutor":
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        new_subject = input("Enter new subject: ")
        new_level = input("Enter new level: ")  

        # Update tutor information
        users[new_username] = {"password": new_password, "role": "tutor", "subject": new_subject, "level": new_level}
        del users[tutor_username]  

        # Save updated users to file (includes both admin, receptionist, and tutors)
        with open(USER_FILE, "w") as file:
            for username, details in users.items():
                file.write(f"{username},{details['password']},{details['role']}\n")

        # Update tutors.txt file with the new subject and level info
        with open("tutors.txt", "w") as file:
            for username, details in users.items():
                if details["role"] == "tutor":
                    file.write(f"{username},{details['password']},{details['subject']},{details['level']}\n")

        print("Tutor profile updated successfully!")
    else:
        print("Tutor user not found.")
        
# Student menu
def student_menu(student_name):
    while True:
        print(f"\nWelcome Student!\n")
        print("Student Menu:")
        print("1. View Class Schedule")
        print("2. Request Subject Change")
        print("3. Delete Subject Change Request")
        print("4. View Payment Status")
        print("5. Update Profile")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_class_schedule(student_name)
        elif choice == "2":
            request_subject_change(student_name)
        elif choice == "3":
            delete_subject_request(student_name)
        elif choice == "4":
            view_payment_status(student_name)
        elif choice == "5":
            update_student_profile()  
        elif choice == "6":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Please try again.")

# View class schedule
def view_class_schedule(student_name):
    found = False
    student_level = ""
    enrolled_subjects = []

    # Load student data to get the enrolled subjects and form level
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            for line in file:
                student_info = line.strip().split(",")
                if student_info[0].lower() == student_name.lower():
                    enrolled_subjects = [subject.strip() for subject in student_info[2:5]]  
                    student_level = student_info[5].strip()  
                    found = True
                    break

    if not found:
        print("Student not found!")
        return

    found_schedule = False
    if os.path.exists("classes.txt"):
        with open("classes.txt", "r") as file:
            print(f"\nYour Class Schedule:")
            for line in file:
                tutor, subject, level, charges, schedule = line.strip().split(",")

                # Ensure no leading/trailing spaces in subject and level
                subject = subject.strip()
                level = level.strip()

                # Check if the subject is in the student's enrolled subjects and the level matches
                if subject in enrolled_subjects and level == student_level:
                    print(f"{subject} by {tutor} | Charges: {charges} | Schedule: {schedule}")
                    found_schedule = True

    if not found_schedule:
        print("No class schedule found for your enrolled subjects.")

# Define function to check enrollment
def is_student_enrolled(student_name, subject):
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            for line in file:
                student_info = line.strip().split(",")
                if student_info[0] == student_name and subject == student_info[2]:  # subject is 3rd column
                    return True
    return False

# Request subject change
def request_subject_change(student_name):
    subject = input("Enter the subject you want to switch to: ")
    with open(REQUEST_FILE, "a") as file:
        file.write(f"{student_name},{subject}\n")
    print("Subject change request submitted.")

# Delete pending subject change request
def delete_subject_request(student_name):
    if not os.path.exists(REQUEST_FILE):
        print("No subject change requests found.")
        return

    updated_requests = []
    deleted = False
    with open(REQUEST_FILE, "r") as file:
        for line in file:
            if not line.startswith(student_name + ","):
                updated_requests.append(line)
            else:
                deleted = True

    with open(REQUEST_FILE, "w") as file:
        file.writelines(updated_requests)

    if deleted:
        print("Your subject change request has been deleted.")
    else:
        print("No request found under your name.")

#Define function view payment status
def view_payment_status(student_name):
    try:
        with open("payments.txt", "r") as file:
            payments = []
            for line in file:
                line = line.strip()
                payment_info = line.split(",")

                # Expecting 3 values: username, amount, date
                if len(payment_info) == 3:
                    name, amount, date = payment_info
                    if name == student_name:
                        payments.append((amount, date))
                else:
                    print(f"Skipping invalid line: {line}")

            if payments:
                print(f"\nYour Payment History:")
                for i, (amount, date) in enumerate(payments, 1):
                    print(f"{i}. Amount: {amount} | Date: {date}")
            else:
                print("No payment records found for you.")

    except FileNotFoundError:
        print("Payments file not found.")

#Define function update student profile
def update_student_profile():
    students = load_students()  
    student_username = input("Enter your current username: ")

# Ask for new details
    if student_username in students:
        new_username = input(f"Enter new username (current: {student_username}): ")
        new_password = input("Enter new password: ")
        new_level = input(f"Enter new Form level (current: {students[student_username]['level']}): ")
        new_ic_or_passport = input(f"Enter new IC/Passport number (current: {students[student_username]['ic_or_passport']}): ")
        new_email = input(f"Enter new email (current: {students[student_username]['email']}): ")
        new_contact_number = input(f"Enter new contact number (current: {students[student_username]['contact_number']}): ")
        new_address = input(f"Enter new address (current: {students[student_username]['address']}): ")

        # Update student data
        students[new_username] = {
            "password": new_password,
            "subjects": students[student_username]["subjects"],
            "level": new_level,
            "ic_or_passport": new_ic_or_passport,
            "email": new_email,
            "contact_number": new_contact_number,
            "address": new_address,
            "enrollment_month": students[student_username]["enrollment_month"]
        }

        # Remove the old student entry
        del students[student_username]

        # Write updated data back to file (students.txt)
        with open(STUDENT_FILE, "w") as file:
            for username, details in students.items():
                subjects = ",".join(details["subjects"])
                file.write(f"{username},{details['password']},{subjects},{details['level']},{details['ic_or_passport']},{details['email']},{details['contact_number']},{details['address']},{details['enrollment_month']}\n")

        print("Student profile updated successfully!")
    else:
        print("Student user not found.")

#Define function load students      
def load_students():
    students = {}
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                student_info = line.split(",")
                if len(student_info) == 11:
                    username, password, subject1, subject2, subject3, level, ic_or_passport, email, contact_number, address, enrollment_month = student_info
                    students[username] = {
                        "password": password,
                        "subjects": [subject1, subject2, subject3],
                        "level": level,
                        "ic_or_passport": ic_or_passport,
                        "email": email,
                        "contact_number": contact_number,
                        "address": address,
                        "enrollment_month": enrollment_month
                    }
    return students

#Define main function
def main():
    while True:
        print("Welcome to Brilliant Tuition Centre (BTC)")
        choice = input("1. Login\n2. Exit\nEnter your choice: ").strip()
        
        if choice == "1":
            initialize_files()
            role = None
            student_name = None  
            while role is None:
                role, student_name = login()  
                
                if role is None:
                    print("Returning to the Welcome page...")
                    break  
                    
            if role == "admin":
                admin_menu()
            elif role == "receptionist":
                receptionist_menu()
            elif role == "tutor":
                tutor_menu(student_name)  
            elif role == "student":
                student_menu(student_name) 
            else:
                print("Access Denied.\n")
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break 
        else:
            print("Invalid choice. Please enter 1 to login or 2 to exit.\n")

if __name__ == "__main__":
    main()
