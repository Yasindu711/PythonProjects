import matplotlib.pyplot as plt
import csv
import os

# Function to calculate the budget distribution
def calculate_budget(salary, categories):
    budget_distribution = {}
    for category, percentage in categories.items():
        budget_distribution[category] = salary * (percentage / 100)
    return budget_distribution

# Function to display the budget distribution as a pie chart
def display_chart(salary, budget_distribution):
    labels = list(budget_distribution.keys())
    amounts = list(budget_distribution.values())
    
    # Define a function to format both percentage and amount
    def func(pct, all_vals):
        absolute = pct / 100. * sum(all_vals)
        return f"{pct:.1f}%\n(${absolute:.2f})"
    
    # Display pie chart with percentages and corresponding amounts
    plt.pie(amounts, labels=labels, autopct=lambda pct: func(pct, amounts), startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title(f'Income Distribution of Weekly Salary: ${salary:.2f}')
    plt.show()

# Function to track history in CSV
def save_to_csv(salary, budget_distribution):
    file_exists = os.path.isfile('budget_history.csv')
    
    with open('budget_history.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Salary'] + list(budget_distribution.keys()))
        writer.writerow([salary] + list(budget_distribution.values()))

# Function to display savings projection
def future_savings_projection(current_savings, weeks):
    return current_savings * weeks

# Main function to run the program
def main():
    try:
        # Asking for user input
        salary = float(input("Enter your weekly salary: $"))
        print("\nCreate your budget by entering percentages for each category.")
        categories = {}
        
        while True:
            category_name = input("Enter category name (or type 'done' to finish): ")
            if category_name.lower() == 'done':
                break
            percentage = float(input(f"Enter percentage for {category_name}: "))
            categories[category_name] = percentage
        
        # Calculate the distribution
        budget_distribution = calculate_budget(salary, categories)
        
        # Display the distribution
        print(f"\nBased on your weekly salary of ${salary:.2f}:")
        for category, amount in budget_distribution.items():
            print(f"{category}: ${amount:.2f} ({categories[category]}%)")
        
        # Save to CSV for tracking history
        save_to_csv(salary, budget_distribution)
        
        # Display the chart
        display_chart(salary, budget_distribution)
        
        # Ask for future savings projection
        if 'Savings' in categories:
            weeks = int(input("\nHow many weeks into the future do you want to project your savings? "))
            savings_projection = future_savings_projection(budget_distribution['Savings'], weeks)
            print(f"After {weeks} weeks, you will have saved approximately: ${savings_projection:.2f}")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Running the main function
if __name__ == "__main__":
    main()
