number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [13]
]

print(number_grid[0][0])

# for row in number_grid:
#     print(row)

for row in number_grid:         #to access the elements inside the rows of the list
    for col in row:              
        print(col)           