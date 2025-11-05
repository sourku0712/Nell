''' 0 for Rock
    1 for Paper
    2 for Scissor '''
def game(u):
    import random
    comp= random.choice([0,1,2])
    dict= {"rock":0, "paper":1, "scissor":2}
    user= dict[u]
    rev_dict= {0: "rock", 1: "paper", 2: "scissor"}
    print(f"You chose: {rev_dict[user]} \nComputer chose: {rev_dict[comp]}")
    if (comp==user):
        print("It's a draw")
    else:
        if (comp== 0 and user== 1):
            print("You win")
        if (comp== 0 and user == 2):
            print("You lose")
        if (comp== 1 and user == 0):
            print("You lose")
        if (comp== 1 and user == 2):
            print("You win")
        if (comp== 2 and user == 0):
            print("You win")
        if (comp== 2 and user == 1):
            print("You lose")

print("We are playing rock, paper & scissor")
while True:
    u= input("Your choice: ")
    if u:
        if u.lower() in ['exit', 'quit', 'stop']:
            print("Goodbye!")
            break
        game(u)