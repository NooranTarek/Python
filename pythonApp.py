import json
import re
from datetime import datetime

#===============================================================================================
class User:
    def __init__(self, firstName, lastName, email, password, confirmPassword, mobilePhone):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.confirmPassword = confirmPassword
        self.mobilePhone = mobilePhone

#===============================================================================================

class Project:
    def __init__(self, title, details, totalTarget, startTime, endTime, createdBy):
        self.title = title
        self.details = details
        self.totalTarget = totalTarget
        self.startTime = startTime
        self.endTime = endTime
        self.createdBy = createdBy
#===============================================================================================
def save_users(user):
    try:
        with open("users.json", "r") as file:
            data = file.read()
            if data:
                existing_users = json.loads(data)
            else:
                existing_users = []
    except FileNotFoundError:
        existing_users = []

    user_dict = {
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "password": user.password,
            "confirmPassword": user.confirmPassword,
            "mobilePhone": user.mobilePhone
        }
    
    existing_users.append(user_dict)

    with open("users.json", "w") as file:
        json.dump(existing_users, file)


#===============================================================================================
def save_projects(project):
    try:
        with open("projects.json", "r") as file:
            data = file.read()
            if data:
                existing_projects = json.loads(data)
            else:
                existing_projects = []
    except FileNotFoundError:
        existing_projects = []

    print(project)
    project_dict = {
            "title": project.title,
            "details": project.details,
            "totalTarget": project.totalTarget,
            "startTime": project.startTime,
            "endTime": project.endTime,
            "createdBy": project.createdBy
        }
    
    existing_projects.append(project_dict)

    with open("projects.json", "w") as file:
        json.dump(existing_projects, file)

#===============================================================================================
def registeration():
    users = []
    try:
        with open("users.json", "r") as file:
            data = file.read()
            if data:
                users = json.loads(data)
    except FileNotFoundError:
        pass  

    print("______________________________________________________")
    first_name = input("first name: ")
    while not first_name.strip(): 
        print("first name must not be empty")
        first_name = input("first name: ")
    print("______________________________________________________")
    last_name = input("last name: ")
    while not last_name.strip(): 
        print("last name must not be empty")
        last_name = input("last name: ")
    print("______________________________________________________")
    email = input("email: ")
    existing_emails = [user['email'] for user in users]
    while not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) or email in existing_emails:
        email = input("sorry... try to enter valid email that is not exist or match email pattern: ")   
    print("______________________________________________________")
    password = input("password: ")
    while not password.strip(): 
        print("password must not be empty")
        password = input("password: ")
    print("______________________________________________________")
    confirm_password = input("confirm password: ")
    while password != confirm_password :
        confirm_password = input("sorry ... passwords do not match.try to fill them again: ")
    print("______________________________________________________")
    mobile_phone = input("mobile phone")
    while not re.match(r'^0\d{2}\d{8}$', mobile_phone):
        mobile_phone = input("try to enter Egyptian phone number please ...: ")
    user = User(first_name, last_name, email, password, confirm_password, mobile_phone)
    users.append(user) 
    save_users(user)
    print("now you are one of CROWDFUNCTION world members :) ")



#===============================================================================================
def login():
    try:
        with open("users.json", "r") as file:
            data = file.read()
            if data:
                users = json.loads(data)
    except FileNotFoundError:
        pass 
    print("______________________________________________________")
    email = input("email: ")
    print("______________________________________________________")
    password = input("password:")
    for registeredUser in users:
        if registeredUser['email'] == email and registeredUser['password'] == password :
            print("logged in successfully!")
            return registeredUser
    print("sorry ...invalid email or password")
    return None 

