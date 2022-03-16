grid = []
height = 10
width = 10 
carre = "▉"

for i in range(height):
    grid.append([])
    for j in range(width):
        grid[i].append(j)

for i in range(height):
    for j in range(width):
        print(grid[i][j], end=" ")
    print()