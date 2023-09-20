#assignment 1 comp think 

income = float(input("What is your annual income?"))

mfj = bool(input("Are you married jointly, type 'true', otherwise press enter."))
if mfj== True:
    spouse_income = float(input("What is your partners income?"))
    income = income + spouse_income
    
else:
    spouse_income = 0 
    income= income + spouse_income

#min * tax rate
max_tax_1_mfj= 528.00
max_tax_2_mfj= 2841.60
max_tax_3_mfj= 7971.60

max_tax_1_single = 264.00
max_tax_2_single = 1420.80
max_tax_3_single = 3985.80

if mfj == True:
    
    if income <= 12000:
        state_tax = (income * 0.0440)
    elif(income > 12000) and (income <= 60000):
        state_tax = max_tax_1_mfj + (income - 120000)* 0.0482
    elif(income > 60000) and (income <= 150000):
            state_tax = max_tax_2_mfj + (income - 60000)* 0.0570
    else:
        state_tax = max_tax_3_mfj + (income - 150000)* 0.0600
else:
    if income <= 6000:
        state_tax = (income * 0.0400)
    elif (income > 6000) and (income<= 30000):
        state_tax = max_tax_1_single + (income - 60000) *0.0482
    elif(income > 30000) and (income <= 75000):
        state_tax = max_tax_2_single + (income - 30000) * 0.0570
    else:
        state_tax = max_tax_3_single + (income - 75000)* 0.6000
    

print("Your state tax owed for Iowa in 2023 was $",round(state_tax))







#federal married jointly
if mfj == True:
    income = income - 27700
   
    if income <= 22000:
        federal_tax = income * 0.100
    elif(income > 22000) and (income <= 89450):
        federal_tax = 2200 + ((income - 22000) *0.1200)
    elif(income > 89450) and (income <= 190750):
        federal_tax = 10294 + ((income - 89450) * 0.2200)
    elif(income > 190750) and (income <= 364200):
        federal_tax = 32580 + ((income-190750) * 0.2400)
    elif(income > 364200) and (income <= 462500):
        federal_tax = 74208 +((income-364200) * 0.3200)  
    elif(income > 462500) and (income <= 693750):
        federal_tax = 105664 + ((income-462500) * 0.3500)
    else:
        federal_tax = 186601.50 +((income-693750) *0.3700)
#single federal 

else:
    income = income - 13850
    if income <= 11000:
        federal_tax = (income * 0.1000)
    elif (income > 11000) and (income <= 44725):
        federal_tax = 1100 + ((income-11000) * 0.1200)
    elif(income > 44725) and (income <= 95375):
        federal_tax = 5147 + ((income-44725) * 0.2200)
    elif (income > 95375) and (income <= 182100):
        federal_tax = 16290 + ((income-95375) * 0.2400)
    elif (income > 182100) and (income <= 231250):
        federal_tax = 37104 + ((income- 182100) * 0.3200)
    elif (income > 231250) and (income <= 578125):
        federal_tax = 52832 + ((income-231250) *0.3500)
    else:
        federal_tax = 174238.25 + ((income- 578125) * 0.3700)



print("Your federal tax owed for 2023 was $",round(federal_tax))



total_tax = state_tax + federal_tax
 

print("Your total tax owed for 2023 was $", round(total_tax)) 
   



