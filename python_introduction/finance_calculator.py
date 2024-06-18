# promt the user for their monthly income
monthly_income = float(input("enter your monthly income:"))
 
 # Ask for their total monthly expenses
monthly_epenses = float(input("enter your total monthly expenses:"))

# Calculate the monthly savings 
monthly_savings = monthly_income - monthly_epenses

# calculate the projected savings after one year, inclusing interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05) # 5% annual interest rate

# Display the user’s monthly savings
print(f"Your monthly savings are: {monthly_savings}")

# Display the projected annual savings after including interest
print(f"Your projected annual savings after one year, including interest, are: {projected_savings}")
