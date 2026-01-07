#Start with a greeting  message
print("Hello Scholar welcome to MyCGPA Calculator\nI would love to know your Course and the respective grades you got")
#Takes In the grade for each course and the credit score
course_code = input("your course code").upper()
grade = input(f"{course_code} the course grade?").strip().upper()
# I am looping through so i am adding course credit as a list
course_credit = []  # Start with empty list
course_credit.append(int(input(f"{course_code} the course credit?")))
total_course_credit= sum(course_credit) 
the_course_credit_quality = course_credit
#list concatination adding to the empty list of course credit also list multiplication using list comprehension

#coursequality list creation

#coursequality calculation for each inputed grade using list comprehension
course_quality_result = [x * 5 for x in the_course_credit_quality]
the_course_credit_quality = the_course_credit_quality + course_quality_result
total_course_credit_quality = sum(the_course_credit_quality)
#course credit addition
total_course_credit = sum(course_credit)
#Assign a value for their grade: Each letter grade gets a specific point value (e.g., A=5, B=4, C=3, D=2,E=1, F=0 ) using if else statement
if grade == "A":
    gradepoint = 5
elif grade == "B":
    gradepoint = 4
elif grade == "C":
    gradepoint = 3
elif grade == "D":
    gradepoint = 2
elif grade == "E":
    gradepoint = 1
elif grade == "F":
    gradepoint = 0
else:
    gradepoint = 0
    print("you have inserted a wrong grade")
#The cgpa calculations
#total_course_credit calcultions summation of the course credit * 5 which is the highest grade point
CGPA = (gradepoint * total_course_credit)/total_course_credit
print(total_course_credit)
print(the_course_credit_quality)
#The CGPA calculations
print(f"your current CGPA is {CGPA}")