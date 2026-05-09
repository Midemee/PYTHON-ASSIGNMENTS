'''FATHER'S AGE 
PSEUDOCODE

Ask the user to enter the father's current age
Ask the user to enter the son's current age
Calculate difference in years = (2 * son's 'age) - father's age
If difference is negative, make it positive
If  equals 0, father is currently twice the son's age'''

father_age = int(input("Enter father's current age (1-80): "))
son_age = int(input("Enter son's current age (1-80): "))


years_difference = (2 * son_age) - father_age

if years_difference < 0:
    years = years_difference * -1   
    time = "past"
elif x > 0:
    years = years_difference
    time = "future"
else:
    years = 0
    time = "now"

if time == "now":
    print("The father is CURRENTLY twice as old as his son.")
elif time == "past":
    print(years, " years ago, the father was twice as old as his son.")
else:
    print("In ", years, " years, the father will be twice as old as his son.")
