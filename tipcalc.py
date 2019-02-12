meal_cost = input("How much was this meal? > ")
tip_per = input("What percentage do you want to give for tip? > ")
tip_per = float(tip_per) * .01

tip_val = tip_per * float(meal_cost)
total_cost = tip_val + float(meal_cost)
print(f"The total with tip is {total_cost}")
