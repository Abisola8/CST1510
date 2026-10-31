"""## Task 4: Body Mass Index (BMI)
BMI is a measure of health and weight. It can be calculated by taking your weight in kilograms and dividing it by the square of your height in meters. The interpretation of BMI for people 20 years or older is as follows:

| BMI | Interpretation |
|-----|----------------|
| BMI < 18.5 | Underweight |
| 18.5 ≤ BMI < 25.0 | Normal |
| 25.0 ≤ BMI < 30.0 | Overweight |
| 30.0 ≤ BMI | Obese |

Write a program that prompts the user to enter weight in pounds and height in inches and display the BMI. Note that one pound is 0.45359237 kilograms, and one inch is 0.0254 meters."""

weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

weight_kg = weight_pounds * 0.45359237
height_m = height_inches * 0.0254

bmi = weight_kg / (height_m ** 2)

print(f"Your BMI is: {bmi:.2f}")