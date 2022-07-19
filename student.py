from datetime import datetime, timedelta

class Student:
    Scores = {}

    # Programmer Information
    # Name: FNU Tripti
    # A-ID: A20503656
    # Course: ITMD-513
    # Date: 07/15/2022
    # Lab #: 6

    # initializing the constructor method
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getScores(self):

        answer_key = []
        # read into answer_key list, the answer key from file
        answer_key = [line.strip() for line in open("answers.txt", 'r')]

        student_answers = []
        # read into student_answers list, student answers from file
        student_answers = [line.strip().split(',')
                           for line in open("data.txt", 'r')]
        total_score = 100

        # place additional code statements here for the above function
        # ---start your loop processing logic here---#

        for i in range(len(student_answers)):
            if student_answers[i][0] == self.getName():
                for key in range(len(answer_key)):
                    if answer_key[key] != student_answers[i][key + 1]:
                        total_score -= 10

        # ---end your loop processing logic here---#

        # ---continue the class definition#

        Student.Scores[self.getName()] = total_score

    def getName(self):
        return self.name

    # Method added to get the current grades.
    def getGrades(self):
        return self.grade

    @staticmethod
    def printSummary(sorted_list):
        print("This program for course ITMD-513 is executed by FNU Tripti (A20503656) on : ", datetime.now() - timedelta(2))
        overall_average = 0.0
        overall_aggregate = 0.0
        count = 0
        for k, v in sorted_list:
            # print(k.title(), "has score:", v)
            for w in range(len(student_objs)):
                if k == student_objs[w].getName():
                    z = student_objs[w].getGrades()
            print(k.title(), "has Old score:", z)
            print(k.title(), "has New score:", v)
            print("Average Grade:", ((z + v)/2))
            print("Grade Range:", abs(z - v), "\n")
            overall_average += ((z + v)/2)
            overall_aggregate += abs(z - v)
            count += 1

        print("Overall Average Grade:", (overall_average/count))
        print("Overall Average Grade Range:", (overall_aggregate/count))

    @staticmethod
    def sortDict():
        return sorted(Student.Scores.items())

    # ---end the class definition#


student_objs = [

    Student('Sammy Student', 65),
    Student('Betty sanchez', 45),
    Student('Alice brown', 100),
    Student('tom Schulz', 50),
    Student('fNU Tripti', 95)
]

for index in range(len(student_objs)):
    student_objs[index].getScores()

sortList = Student.sortDict()

Student.printSummary(sortList)

