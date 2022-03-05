# DYNAMIC PROGRAMMING


# Find longest common substring between word_a and word_b
def longest_common_substring(word_a, word_b):
    word_a = [*word_a]
    word_b = [*word_b]
    grid = [[0] * len(word_a) for _ in word_b]
    for y_idx, row in enumerate(grid):
        for x_idx, _ in enumerate(row):
            if word_b[y_idx] == word_a[x_idx]:
                row[x_idx] = 1
                row[x_idx] += grid[y_idx-1][x_idx-1]
    return grid


# Find longest common subsequence between word_a and word_b
def longest_common_subsequence(word_a, word_b):
    word_a = [*word_a]
    word_b = [*word_b]
    grid = [[0] * len(word_a) for _ in word_b]
    for y_idx, row in enumerate(grid):
        for x_idx, _ in enumerate(row):
            if word_b[y_idx] == word_a[x_idx]:
                row[x_idx] = 1
                row[x_idx] += grid[y_idx-1][x_idx-1]
            else:
                row[x_idx] = max(grid[y_idx-1][x_idx], grid[y_idx][x_idx-1])
    return grid


for row in longest_common_substring("FISH", "FOSH"):
    print(row)


for row in longest_common_subsequence("FISH", "FOSH"):
    print(row)
