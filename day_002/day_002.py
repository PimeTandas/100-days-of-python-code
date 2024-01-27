# Tip Cost Calculator

# Title
print("Tip Cost Calculator")

# Get inputs
raw_cost = float(input("Please Enter the Cost of the bill: "))
tip_pct = int(input("Please Enter percentage tip, (10, 12, 15): "))
people = int(input("How ways is the bill being split: "))

# Perform Calculation
tip_cost_pct = (tip_pct / 100) + 1
cost = raw_cost * tip_cost_pct
per_person_cost = round(cost / people, 2)

# Output the result
print(f"The final amount per person to pay is: {per_person_cost:.2f}")