# DYNAMIC PROGRAMMING


# Given word_a, find the matching letters between word_b
word_a = [*"FOSH"]
word_b = [*"FISH"]
grid = [[0] * len(word_a) for _ in word_b]

for y_idx, row in enumerate(grid):
    for x_idx, _ in enumerate(row):
        # print()
        print(x_idx)
        # print(f"{(x_idx, y_idx), word_b[x_idx]=}")
        # print(f"{(x_idx, y_idx), word_a[x_idx]=}")
        if word_b[y_idx] == word_a[x_idx]:
            row[x_idx] = 1
            # row[x_idx] += grid[y_idx-1][x_idx-1]


for row in grid:
    print(row)
