import pandas

data = pandas.read_csv("C:/Python/Day 25/Squirrel/squirrels.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_count)

black_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_count)

red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("C:/Python/Day 25/Squirrel/squirrel_count.csv")