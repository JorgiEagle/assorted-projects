fruits = ["apple", "orange", "b", "grape", "S", "blue", "mando"]
prices = [125, 75, 50, 200, 350, 400, 175]

fruit_prices = [(fruit, price) for fruit, price in zip(fruits, prices)]
filtered_fruit_prices = [fp for fp in fruit_prices if 1<=fp[1]<=3]
sorted_fruit_prices = sorted(filtered_fruit_prices, key=lambda x: x[1], reverse=True)

print(sorted_fruit_prices)


filtered_fruit_prices = [(fruit, price) for fruit, price in zip(fruits, prices) if 1 <= price <=3]
sorted_fruit_prices = sorted(filtered_fruit_prices, key=lambda x: x[1], reverse=True)

print(sorted_fruit_prices)