#===============================================================================================
def create_project(user):
    projects = []
    try:
        with open("projects.json", "r") as file:
            data = file.read()
            if data:
                projects = json.loads(data)
    except FileNotFoundError:
        pass  
    print("______________________________________________________")
    title = input("title: ")
    print("______________________________________________________")
    details = input("details: ")
    print("______________________________________________________")
    total_target = float(input("total target: "))
    if not isinstance(total_target,float):
            total_target = float(input("please provide total target as float number: "))
    print("______________________________________________________")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    start_time = input("start Time : ")
    while not re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", start_time) or (start_time < current_time):
        start_time = input("this date not match date format YYYY-MM-DD HH:MM . or this date passed: ")
    end_time = input("end Time : ")
    while not re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", end_time):
        end_time = input("incorrect date format. Please enter in YYYY-MM-DD HH:MM format: ")
    createdBy = user['email']
    #print(users)
    if user:
        project = Project(title, details, total_target, start_time, end_time, createdBy)
        projects.append(project)
        save_projects(project)
        print("project created successfully")
    else:
        print("user not found. try to login with valid email")

#==================================================================================
def view_all_projects():
    with open("projects.json", "r") as file:
            data = file.read()
            if data:
                projects = json.loads(data)
    print("crowd funding projects:")
    for index, project in enumerate(projects, start=1):
        print(f"{index}. title: {project['title']}, createdBy: {project['createdBy']}")
    print("________________________________________________________")
#==================================================================================
def edit_project(user):
    with open("projects.json", "r") as file:
            data = file.read()
            if data:
                projects = json.loads(data)
    print("______________________________________________________")
    print("Your Projects:")
    user_projects = [project for project in projects if project['createdBy'] == user['email']]
    for i, project in enumerate(user_projects, start=1):
        print(f"{i}. Title: {project['title']}, Created By: {project['createdBy']}")

    if not user_projects:
        print("You have no projects to edit.")
        return

    choice = input("Enter the number of the project you want to edit: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(user_projects):
        print("Invalid choice.")
        return

    project_to_edit = user_projects[int(choice) - 1]
    print("Enter new details for the project:")
    project_to_edit['title'] = input(f"New title [{project_to_edit['title']}]: ") or project_to_edit['title']
    project_to_edit['details'] = input(f"New details [{project_to_edit['details']}]: ") or project_to_edit['details']
    project_to_edit['totalTarget'] = float(input(f"New total target [{project_to_edit['totalTarget']}]: ") or project_to_edit['totalTarget'])
    project_to_edit['startTime'] = input(f"New start time [{project_to_edit['startTime']}]: ") or project_to_edit['startTime']
    project_to_edit['endTime'] = input(f"New end time [{project_to_edit['endTime']}]: ") or project_to_edit['endTime']
    print("Project updated successfully!")
    def save_edited_projects(projects):
        with open("projects.json", "w") as file:
          json.dump(projects, file)
    save_edited_projects(projects)
#==================================================================================
def delete_project(user):
    with open("projects.json", "r") as file:
            data = file.read()
            if data:
                projects = json.loads(data)
    print("______________________________________________________")
    print("Your Projects:")
    user_projects = [project for project in projects if project['createdBy'] == user['email']]
    for i, project in enumerate(user_projects, start=1):
        print(f"{i}. Title: {project['title']}, Created By: {project['createdBy']}")

    if not user_projects:
        print("You have no projects to delete.")
        return

    choice = input("Enter the number of the project you want to delete: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(user_projects):
        print("Invalid choice.")
        return

    project_to_delete = user_projects[int(choice) - 1]
    projects.remove(project_to_delete)
    print("Project deleted successfully!")
    def projects_after_delete(projects):
        with open("projects.json", "w") as file:
          json.dump(projects, file)
    projects_after_delete(projects)
#==================================================================================
def runApp():
    while True:
        print("1. register")
        print("2. login")
        print("3. exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            registeration()
        elif choice == "2":
         logged_user = login()
         if logged_user:
             while True:
                print("1. Create Project")
                print("2. View All Projects")
                print("3. Edit Project")
                print("4. Delete Project")
                print("5. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    create_project(logged_user) 
                elif choice == "2":
                    view_all_projects()
                elif choice == "3":
                    edit_project(logged_user) 
                elif choice == "4":
                    delete_project(logged_user) 
                elif choice == "5":
                    break
                else:
                    print("Invalid choice")
        elif choice == "3":
            break
        else:
            print("invalid choice")



runApp() 