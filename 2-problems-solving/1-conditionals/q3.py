score=int(input("enter your score"))
if score<0 or score>100:
    print("enter valid score (0-100)")
elif score >= 90 :
    print("your grade is A")
elif score >= 80 :
    print("your grade is B")
elif score >= 70  :
    print("your grade is C")
elif score > 60:
    print("your score is D")
else:
    print("your grade is F")