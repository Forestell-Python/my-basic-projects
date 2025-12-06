import time

positions = [
    {"id": 1, "name": "RedBull", "price": 150, "stock": 5},
    {"id": 2, "name": "Cola", "price": 80, "stock": 10},
    {"id": 3, "name": "Mineral Water", "price": 50, "stock": 13},
    {"id": 4, "name": "Apple juice", "price": 72, "stock": 4},
    {"id": 5, "name": "Coffee 3-in-1", "price": 60, "stock": 9},

    {"id": 6, "name": "Chocolate 'Black Gold'", "price": 65, "stock": 7},
    {"id": 7, "name": "Chips 'Lays'", "price": 120, "stock": 16},
    {"id": 8, "name": "Cookies 'Anniversary'", "price": 55, "stock": 8},
    {"id": 9, "name": "Kiriyeshki", "price": 45, "stock": 1},
    {"id": 10, "name": "Bubble Gum", "price": 30, "stock": 0},

    {"id": 11, "name": "Chupa", "price": 40, "stock": 7},
    {"id": 12, "name": "Sweet Bears", "price": 90, "stock": 7},
    {"id": 13, "name": "Sneakers", "price": 55, "stock": 7},
    {"id": 14, "name": "Child's happieness", "price": 35, "stock": 7},
    {"id": 15, "name": "Red October", "price": 25, "stock": 7}
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
        print("An error")
    
    money -= kupura
    sdacha = kupura - cost
    money += sdacha
    print(kupura)
    print(sdacha)

def buy():
    global money
    while True:
        for position in positions:
            print(f"№{position['id']} {position['name']}, {position['price']}₽, {position['stock']} left")
            time.sleep(0.2)
        print(money)
        print("")
        choice = input("Enter the number: ")
        for position in positions:
            if choice == str(position["id"]):
                print(f"{position['name']} costs {position['price']}₽")
                sure = input(f"Do you want to buy {position['name']}? ")
                if sure.lower() == "yes":
                    if position["stock"] > 0:
                        if money >= position["price"]:
                            position["stock"] -= 1
                            give_back(position["price"])
                        else:
                            print("Not enough money")
                    else:
                        print(f"{position['name']} ran out!")
                elif sure.lower() == "no":
                    print("An operation was cancelled")
        print("")           

buy()
