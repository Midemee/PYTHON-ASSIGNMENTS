'''SCORE GRADE
PSEUDOCODE

Ask the user to enter three scores
Add the three scores together and divide the total by 3 to get the average
Check which grade range the average falls into
Use conditions to determine the output'''


first_score = int(input("Enter first score: "))
second_score = int(input("Enter second score: "))
third_score = int(input("Enter third score: "))

total_score = first_score + second_score + third_score
average_score = total_score / 3

if average_score >= 90 and average_score <= 100:
    print("Letter Grade: A")
elif average_score >= 80 and average_score < 90:
    print("Letter Grade: B")
elif average_score >= 70 and average_score < 80:
    print("Letter Grade: C")
elif average_score >= 60 and average_score < 70:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")
