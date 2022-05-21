from random import sample

fruits = [
    {"item":"Cucumber Batons" , "price" : 0.40 },
    {"item":"Diced Swede", "price" : 0.40},
    {"item":"Carrots & Peas","price" : 0.85},
    {"item":"Strawberries", "price" : 3.00},
    {"item":"Washed Potatoes","price" : 2.50},
    {"item":"Spring Onions","price" : 0.65}
]
chosen_item = (sample(fruits, 3))
print(chosen_item)