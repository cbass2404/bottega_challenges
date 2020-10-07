def matrix_builder(start, grid):
    matrices = []

    for i in range(grid):
        new_array = []
        end = start + grid
        for n in range(start, end):
            new_array.append(n)
        start += 1
        matrices.append(new_array)
    return matrices


print(matrix_builder(10, 5))
