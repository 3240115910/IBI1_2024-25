# Initialize two variables named weight and height.
# Let the people input the numbers of weight and height.
weight=float(input("Please enter your weigth(unit:kg):"))
height=float(input("Please enter your height(unit:m)"))
# Calculate the BMI.
BMI=weight//height**2
# Definite the categories of different BMI.
if BMI<18.5:
    categories="underweight"
elif 18.5<=BMI<=30:
    categories="normal"
else:
    categories="obese"
# Print the results.
print (f"Your BMI is {BMI:.2f} and you belong to {categories}.")
