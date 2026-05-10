import random

def generate_question():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)

    if second_number > first_number:
        temporary_number = first_number
        first_number = second_number
        second_number = temporary_number

    return first_number, second_number


def check_answer(first_number, second_number, user_answer):
    correct_answer = first_number - second_number

    if user_answer == correct_answer:
        return True

    return False


def calculate_score(correct_answers, total_questions):
    score = (correct_answers / total_questions) * 100
    return score


def ask_question(first_number, second_number):
    attempts = 2

    while attempts > 0:
        answer = int(input(f"What is {first_number} - {second_number}? "))

        if check_answer(first_number, second_number, answer):
            print("Correct!")
            return True
        else:
            attempts -= 1
            print("Wrong answer.")

            if attempts > 0:
                print("Try again.")

    print("No attempts left!")
    return False
