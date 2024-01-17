def calculate_travel_expense(budget_limit_per_day, number_of_days):
    
    # Get user input for expenses

    accomodation_percentage = float(input("Enter the percentage for accomodation: "))
    transportation_percentage = float(input("Enter the percentage for tranportation: "))
    meals_percentage = float(input("Enter the percentage for meals: "))
    activities_percentage = float(input("Enter the percentage for activities: "))

    # Calculte daily budget
    daily_budget = budget_per_day if budget_limit_per_day else float('inf')
    daily_budget = min(daily_budget, budget_limit_per_day) # Ensure it doesn't exceed the limit

    # Calculate total expenses
    
    accomodation_cost = daily_budget * (accomodation_percentage / 100)
    transportation_cost = daily_budget * (transportation_percentage / 100)
    meals_cost = daily_budget * (meals_percentage / 100)
    activities_cost = daily_budget * (activities_percentage / 100)

    # Calculate total expenses
    total_expense = accomodation_cost + transportation_cost + meals_cost + activities_cost

    # Display individual expenses
    print(f"Accomodation cost: ${accomodation_cost:.2f}")
    print(f"Transportation cost: ${transportation_cost:.2f}")
    print(f"Meals cost: ${meals_cost:.2f}")
    print(f"Activities cost: ${activities_cost:.2f}")


    # Check if total expense exceeds budget 

    if total_expense > daily_budget:
        print("Total expense exceeds daily budget!")
        excess_amount = total_expense - daily_budget
        print(f"To stay within the budget, consider reducing expenses by ${excess_amount:.2f}.")

    # Suggest adjustments based on the percentage contributions
        excess_accomodation = accomodation_cost - (daily_budget * (accomodation_percentage / 100))
        excess_tranportation = transportation_cost - (daily_budget * (transportation_percentage / 100))
        excess_meals = meals_cost - (daily_budget * (meals_percentage / 100))
        excess_activities = activities_cost - (daily_budget * (activities_percentage / 100))
        
        print(f"Suggestions to cut expenses:")
        if excess_accomodation > 0:
            print(f" - Reduce accomodation expenses by ${excess_accomodation:.2f}")
        if excess_tranportation > 0:
            print(f" - Reduce tranportation expenses by ${excess_tranportation:.2f}")
        if excess_meals > 0:
            print(f" - Reduce meals exoenses by ${excess_meals:.2f}")
        if excess_activities > 0:
            print(f" - Reduce activities expenses by ${excess_activities:2f}") 


    else:
        remaining_budget = daily_budget - total_expense
        print(f"Total expense: ${total_expense:.2f}") 
        print(f"Remaining daily budget: ${remaining_budget:.2f}")
        
# Get user input for budget
budget_per_day = float(input("Enter your budget per day (enter 0 for unlimited): "))
number_of_days = int(input("Enter the number of days: "))

# Call the function with the provided budget per day and number of days
calculate_travel_expense(budget_per_day, number_of_days)
