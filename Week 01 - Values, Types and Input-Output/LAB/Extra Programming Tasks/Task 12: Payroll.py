"""## Task 12: Payroll Statement
Ask for: employee name, hours worked, hourly rate, federal tax rate, state tax rate.
Print a formatted payroll slip with gross pay, each deduction, and net pay (2 d.p.).

**Example Output:**
```
Employee: Smith
Gross pay: £97.50
Federal withholding: £19.50
State withholding: £8.78
Net pay: £69.22
```"""

name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
federal_tax_rate = float(input("Enter federal tax rate: "))
state_tax_rate = float(input("Enter state tax rate: "))

gross_pay = hours_worked * hourly_rate
federal_withholding = gross_pay * federal_tax_rate
state_withholding = gross_pay * state_tax_rate
net_pay = gross_pay - federal_withholding - state_withholding

print(f"Employee: {name} \nGross pay: £{gross_pay:.2f} \nFederal withholding: £{federal_withholding:.2f} \nState witholding: £{state_withholding:.2f} \nNet pay: £{net_pay:.2f}")