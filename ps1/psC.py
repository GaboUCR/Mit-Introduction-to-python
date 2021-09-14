total_cost = 1000000.0
annual_salary = float(input("enter your annual salary "))
max_portion = 10000
min_portion = 0
portion_saved= (max_portion + min_portion)/2
semi_annual_raise = 0.07
current_savings = 0.0
annual_return = 0.04
total_months = 0
portion_down_payment = 0.25
months_to_get_raise = 0
initial_annual_salary = annual_salary
n_iterations = 0
bol = 0
  if (total_cost*portion_down_payment /3 >= annual_salary ):
        print ("it is not possible to save for a down payment in three years")
        
  else  :
          while bol == 0:
          
            for total_months in range (36):
                current_savings += current_savings*annual_return /12
                current_savings += (annual_salary / 12 ) * (float(portion_saved/10000))
                
                if (int(total_cost * portion_down_payment) == int(current_savings) and total_months == 35 ):
                    print (portion_saved/10000 , n_iterations, current_savings , total_months)
                    bol = 10
                    break
              
               
                if (months_to_get_raise == 6 ):
                    annual_salary = annual_salary + annual_salary*semi_annual_raise
                    months_to_get_raise = 0
                       
                months_to_get_raise += 1 
                if (int(total_cost * portion_down_payment <= current_savings)):
                     max_portion = portion_saved 
                     portion_saved = int((max_portion + min_portion)/2)
                     print (max_portion,portion_saved, min_portion)
                     total_months = 0
                     months_to_get_raise = 0
                     current_savings = 0
                     annual_salary = initial_annual_salary
                     n_iterations += 1
                     break
                if (total_months == 35):
                     min_portion = portion_saved 
                     portion_saved = (max_portion + min_portion)/2
                     total_months = 0
                     months_to_get_raise = 0
                     current_savings = 0
                     annual_salary = initial_annual_salary
                     n_iterations += 1       
                     break
               
           #     print( portion_saved/10000 , total_months, current_savings)
                
                
                
        
        
        
