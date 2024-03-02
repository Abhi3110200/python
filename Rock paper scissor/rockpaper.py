import random
item_list=['Rock','Scissor','Paper']

user_choice = input("Enter your move = Rock, Scissor, Paper ")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print('Both chooses same : Match Tie')
    
elif user_choice == 'Rock':
    if comp_choice=='Paper':
        print('Paper covers Rock = Computer Wins')
    else:
        print('Rock Smashes Scissor = You Win')
        
elif user_choice == 'Paper':
    if comp_choice == 'Scissor':
        print('Scissor cuts paper, Computer Wins')
    else:
        print('Paper covers Rock , You Win')
        
elif user_choice == 'Scissor':
    if comp_choice == 'Paper':
        print('Scissor cuts paper , You Win')
    else:
        print('Rock smashes scissor, Computer Wins')