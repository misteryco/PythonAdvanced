food_data = "#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|"
food_data = food_data.split("|")
for index in range(len(food_data)):
    if "#" in food_data[index]:
        food_data[index] = food_data[index].split("#")
print(food_data)
