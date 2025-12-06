import random
import time

matches = 0
wins = 0
loses = 0
draws = 0
easters = ["кристина", "папоротник", "понюхай моего отродия"]
easters_found = []

def game():
    global wins, loses, draws, matches, easters
    choice = input("Камень, ножницы или бумага?\n").lower()
    ran = random.randint(1, 3)
    if ran == 1:
        choice2 = "камень"
    elif ran == 2:
        choice2 = "ножницы"
    elif ran == 3:
        choice2 = "бумага"
    if choice == choice2:
        print(f"Ничья! Вы оба показали {choice}")
        draws += 1
    elif choice == "камень" and choice2 == "бумага":
        print(f"Ты проиграл! Ты показал {choice}, а твой противник {choice2}")
        loses += 1
    elif choice == "камень" and choice2 == "ножницы":
        print(f"Ты выиграл! Ты показал {choice}, а твой противник {choice2}")
        wins += 1
    elif choice == "бумага" and choice2 == "камень":
        print(f"Ты выиграл! Ты показал {choice}, а твой противник {choice2}")
        wins += 1
    elif choice == "бумага" and choice2 == "ножницы":
        print(f"Ты проиграл! Ты показал {choice}, а твой противник {choice2}")
        loses += 1
    elif choice == "ножницы" and choice2 == "бумага":
        print(f"Ты выиграл! Ты показал {choice}, а твой противник {choice2}")
        wins += 1
    elif choice == "ножницы" and choice2 == "камень":
        print(f"Ты проиграл! Ты показал {choice}, а твой противник {choice2}")
        loses += 1
    elif choice.lower() == "папоротник":
        print("Оооо пасхалочка. Вымри чупакабра")
        easters_found.append("папоротник")
    elif choice.lower() == "кристина":
        print("Оооо пасхалочка. Вымри чупакабра")
        easters_found.append("Кристина")
    elif choice.lower() == "понюхай моего отродия":
        print("Оооо пасхалочка. Вымри чупакабра")
        easters_found.append("понюхай моего отродия")
    else:
        print(f"{choice} - некорректное название")
    if len(easters_found) == len(easters):
        print(f"Ты собрал все пасхалки:")
        for easter in easters:
            print(easter)
        
while True:
    game()
    print(f"Из {matches} игр {wins} побед, {loses} проигрышей, {draws} ничей. ")
    print("")