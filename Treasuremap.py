#!/usr/bin/env python3

#Treasure map

# ð¨ Don't change the code below ð
row1 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row2 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row3 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ð¨ Don't change the code above ð

#Write your code below this row ð

horizontal = int(position[0])
vertical= int(position[1])

#replace the treasture area with a crown jewel 
selected_row =map[vertical-1]
selected_row[horizontal-1] = "ð"







# ð¨ Output belowð
print(f"{row1}\n{row2}\n{row3}")