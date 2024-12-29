def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = input("Please enter the number of your answer: ")

    if options[int(answer) - 1] == correct_answer:
        print("Correct! Well done.\n")
        return True
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")
        return False


def play_kbc():
    print("Welcome to Kaun Banega Crorepati With Safia Khatoon!")
    print("Let's begin the game.\n")

    # Define the questions, options, and correct answers
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
            "answer": "Delhi"
        },
        {
            "question": "Who is known as the father of the nation in India?",
            "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhash Chandra Bose", "Sardar Patel"],
            "answer": "Mahatma Gandhi"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "Which is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Leo Tolstoy"],
            "answer": "William Shakespeare"
        }
    ]

    # Start asking questions
    for i, q in enumerate(questions):
        correct = ask_question(q["question"], q["options"], q["answer"])
        if not correct:
            print("Game Over! Better luck next time.")
            break
    else:
        print("Congratulations! You have answered all the questions correctly.")


if __name__ == "__main__":
    play_kbc()
