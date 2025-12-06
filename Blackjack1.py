#Blackjack parody
import random

wins = 0
draws = 0
loses = 0
blackjacks = 0
bal = 1000
earned = 0

def get_bet():
    while True:
        bet_input = input(f"Enter your bet (Your balance {bal}): ")
        if bet_input.isdigit():
            bet = int(bet_input)
            if bet > bal:
                print("Not enough money!")
            else:
                return bet
        else:
            print("Please, enter a NUMBER!")

def blackjack():
    global wins, draws, loses, blackjacks, bal, earned
    score = 0
    dscore = 0
    want = True
    
    bet = get_bet()
    bal -= bet
    earned -= bet
    print(f"Your bet: {bet}. Your current balalnce : {bal}")
    
    while want == True:
        card = random.randint(2, 11)
        choice = input("Do you want to take a card? ")
        if choice.lower() == "yes": 
            score += card
            print(f"You took: {card}. Your score: {score}")
        elif choice.lower() == "no":
            print(f"Your score: {score}")
            want = False
        else:
            print("Incorrect word. Please, enter 'yes' or 'no' ")
            continue
        
        
    while dscore < 17:
        dcard = random.randint(2, 11)
        dscore += dcard
        
    print(f"Diller's score is {dscore}")
        
    if score == dscore:
        print(f"Draw! Your score is {score}")
        draws += 1
        bal += bet
    elif score > dscore and score < 22 and score != 21:
        print(f"Win! Your score is {score}, and the diller's one is {dscore}")
        wins += 1
        bal += bet * 2
    elif score == 21:
        print("BLACKJACK!!! YOU WON")
        wins += 1
        blackjacks += 1
        bal += bet * 2.5
    elif score > 21 and dscore < 22:
        print(f"Loss! Your score's over 21 {score}, diller's one is {dscore}")
        loses += 1
    elif score > 21 and dscore > 22:
        print(f"Draw! You both have an overscore {score} and {dscore}")
        draws += 1
        bal += bet
    elif score < 22 and dscore > 21:
        print(f"Win! Your score is {score}, and diller's one is {dscore}")
        bal += bet * 2
    elif score < dscore and dscore < 22:
        loses += 1
        print(f"Loss! Your score is {score}, and diller's one is {dscore}!")
        
def check_stats():
        earned = bal - 1000
        print(f"balance - {bal}$")
        print(f"{wins} wins")
        print(f"{draws} draws")
        print(f"{loses} loses")
        print(f"{blackjacks} blackjacks")
        print(f"earned {earned}$")
        
while True:
    print("=" * 40)
    print("BLACKJACK 1.0")
    print("=" * 40)
    ch = input("Enter '1' to start the game, '2' to look at your stats: ")
    if ch == "1":
        blackjack()
        print("")
    elif ch == "2":
        check_stats()
    else:
        print("Incorrect symbol!")
