annual_salary = float(input("What is your annual income? "))
portion_saved = float(input("What percentage of your income will you save each month? "))
total_cost = float(input("What is the total cost of your dream home? "))

monthly_salary = annual_salary / 12
portion_down_payment = .25 * total_cost
current_savings = 0
months = 0
r = .04
while current_savings <= portion_down_payment: 
    total_monthly_savings = (current_savings + ((current_savings * r) / 12) + (portion_saved * monthly_salary))
    current_savings += portion_down_payment
    months = months + 1
    
print("Enter your annual salary: " + str(annual_salary))
print("Enter the percent of your salary to save, as a decimal: " + str(portion_saved))
print("Enter the cost of your dream home: " + str(total_cost))
print("Number of months: " + str(months))


