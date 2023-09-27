# Creating a grid called "Minsweeper"
       
minesweeper = [["-", "#", "-", "-"],
             ["#", "#", "-","#"],
             ["-", "-", "#", "-"],
             ["#", "-", "#", "-"]]


# Using a for loop to determine the current position that will be used to check the 
# adjacent position
for row1, row in enumerate(minesweeper):
    for col1, cols in enumerate(row):
        count = 0
        if cols == "-":
            
            # Checking the adjacent position of the top left index
            if row1 > 0 and col1 > 0 and minesweeper[row1 - 1][col1 - 1] == "#":
                count += 1
            
            # Checking the top position index
            if row1 > 0 and minesweeper[row1 - 1][col1] == "#":
                count += 1
            
            # Checking the north east adjacent position
            if row1 > 0 and col1 < 3 and minesweeper[row1 -1][col1 + 1] == "#":
                count += 1
            
            # Checking the east adjacent position and making sure not to go out of bounds
            if col1 < 3 and minesweeper[row1][col1 + 1] == "#":
                count += 1
            
            # Checking the south east adjacent position
            if col1 < 3 and row1 < 3 and minesweeper[row1 + 1][col1 + 1] == "#":
                count += 1
            
            # Checking the south adjacent position and making sure not to go out of bounds
            if row1 < 3 and minesweeper[row1 + 1][col1] == "#":
                count += 1
            
            # Checking the south west adjacent position
            if row1 < 3 and col1 > 0 and minesweeper[row1 + 1][col1 - 1] == "#":
                count += 1
            
            # Checking the west adjacent position
            if col1 > 0 and minesweeper[row1][col1 -1] == "#":
                count += 1
            
            # Replace the current positions by the count  
            minesweeper[row1][col1] = count
            

# Printing the grid showing the number of count
for row in minesweeper:
    print(row)
        
            
    