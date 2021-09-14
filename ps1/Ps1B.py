total_cost = float(input("Enter the cost of your dream house "))
annual_salary = float(input("enter your annual salary "))
portion_saved= float(input("enter the percentage to be saved "))
semi_annual_raise = float(input("Enter the percentage of your raise"))
current_savings = 0
annual_return = 0.04
total_months = 0
portion_down_payment = 0.25
months_to_get_raise = 0
while total_cost * portion_down_payment > current_savings :
    months_to_get_raise += 1
    current_savings += current_savings*annual_return /12
    current_savings += (annual_salary / 12 ) * portion_saved 
    
    if (months_to_get_raise == 6 ):
        annual_salary = annual_salary + annual_salary*semi_annual_raise
        months_to_get_raise = 0
    total_months += 1       
        
print("you need to save for " , total_months , " months to be able to make a payment" )
