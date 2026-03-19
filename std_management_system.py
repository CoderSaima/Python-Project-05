import os
import json

# Load Data
File_Name = "std.json"
if os.path.exists(File_Name):
    with open(File_Name, "r") as f:
        try:
            std_list = json.load(f)
        except json.JSONDecodeError:
            std_list = []
else:
    std_list = []

while True:
# Input Choice
    print(
    "1. Add New Student Data\n",
    "2. View specific Student Data\n",
    "3. View all Student Data\n",
    "4. Edit student data\n",
    "5. Delete student data\n", 
    "6. Exist")
    choice = input("Enter your choice...")

    #.......Add New Student.....
    if choice == "1":
        print("--- Add New Student ---")
        std_id = input("Enter student ID: ")
        
        exists = False
        for s in std_list:
            if s['std_ID']  == std_id:
               exists = True
               break
            
        if exists:
            print("Student with this ID already exist..!")
        else:
            std_entry = {     
            "std_name" : input("Enter student name\n"),
            "std_fname" : input("Enter student Father name\n"),
            "std_age" : input("Enter student age\n"),
            "std_ID" : std_id,
            "std_Email" : input("Enter student Email\n"),
            "std_phone" : input("Enter student phone\n"),
            "std_section" : input("Enter student section\n")
        }
        std_list.append(std_entry)
        print("Student added successfully..!")

#............View Specific Student Data ........
    elif choice == "2":
        search_id = input("Enter Student ID to search: ")
        found = False
        for s in std_list:
            if s['std_ID'] == search_id:
                print("\n--- Student Details ---")
                for key, value in s.items():
                    print(f"{key}: {value}")
                found = True
                break
        if not found:
            print("Student not found.")

# .......View All Student Data...........
    elif choice == "3":
        if not std_list:
            print("Data not found.")
        else:
            print("---- All Registered Student Detail ----")
            for s in std_list:
                print(f"ID: {s['std_ID']}\n Name: {s['std_name']}\n Father Name: {s['std_fname']}\n Email: {s['std_Email']}\n Phone: {s['std_phone']}\n Section: {s['std_section']}")     
#........... Edit student data.......
    elif choice == "4":
        edit_id = input("Enter student ID..")
        for s in std_list:
            if s['std_ID'] == edit_id:
                print(f"Editing detail for {s['std_name']}.")
                new_Name = input(f"New Name of [{s['std_name']}] will be : ")
                new_email = input(f"New Email of [{s['std_Email']}] will be : ")
                # new_ID = input(f"New Email of [{s['std_ID']}] will be : ")

                if new_Name:
                    s['std_name'] = new_Name
                if new_email:
                    s['std_Email'] = new_email
                # if new_ID:
                #     s['std_ID'] = new_ID
                print("Update successfully..")
                break 
        else:
            print("Student ID not found")       
# ............ Delete Student data ............
    elif choice == "5":
        del_Id = input("Enter student ID.")
        for i, s in enumerate(std_list):
            if s['std_ID'] == del_Id:
                confirm = input(f"Are you sure you want to delete the data {s['std_name']} ? yes/No")
                if confirm.lower() == "yes":
                    std_list.pop(i)
                    print("Student removed..")
                    break
                else:
                    print("Student ID not found")

#............ Exit ..........
    elif choice == "6":
        print("Saving Data and exists ...")
        break
    else:
        print("Invalid choice, Try Again...")

    with open(File_Name, "w") as f:
        json.dump(std_list, f, indent=3)