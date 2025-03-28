# Get user input for the five subjects
maths = int(input("Enter your score in Maths: ")) 
english = int(input("Enter your score in English: "))
kiswahili = int(input("Enter your score in Kiswahili: "))
science = int(input("Enter your score in Science: "))
social = int(input("Enter your score in Social Studies: "))

# Calculate total and average score
result = maths + english + kiswahili + science + social
average = result / 5  # Compute the average

# Print total and average
print(f"Total Marks: {result}")
print(f"Average Score: {average:.2f}")

# Determine the grade based on the average score
if average >= 80:
    print("You got an A")
elif average >= 75:
    print("You got an A-")
elif average >= 70:
    print("You got a B+")
elif average >= 65:
    print("You got a B")
elif average >= 60:
    print("You got a B-")
elif average >= 55:
    print("You got a C+")
elif average >= 50:
    print("You got a C")
elif average >= 45:
    print("You got a C-")
elif average >= 40:
    print("You got a D+")
elif average >= 35:
    print("You got a D")
elif average >= 30:
    print("You got a D-")
else:
    print("You got an E")
