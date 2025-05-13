import json
import random
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)  # Enable color reset after each print

def load_questions(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def choose_category(categories):
    print(f"{Fore.CYAN}Available Categories:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    try:
        choice = int(input(f"\n{Fore.YELLOW}Select a category (1-{len(categories)}): "))
        return categories[choice - 1]
    except:
        print(f"{Fore.RED}Invalid selection. Defaulting to {categories[0]}.")
        return categories[0]

def run_quiz(questions, category):
    print(f"\n{Fore.CYAN}Starting quiz for category: {category}\n")
    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        print(f"{Fore.CYAN}Q{i}: {q['question']}")
        for idx, opt in enumerate(q['options'], 1):
            print(f"{idx}. {opt}")
        try:
            ans = int(input(f"{Fore.YELLOW}Your answer (1-{len(q['options'])}): "))
            if q['options'][ans - 1].lower() == q['answer'].lower():
                print(f"{Fore.GREEN}✅ Correct!\n")
                score += 1
            else:
                print(f"{Fore.RED}❌ Incorrect! Correct: {q['answer']}\n")
        except:
            print(f"{Fore.RED}⚠️ Skipped due to invalid input.\n")

    print(f"{Fore.CYAN}You scored {score} out of {len(questions)}.\n")
    return score

def save_score(name, category, score, total):
    with open("scores.txt", "a") as f:
        f.write(f"{datetime.now()} | {name} | {category} | {score}/{total}\n")

def main():
    print(f"{Fore.MAGENTA}Welcome to 3MTT LearnBot - Expanded Edition!")
    name = input("Enter your name: ").strip()
    questions_by_category = load_questions("questions.json")
    category = choose_category(list(questions_by_category.keys()))
    score = run_quiz(questions_by_category[category], category)
    save_score(name, category, score, len(questions_by_category[category]))

    print(f"{Fore.GREEN}Thanks for using LearnBot, {name}! Your score has been saved.")

if __name__ == "__main__":
    main()
