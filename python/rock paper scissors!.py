import random

user_wins = 0
computer_wins = 0

options = ["r", "p", "s"]

while True:
    user_input = input("Type [R]Rock [P]Paper or [S]Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock 0, paper 1, scissors 2
    computer_pick = options[random_number]
    print*("computer picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
    print("now your score is", user_wins + ".")
    user_wins += 1
    continue

    elif user_input == "p" and computer_pick == "r"
    print("now your score is", user_wins + ".")
    user_wins += 1

    elif user_input == "s" and computer_pick == "p"
    print("now your score is", user_wins + ".")
    user_wins += 1

    else:
        print("computer got", computer_wins)
        computer_wins +=

print("you won ", user_wins, " time(s)")
print("computer won ", computer_wins, " time(s)")
print("Goodbye!")



    

