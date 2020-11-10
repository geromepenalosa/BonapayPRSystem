import os
import shutil
import sys
from os import mkdir
from os.path import exists as fileExists

#   FUNCTIONS
def salary_read(user):
    username = user
    filename = "./employees_data/{}.txt".format(username.lower().replace(" ", "_").replace(".", "_"))
    file = open(filename, "r")
    contents = file.readlines()
    fields = {}

    for line in contents:
        values = line.split(": ")
        fields[values[0]] = values[1]

        est_salary = fields["EST. SALARY"]
        salary_bracketing(est_salary)

        if len(contents) > 0:
            print("".join(contents))
            print("Estimated Salary: {}".format(fields["EST. SALARY"]))

        salary_bracketing(est_salary)



    file.close()

def info_update(user):
    username = user
    filename = "./employees_data/{}.txt".format(username.lower().replace(" ", "_").replace(".", "_"))
    file = open(filename, "r")
    contents = file.readlines()
    fields = {}

    for line in contents:
        values = line.split(": ")
        fields[values[0]] = values[1]

    if len(contents) > 0:
        print("".join(contents))
        print("Monthly Salary: {}".format(fields["MONTHLY SALARY"]))
    file.close()

def salary_bracketing(emp_salary):
    global employee_position
    est_salary = emp_salary

    fields = {}
    for line in contents:
        values = line.split(": ")
        fields[values[0]] = values[1]

        employee_position = fields["Company Position"]

    if est_salary <=20000:
        filename = "./company_data/{}.txt".format(str(employee_position).replace(" ", "_").replace(".", "_"))
        for line in contents:
            values = line.split(": ")
            fields[values[0]] = values[1]
            employee_position = fields["Deductions"]

running = True
while running:

    #   PROGRAM EXISTENCE CHECK:
    filename = "./company_data/.txt"
    if fileExists(filename):
        continue
    if not fileExists("company_data/"):
        prompt_1 = input("Company data not found! Enroll your company? (Y/N): ").upper()
        if prompt_1 == "Y":
            mkdir("company_data/")
            company_name = input("Enter Company Name: ")
            prompt_2 = int(input("Enter number of available positions: "))
            positionNum = prompt_2
            for i in range(positionNum):
                company_positions = input("Enter position: ")
                est_salary = int(input("Monthly salary: "))
                filename = "./company_data/{}.txt".format(company_positions.replace(" ", "_").replace(".", "_"))
                file = open(filename, "w")
                file.write("Company Position: {}\n".format(company_positions))
                file.write("Salary: {}\n".format(est_salary))

                if est_salary <= 20000:
                    salary_deductions = {"SSS": 300, "PhilHealth": 500, "PAG-IBIG": 100}
                    file.write("Deductions {}\n".format(salary_deductions))

            continue
        elif prompt_1 == "N":
            sys.exit()

    #   MAIN MENU
    print("Welcome to Bonapay Payroll Management System")
    print("-"*50)
    print("Select an action: \n"+"(1) Review company data \n"+"(2) Enroll employee \n"+
          "(3) Read employee data \n"+"(4) Delete employee data\n"+"(5) Reset program\n"+
          "(6) Exit")
    cmd = int(input(">> "))
    print("")

    if cmd == 1:
        print("-" * 50)
        print("Available Company data: ")
        dir_list = os.listdir(path='company_data/')
        print(dir_list)
        print("-" * 50)

        post_input = input("To read data, enter position name: ")
        filename = "./company_data/{}.txt".format(post_input.lower().replace(" ", "_").replace(".", "_"))
        if not fileExists(filename):
            print("Data not found!")
            print("-" * 50)
            continue

        file = open(filename, "r")
        contents = file.readlines()
        if len(contents) > 0:
            print("".join(contents))
        file.close()

    #   OPT #2 : WRITING DATA
    elif cmd == 2:
        if not fileExists("employees_data/"):
            mkdir("employees_data/")
        employee_fName = input("First Name: ")
        employee_lName = input("Last Name: ")
        employee_idNum = input("Employee I.D.: ")
        filename = "./employees_data/{}.txt".format(employee_idNum.replace(" ", "_").replace(".", "_"))

        #   FILE EXISTENCE CHECK:
        if fileExists(filename):
            print("Employee already exists!")
            print("-"*50)
            continue

        dir_list = os.listdir(path='company_data/')
        print(dir_list)
        print("-" * 50)
        employee_position = (input("Enter Position: "))

        employee_absences = int(input("Number of Absences: "))
        employee_overtimeHrs = int(input("Number of Overtime Hours: "))
        employee_late = int(input("Number of Times Late (in mins.): "))

        #   DATA WRITING:
        file = open(filename, "w+")
        file.write("Employee Name: {}\n".format(employee_fName+" "+employee_lName))
        file.write("Employee I.D.: {}\n".format(employee_idNum))
        file.write("Employee's Position: {}\n".format(employee_position))
        file.write("Num. of Absences: {}\n".format(employee_absences))
        file.write("Num. of Overtime Hours: {}\n".format(employee_overtimeHrs))
        file.write("Num. of Times Late (in mins.): {}\n".format(employee_late))

        filename = "./company_data/{}.txt".format(employee_position.lower().replace(" ", "_").replace(".", "_"))

        contents = file.readlines()
        fields = {}
        for line in contents:
            values = line.split(": ")
            fields[values[0]] = values[1]

        employee_salary = fields["Salary: "]

        file.write("EST. SALARY: {}\n".format(employee_salary))
        file.close()

        print("-"*50)
        print("Employee data saved successfully!")
        print("-"*50)

    #   READ DATA:
    elif cmd == 3:
        print("-"*50)
        print("Available employee data: ")
        print(os.listdir(path='employees_data/'))
        print("-"*50)

        id_input = input("To read data, enter employee's I.D. Number: ")
        filename = "./employees_data/{}.txt".format(id_input.lower().replace(" ", "_").replace(".", "_"))
        if not fileExists(filename):
            print("Employee data not found!")
            print("-"*50)
            continue

        # Calls function 'salary_read' and uses I.D. as parameter
        salary_read(id_input)

    #   DELETE EMPLOYEE DATA
    elif cmd == 4:
        print("-" * 50)
        print("Available Company data: ")
        dir_list = os.listdir(path='company_data/')
        print(dir_list)
        print("-" * 50)

        post_input = input("To read data, enter position name: ")
        filename = "./company_data/{}.txt".format(post_input.lower().replace(" ", "_").replace(".", "_"))
        if not fileExists(filename):
            print("Data not found!")
            print("-" * 50)
            continue

        file = open(filename, "r")
        contents = file.readlines()
        if len(contents) > 0:
            print("\n".join(contents))
        file.close()

    #   PROGRAM RESET:
    elif cmd == 5:
        print("This will delete all of the enrolled data. Proceed? (Y/N)")
        cmd_1 = input(">> ").upper()
        if cmd_1 == "Y":
            if fileExists("employees_data"):
                shutil.rmtree("employees_data")
            print("Employee data deleted succesfully!")
            print("-" * 50)
            shutil.rmtree("company_data")
            print("Company data deleted succesfully!")
            print("-" * 50)

    #   EXIT
    elif cmd == 6:
        running = False

    else:
        print("Invalid input! Try again.")
        continue