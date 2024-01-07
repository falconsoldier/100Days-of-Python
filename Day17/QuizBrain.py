class QuizBrain:
    def __init__(self, quizlist):
        self.qnum = 0
        self.score = 0
        self.qlist = quizlist
    
    def still_has_question(self):
        return self.qnum < len(self.qlist)-1
    
    def question(self, jc):
        print(jc["text"])
        ans = input("True or False: ")
        return ans