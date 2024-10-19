def calculate_grade(score):
    grade = None
    if score >= 70:
        grade = 4
    elif score >=60 and score < 70:
        grade = 3
    elif score >=50 and score < 60:
        grade = 2
    elif score >=45 and score < 50:
        grade = 1
    else:
        grade = 0
    return grade

    def cgpacalculator():
        grade = 0
        TotalUnit = 0
        TotalPoint = 0
    
    numberofcourses = int(input("Please enter the number of courses you offered: "))
    print(numberofcourses)
    
    for x in range(numberofcourses):
        score =  int(input("Enter Score: "))
        grade = calculate_grade(score)
        
        unit = int(input("Enter Course Unit: "))
        TotalUnit += unit
        
        point = grade * unit
        TotalPoint += point
        
        
    print(f"Total points accumulated: {TotalPoint}")
    print(f"Total units: {TotalUnit}")
    
    cgpa = TotalPoint / TotalUnit
    
    return f"CGPA = {cgpa}"   