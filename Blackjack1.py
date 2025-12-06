#Очко
import random

wins = 0
draws = 0
loses = 0
blackjacks = 0
bal = 1000
earned = 0

def get_bet():
    while True:
        bet_input = input(f"Введите ставку (Ваш баланс {bal}): ")
        if bet_input.isdigit():
            bet = int(bet_input)
            if bet > bal:
                print("Недостаточно денег!")
            else:
                return bet
        else:
            print("Пожалуйста, введите ЧИСЛО!")

def blackjack():
    global wins, draws, loses, blackjacks, bal, earned
    score = 0
    dscore = 0
    want = True
    
    bet = get_bet()
    bal -= bet
    earned -= bet
    print(f"Ваша ставка: {bet}. Ваш баланс : {bal}")
    
    while want == True:
        card = random.randint(2, 11)
        choice = input("Вы хотите взять карту? ")
        if choice.lower() == "да": 
            score += card
            print(f"Вы взяли: {card}. Ваши очки: {score}")
        elif choice.lower() == "нет":
            print(f"Ваши очки: {score}")
            want = False
        else:
            print("Неправильное слово. Введите ''да'' или ''нет'' ")
            continue
        
        
    while dscore < 17:
        dcard = random.randint(2, 11)
        dscore += dcard
        
    print(f"У диллера {dscore} очков")
        
    if score == dscore:
        print(f"Ничья! У вас по {score} очков")
        draws += 1
        bal += bet
    elif score > dscore and score < 22 and score != 21:
        print(f"Победа! У тебя {score} очков, а у диллера - {dscore}")
        wins += 1
        bal += bet * 2
    elif score == 21:
        print("BLACKJACK!!! Вы победили")
        wins += 1
        blackjacks += 1
        bal += bet * 2.5
    elif score > 21 and dscore < 22:
        print(f"Проигрыш! У вас перебор: {score}, а у диллера {dscore}")
        loses += 1
    elif score > 21 and dscore > 22:
        print(f"Ничья! Перебор: {score} и {dscore}")
        draws += 1
        bal += bet
    elif score < 22 and dscore > 21:
        print(f"Победа! У тебя {score} очков, а у диллера {dscore} очков")
        bal += bet * 2
    elif score < dscore and dscore < 22:
        loses += 1
        print(f"Поражение! У вас {score} очков, а у диллера {dscore}!")
        
def check_stats():
        earned = bal - 1000
        print(f"баланс - {bal} денег")
        print(f"{wins} побед")
        print(f"{draws} ничьих")
        print(f"{loses} проигрышей")
        print(f"{blackjacks} блекджеков")
        print(f"заработано {earned} денег")
        
while True:
    print("=" * 40)
    print("BLACKJACK 1.0")
    print("=" * 40)
    ch = input("Нажмите 1 для начала игры, 2 для просмотра статистики: ")
    if ch == "1":
        blackjack()
        print("")
    elif ch == "2":
        check_stats()
    else:
        print("Неопознанный символ!")