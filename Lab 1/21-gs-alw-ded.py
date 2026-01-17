def gr_salary() :

    salary= float(input("Enter the gross amount of your salary\n"))

    allowance= salary*10/100

    deduction= salary*3/100

    Netsalary= salary+allowance-deduction

    print(f"The Net Salary With Gross Salary {salary} , allowances {allowance} , and deductions {deduction} is {Netsalary}\n")

gr_salary()
