class FlashCard:
    def __init__(self):
        import random
        self.fruits = {"Banana": "yellow", "Strawberries": "pink" ,"orange": "orange", "apple": "red"}
        self.k = list(self.fruits.keys())
        self.fruit = random.choice(self.k)

    def quiz(self):
        while True:
            print("Welcome to fruits quiz..\n")
            answer = input(f"what is the color of {self.fruit} ?\n")
            if answer == self.fruits[self.fruit]:
                print("Your answer is correct")

            else:
                print("your answer is wrong")

            key = input("Enter 0 to play again\n")
            if key != '0':
                break


flash = FlashCard()
flash.quiz()
