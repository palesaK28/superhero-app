foods = []
prices = []
total = 0.0

while True:
    food = input("Enter food item (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    price = float(input(f"Enter price for {food}: R"))
    
    foods.append(food)
    prices.append(price)
    
    
    print("-------YOUR CART-------")

for i in range(len(foods)):
    print(f"{foods[i]}: R{prices[i]}")
    total += prices[i]

print("\n")
print(f"your total is: R{total}")