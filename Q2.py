#Q2
n1=int(input("Enter the gross income:"))
n2=int(input("Enter the number of dependents:"))
tax_rate=0.20
standard_deduction=10000
dependent_deduction=3000
taxable_income=n1-standard_deduction-dependent_deduction*n2
tax=taxable_income*tax_rate
print("The tax is:", tax)
