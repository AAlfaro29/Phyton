# Q1
# groceries = {
#  "Baby Spinach": 2.78,
#  "Hot Chocolate": 3.70,
#  "Crackers": 2.10,
#  "Bacon": 9.00,
#  "Carrots": 0.56,
#  "Oranges": 3.08  

# }

# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
    
# }

# for key,value in groceries.items():
#      print(f"{quantity[key]} {key} @ ${value}= ${round(quantity[key]*value,2)}")

# Q2

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
    ]

for colour in colours:
        #print(colour)
        #colour_counts[colour] 
        # if colour exist in list
        colour_counts[colour] += 1
for colour in colour_counts:
        print(f"{colours}: {colour_counts[colour]}")

        print(colour_counts)


