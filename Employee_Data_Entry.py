import string
sum_of_age = 0
emp_number = input("Please enter the number of employees : ")
for index in range(int(emp_number)):

    emp_first_name = input("Please enter your first name : ")
    emp_first_name = emp_first_name.strip()

    while len(emp_first_name) == 0:
        emp_first_name = input("Please enter your first name : ")

    emp_last_name = input("Please enter your last name : ")
    emp_last_name = emp_last_name.strip()

    while len(emp_last_name) == 0:
        emp_last_name = input("Please enter your last name : ")

    emp_age = input("Enter the age : ")

    while not emp_age.isdigit():
        emp_age = input("Enter the age : ")

    age = int(emp_age)

    while (age < 18) or (age > 100):
        age = int(input("Enter a valid age : "))

    print("Employee details - ")
    print(emp_first_name)
    print(emp_last_name)
    print(age)

    sum_of_age = sum_of_age + age

    if sum_of_age > 500:
        print("The sum of ages is above 500 ")

