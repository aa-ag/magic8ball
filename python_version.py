from random import choice

class Magic8Ball():
    def __init__(self, questions=0):
        self.questions = questions

    def convo(self):
        self.questions = input("\n* What's on your mind?\n")
        responses = ['\nYes\n', '\nNo\n', '\nThat is a tough one: ask again in 5 minutes...\n']
        random.choice(responses)

def ask():
    one_question = Magic8Ball()
    while True:
        start = input("\n* Enter 'ask' to get started or 'quit' to leave: \n")
        if start.lower() == 'ask':
            one_question.convo()
        elif start.lower() == 'quit':
            print("\n * Hope this helped!\n")
            break

ask()