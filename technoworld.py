class TechWorld:
    def __init__(self,name,skills,exp,feedback):
        self.name = name
        self.skills = skills
        self.exp = exp
        self.feedback = feedback

    def eligibility(self):
        if self.exp > 3 and self.feedback >= 4.5:
            return True

        elif self.exp <= 3 and self.feedback >= 4:
            return True

        else:
            return False

    def course(self,tech):
        iseligible = self.eligibility()
        if iseligible:
            if tech in self.skills:
                print(f"He can teach {tech}")

            else:
                print(f"He cannot teach {tech}")

        else:
            print("He is not elligible as a teacher")

professor = TechWorld('dhruv',['datascience'],3,4.2)
professor.course('webdev')

