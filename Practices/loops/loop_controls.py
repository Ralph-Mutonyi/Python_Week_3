# break in for loop

colors = ["blue", "green", "white", "yellow", "brown", "cream"]

color_i_want = "white"

for color in colors:
    if color == color_i_want:
        print("They have the color i want!")
        break
    print(color)

# break using while loop
    
colors1 = ["blue", "green", "white", "yellow", "brown", "cream"]
color_i_want1 = "white"

length = len(colors1)

count = 0

while  count < length:
    print(colors1[count])

    if colors1[count] == color_i_want1:
        print("They have the color i want!")
        break
    count += 1


