def printinfo():
    for key, item in info.items():
        if key == "Homework" or key == "Homework Average":
            print(key,"\t:",item)
        else:
            print(key,"\t\t:",item)
def calculate():
    quizav = sum(info["Quiz"]) / numq
    info["Quiz Average"] = quizav
    homeworkav = sum(info["Homework"]) / numh
    info["Homework Average"] = homeworkav
    grade =  ( quizav + homeworkav) /2 * 0.6 + (exam/100) * 0.4
    info["Grade"] = grade
    return info
def lettergrade():
    score = info["Grade"]
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
        
info = {"Name":"","Course":"","Quiz":[],"Homework":[],"Exam":0,"Quiz Average":0,"Homework Average":0,"Grade":0}
name = input("Name: ")
info["Name"] = name
course = input("Course: ")
info["Course"] = course
numq = int(input("Enter number of Quiz:"))

for x in range (numq):
    print("Enter Score for quiz",x+1,end=": ")
    quiz = int(input())
    info["Quiz"].append(quiz)
numh = int(input("Enter number of Homework:"))

for i in range (numh):
    print("Enter Score for homework",i+1,end=": ")
    homework = int(input())
    info["Homework"].append(homework)


exam = int(input("Enter major exam: "))
info["Exam"] = exam
calculate()
printinfo()
print("Letter Grade",end=" ")
lettergrade()
