questions = (
    "What is the name of the main character in Avatar?: ",
    "What is the most populated country?: ",
    "What is the name of the element Cl?: ",
    "What is the name of Taylor Swift's last album?: ",
    "What is the name of Minnesota's NFL team?: "
)

options = (
    ("A. Spider", "B. Jake Sully", "C. Lo'ak", "D. Manaswini"),
    ("A. India", "B. China", "C. Australia", "D. Mozambique"),
    ("A. Aluminum", "B. Chlorine", "C. Hydrogen", "D. Chloride"),
    ("A. 1989", "B. Debut", "C. Fearless", "D. The Life of a Showgirl"),
    ("A. Bears", "B. Packers", "C. Vikings", "D. Twins")
)

answers = ("B", "A", "B", "D", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("-------------------------")
print("        RESULTS          ")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")