weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))
BMI = weight/(height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
  print("You are underweight")
elif BMI <= 24.9:
  print("You are healthy")
elif BMI <= 29.9:
  print("You are slightly obese")
elif BMI <= 34.9:
  print("You are obese")
elif BMI <= 39.9:
  print("You are very obese")
else:
  print("You are extremely obese")