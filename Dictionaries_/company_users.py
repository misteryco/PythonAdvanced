command = input()
company_and_employees_data = {}
while command != "End":
    command = command.split(" -> ")
    company, emp_id = command[0], command[1]
    if company not in company_and_employees_data:
        company_and_employees_data[company] = []
    if emp_id in company_and_employees_data[company]:
        command = input()
        continue
    company_and_employees_data[company].append(emp_id)
    command = input()

for company, emp_list in company_and_employees_data.items():
    print(company)
    for employee in emp_list:
        print(f"-- {employee}")
