import random

total_numbers=5
total_lives=20
min_val=1
max_val=100

numbers_list=[]
for i in range(total_numbers):
    new_number = random.randint(min_val,max_val)
    while new_number in numbers_list:
        new_number = random.randint(min_val,max_val)
    numbers_list.append(new_number)
numbers_list.sort()

numbers_list_copy=numbers_list.copy()

print(f"There are [{total_numbers}] numbers between {min_val} and {max_val}. Guess them all. If you guess wrong you loose one of your {total_lives} lives!")

def get_hint():
    hint_string="\n[ "
    all_numbers=numbers_list_copy+guesses
    all_numbers.sort()
    all_numbers=list(dict.fromkeys(all_numbers)) #remove duplicates
    for n in all_numbers:
        if n in numbers_list_copy and n in guesses: hint_string += f"\033[32m✔{n}\033[0m "
        elif n in numbers_list_copy and n not in guesses: hint_string += "??? "
        else: hint_string += f"\033[31m✗{n}\033[0m "
    hint_string += "]"
    return f"{hint_string}"

lives=total_lives
guesses=[]
while lives>0:
    user_input=0
    while True:
        try:
            user_input=int(input(f"Enter a number [{lives}/{total_lives}]: "))
            if min_val <= user_input <= max_val:
                if user_input in guesses: print(f"You already guessed {user_input}")
                else: break
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a number")
    guesses.append(user_input)
    if user_input in numbers_list:
        numbers_list.remove(user_input)
        if len(numbers_list)>0:
            print(f"You guessed {user_input} correctly! {get_hint()}")
        else:
            print(f"You guessed all the numbers correctly! You won! [\033[32m {"".join(str(num) + " " for num in numbers_list_copy)}\033[0m]")
            break
    else:
        print(f"Wrong. There is no {user_input} in the list. {get_hint()}")
        lives-=1
else:
    print(f"You lost all your lives!\nThe numbers were [ {"".join(str(num) + " " for num in numbers_list_copy)}] and you managed to guess {len(numbers_list_copy) - len(numbers_list)} numbers.)")
