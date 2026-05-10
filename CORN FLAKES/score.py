passes = 0
failures = 0
for count in range (15):
    score = int(input("Enter the score: "))
    
    if score >= 45:
        passes += 1
    else:
        failures += 1
     
print(passes, "Students passed")
       

