import random


def grade(score):
    if score >=60 and score < 70:
        grade = "D"
    if score >=70 and score < 80:
        grade = "C"
    if score >=80 and score < 90:
        grade = "B"
    if score >=90 and score <= 100:
        grade = "A"
    ret = "Score: "+ str(score) + "; Your grade is " + grade
    return ret





for counter in range(1,10):
    print grade(random.randint(60,100))
