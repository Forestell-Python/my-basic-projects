import time
import random
from datetime import datetime, timedelta

bal = 0
recipes = """
Recipe book:
boiled egg - take an egg, throw into boiling water
pasta - take frozen pasta, fry in a pan,
...
"""
clients = ["Ghost", "Skeleton", "Zombie"]
food = ["boiled egg", "pasta", "sushi"]
drinks = ["water", "coke", "milk"]

def ordering():
    global orderded_food, orderded_drink
    cl = random.choice(clients)
    #food_amount = random.randint(len(food))
    orderded_food = random.choice(food)
    orderded_drink = random.choice(drinks)
    print(f"{cl} ordered {orderded_food} and {orderded_drink}")
    print("It's cooking time!")
    cooking()

def cooking():
    global products, method
    print(f"Let's cook {orderded_food}!")
    print(recipes)
    products = []
    producting = True
    while producting == True:
        print("Choose a product:")
        print(f"Your products: {products}")
        print("1. An egg\n2. Pasta\n3. Rice\n4. Delete\n5. Stop")
        choice = input("Adding? ")
        if choice == "1":
            products.append("egg")
        elif choice == "2":
            products.append("pasta")
        elif choice == "3":
            products.append("rice")
        elif choice == "4":
            products.clear()
        elif choice == "5":
            producting = False
        else:
            print("incorrect symbols\n ")
    print(f"You took {products}")


    doing = True
    while doing == True:
        print("What do I do?")
        print("1. boil\n2. fry\n3. Roll up")
        ch = input("What? ")
        if ch == "1":
            method = "boiled"
            print("Boiling...")
            doing = False
        elif ch == "2":
            method = "fried"
            print("Frying...")
            doing = False
        elif ch == "3":
            method = "rolled up"
            print("Rolling up...")
            doing = False
        else:
            print("Incorrect symbol")
        print(f"I took {products} and {method} them!")
    comparing()
    drink_result = make_drink(orderded_drink)
    
    if result == orderded_food and drink_result == orderded_drink:
        print("🎉 Весь заказ выполнен идеально!")
        bal += 100
    else:
        print("💸 Часть заказа не выполнена...")

def comparing():
    global result, bal
    
    temp_products = products.copy()
    
    if "egg" in temp_products and method == "boiled":
        temp_products.remove("egg")
        if len(temp_products) == 0:
            result = "boiled egg"
    
    elif "pasta" in temp_products and method == "fried":
        temp_products.remove("pasta") 
        if len(temp_products) == 0:
            result = "pasta"
            
    elif "rice" in temp_products and method == "rolled up":
        temp_products.remove("rice")
        if len(temp_products) == 0:
            result = "sushi"
    
    else:
        result = "failed dish"
    
    if result == orderded_food:
        print(f"Perfect! Client got {result}")
        bal += 50
    else:
        print(f"Failed! Made {result}, but ordered {orderded_food}")
    
    print(f"Balance: {bal}")

def make_drink(ordered_drink):
    print(f"\n🧃 Клиент заказал: {ordered_drink}")
    
    drinks_recipes = {
        "water": ["1. Взять стакан", "2. Открыть кран", "3. Налить воду"],
        "coke": ["1. Взять банку", "2. Открыть банку", "3. Налить в стакан"], 
        "milk": ["1. Взять пакет", "2. Открыть пакет", "3. Налить молоко"]
    }
    
    if ordered_drink in drinks_recipes:
        print("📋 Рецепт:")
        for step in drinks_recipes[ordered_drink]:
            print(step)
            time.sleep(1)
            
        print(f"✅ {ordered_drink} готов!")
        return ordered_drink
    else:
        print("❌ Такого напитка нет в меню")
        return "failed drink"

ordering()

def cooking():
    global products, method
    print(f"Let's cook {orderded_food}!")
    print(recipes)
    products = []
    producting = True
    
    # 1. Собираем продукты
    while producting == True:
        print("Choose a product:")
        print(f"Your products: {products}")
        print("1. An egg\n2. Pasta\n3. Rice\n4. Delete\n5. Stop")
        choice = input("Adding? ")
        if choice == "1":
            products.append("egg")
        elif choice == "2":
            products.append("pasta")
        elif choice == "3":
            products.append("rice")
        elif choice == "4":
            products.clear()
        elif choice == "5":
            producting = False
        else:
            print("incorrect symbols\n ")
    print(f"You took {products}")

    # 2. Выбираем метод готовки
    doing = True
    while doing == True:
        print("What do I do?")
        print("1. boil\n2. fry\n3. Roll up")
        ch = input("What? ")
        if ch == "1":
            method = "boiled"
            print("Boiling...")
            doing = False
        elif ch == "2":
            method = "fried"
            print("Frying...")
            doing = False
        elif ch == "3":
            method = "rolled up"
            print("Rolling up...")
            doing = False
        else:
            print("Incorrect symbol")
    
    print(f"I took {products} and {method} them!")