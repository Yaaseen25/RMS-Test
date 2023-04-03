def count_combinations(grid, length):
    nrows = len(grid)
    ncols = len(grid[0])

    # Compute the number of combinations in the horizontal and vertical directions
    num_combinations_horizontal_vertical = (nrows - length + 1) * (ncols - length + 1) * 2

    # Compute the number of combinations in the diagonal directions
    num_combinations_diagonal = 2 * (nrows - length + 1) * (ncols - length + 1) - (nrows - length + 1) * 4

    total_combinations = num_combinations_horizontal_vertical + num_combinations_diagonal

    return total_combinations



def find_largest_product(grid, length):
    nrows, ncols = len(grid), len(grid[0])
    max_product = 0

    # Check horizontal products
    for row_idx in range(nrows):
        for col_idx in range(ncols - length + 1):
            product = 1
            for i in range(length):
                product *= grid[row_idx][col_idx + i]
            max_product = max(max_product, product)

    # Check vertical products
    for row_idx in range(nrows - length + 1):
        for col_idx in range(ncols):
            product = 1
            for i in range(length):
                product *= grid[row_idx + i][col_idx]
            max_product = max(max_product, product)

    # Check diagonal products (down-right)
    for row_idx in range(nrows - length + 1):
        for col_idx in range(ncols - length + 1):
            product = 1
            for i in range(length):
                product *= grid[row_idx + i][col_idx + i]
            max_product = max(max_product, product)

    # Check diagonal products (up-right)
    for row_idx in range(length - 1, nrows):
        for col_idx in range(ncols - length + 1):
            product = 1
            for i in range(length):
                product *= grid[row_idx - i][col_idx + i]
            max_product = max(max_product, product)

    # Return the maximum product found
    return max_product



grid = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
    [24, 55, 58,5, 66, 73, 99, 26, 97, 17],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45]
    ]
length = 3

combinations = count_combinations(grid, length)
print("Number of different combinations:", combinations)

largest_product = find_largest_product(grid,length)
print("The largest product is: ",largest_product)




