# Nested loops

groups = [["Paul", "Skinny"], ["ahmad", "Gregory"]]
# This outer loop will iterate over each list in the groups list
for group in groups:
    # this inner loop will go through each name in each list
    for name in group:
        print(name)

