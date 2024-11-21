# class Movie():
#     def __init__(self, title, director, duration):
#         self.title = title
#         self.director = director 
#         self.duration = duration
#         print("movie object created")
#     def __str__(self):
#         return f"{self.title} by {self.director}"
#     def __len__(self):
#         return self.duration
    
# m = Movie("film adi", "yonetmen adi", 10)
# print(str(m))
# print(len(m))





# class Movie():
#     def __init__(self, title, director, duration):
#         self.title = title
#         self.director = director 
#         self.duration = duration
#         print("movie object created")
#     def __str__(self):
#         return f"{self.title} by {self.director}"
#     def __len__(self):
#         return self.duration
#     def __del__(self):
#         print("movie object deleted")
    
# m = Movie("film adi", "yonetmen adi", 10)
# del m
# print(m)

# class Question():
#     def __init__(self, text, choices, answer):
#         self.text = text
#         self.choices = choices
#         self.answer = answer

#     def checkAnswer(self, answer):
#         return self.answer == answer

# q1 = Question("en ii programlama dili hangisi ? ", ["c#" , "python", "java"], "python")
# q2 = Question("en popüler programlama dili hangisi ? ", ["python", "java", "c#"], "python")
# q3 = Question("en çok kazandıran programlama dili hangisi ? ", ["c#" , "java", "python"], "python")

# questions = [q1, q2, q3]
# # print(q1.checkAnswer("python"))
# # print(q2.checkAnswer("java"))
# # print(q3.checkAnswer("c#"))


# class Quiz():
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0
#         self.questionIndex = 0 # questions listesindeki soru indexi



class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"soru {self.questionIndex + 1} : {question.text} ")

        for q in question.choices:
            print("-" + q)
        answer = input("cevap : ")
        self.guess(answer)
        self.loadQuestion()
    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showScore(self):
        print("score :" , self.score )
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestion} ".center(100,"*"))
            

q1 = Question("en ii programlama dili hangisi ? ", ["c#" , "python", "java"], "python")
q2 = Question("en popüler programlama dili hangisi ? ", ["python", "java", "c#"], "python")
q3 = Question("en çok kazandıran programlama dili hangisi ? ", ["c#" , "java", "python"], "python")
questions = [q1, q2, q3]

quiz = Quiz(questions)
quiz.loadQuestion()


