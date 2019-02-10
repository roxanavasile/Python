midterm=float(input("Enter your midterm score: "))
final=float(input("Enter final score: "))
if final-midterm > 20:
    total=midterm+final
    total_2= midterm+final+5
    print("Your score before the 5 bonus points is: " , total)
    print("Your new score including 5 bonus points is: " , total_2)
else:
    total=midterm+final
    print("Your total score is: ", total)

