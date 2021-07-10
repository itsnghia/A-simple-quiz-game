
def new_game():
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print("-------------------")
    print(key)
    for i in options[question_num - 1]:
      print(i)
    guess = input("Enter either A, B, C or D: ").upper().strip()
    while (guess != "A" and guess != "B" and guess != "C" and guess != "D"):
      guess = input("Enter either A, B, C or D: ").upper().strip()
    guesses.append(guess)
    question_num += 1
  correct_guesses = check_answer(guesses)
  display_score(len(questions), correct_guesses)
  play_again()
   

def check_answer(choices):
  correct_choices = 0
  correct_answers = []
  for key in questions:
    correct_answers.append(questions[key])
  for i in range(0, len(choices)):
    if choices[i] == correct_answers[i]:
      correct_choices += 1
  return correct_choices


def display_score(question_nums ,c_choices):
  score = 10 / int(question_nums) * int(c_choices)
  return print("You got " + str(score) + "/10")

  

def play_again():
  again = input("Do you want to play again? (Yes/No): ").lower().strip()
  while (again != "yes" and again != "no"):
    again = input("Enter Yes or No only: ").lower().strip()
  if (again == "yes"):
    new_game()
    return True
  else: 
    print("Bye!!")
    return False
    

questions = {
  "What is your name" : "A",
  "When were you born?" : "B",
  "Where were" : "A",
  "Is the Earth round?" : "A"
}

options = [["A. Huynh Dai Nghia", "B. Bill Gates", "C. Calum Scott", "D. Elon Musk"],
           ["A. 1969", "B. 1999", "C. 2001", "D. 2002"],
           ["A. Hanoi", "B. Thai Binh", "C. Thanh Hoa", "D. Ha Tinh"],
           ["A. True", "B. False", "C. Sometimes", "D. The Earth is f*cking flat!!!"]]


new_game()
