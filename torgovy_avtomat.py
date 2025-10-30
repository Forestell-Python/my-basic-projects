import time

positions = [
    {"id": 1, "name": "Красный Бык", "price": 150, "stock": 5},
    {"id": 2, "name": "Кола", "price": 80, "stock": 10},
    {"id": 3, "name": "Минеральная Вода", "price": 50, "stock": 13},
    {"id": 4, "name": "Сок яблочный", "price": 72, "stock": 4},
    {"id": 5, "name": "Кофе 3 в 1", "price": 60, "stock": 9},

    {"id": 6, "name": "Шоколад 'Черное золото'", "price": 65, "stock": 7},
    {"id": 7, "name": "Чипсы 'Слои'", "price": 120, "stock": 16},
    {"id": 8, "name": "Печенье 'Юбилейное'", "price": 55, "stock": 8},
    {"id": 9, "name": "Сухарики 'Кириешки'", "price": 45, "stock": 1},
    {"id": 10, "name": "Жвачка 'Орбита'", "price": 30, "stock": 0},

    {"id": 11, "name": "Леденец 'Чупсик'", "price": 40, "stock": 7},
    {"id": 12, "name": "Мармеладные мишки", "price": 90, "stock": 7},
    {"id": 13, "name": "Батончик 'Кроссовки'", "price": 55, "stock": 7},
    {"id": 14, "name": "Шоколад 'Ребечачье удовольствие'", "price": 35, "stock": 7},
    {"id": 15, "name": "Звездочки 'Красный Октябрь'", "price": 25, "stock": 7}
]

accepted_banknotes = [50, 100, 200, 500, 1000]
money = 250

def give_back(cost):
    global money
    if cost <= 50:
        kupura = 50
    elif cost <= 100:
        kupura = 100
    elif cost <= 200:
        kupura = 200
    elif cost <= 500:
        kupura = 500
    elif cost <= 1000:
        kupura = 1000
    else:
        print("Ну хз, пиздец какой-то")
    
    money -= kupura
    sdacha = kupura - cost
    money += sdacha
    print(kupura)
    print(sdacha)

def buy():
    global money
    while True:
        for position in positions:
            print(f"№{position['id']} {position['name']}, {position['price']}₽, {position['stock']} шт осталось")
            time.sleep(0.2)
        print(money)
        print("")
        choice = input("Впишите номер позиции: ")
        for position in positions:
            if choice == str(position["id"]):
                print(f"{position['name']} стоит {position['price']}₽")
                sure = input(f"Вы точно хотите купить {position['name']}? ")
                if sure.lower() == "да":
                    if position["stock"] > 0:
                        if money >= position["price"]:
                            position["stock"] -= 1
                            give_back(position["price"])
                        else:
                            print("Недостаточно средств")
                    else:
                        print(f"{position['name']} закончился!")
                elif sure.lower() == "нет":
                    print("Операция отменена")
        print("")           
buy()