''' 
    write a program to calculate & display gross annual income, tax and net income from  given monthly income as per below income tax rule 
    ---------------------------------------------------------------------------------
    annual income                           Tax Rate
    Above Rs. 24,00,000                     30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,000 to Rs. 16,00,000	    15%
    below 12,00,000                          0%

    steps 
    1) accept monthly income 
    2) calculate annual income 
    3) calculate tax as per rule
    4) calculate net income using gross annual income and tax 
    5) display gross income, tax, net income
'''   

income =int(input("Enter monthly income : "))
gross = income * 12

if gross >2400000 :
    tax = gross* 0.30
elif gross >2000001:
    tax = gross * 0.25
elif gross >1600001:
    tax = gross * 0.20
elif gross >1200000:
    tax = gross * 0.15
else:
    tax=0
print(f"Gross income is {gross} tax applicable is {tax} income after tax is {gross-tax}")