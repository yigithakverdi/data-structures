## Boilerplate code for Depth First Search (DFS) algorithm for a 2D matrix
def dfs(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    stack = [start]
    visited = set()

    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # Process the current cell
        print(matrix[r][c], end=' ')
        
        # Check all four possible directions (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                stack.append((nr, nc))

## Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# start_position = (0, 0)  # Starting from the top-left corner
# dfs(matrix, start_position)

def dfs_recursive_v1(matrix, r, c, visited):
    rows, cols = len(matrix), len(matrix[0])
    
    # Check if the current cell is out of bounds or already visited
    if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
        return
    
    # Mark the current cell as visited
    visited.add((r, c))
    
    # Process the current cell
    print(matrix[r][c], end=' ')
    
    # Recursively visit all four possible directions (up, down, left, right)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs_recursive_v1(matrix, r + dr, c + dc, visited)

##  Wrapper function to initiate the DFS
# def dfs(matrix, start):
#     visited = set()
#     dfs_recursive_v1(matrix, start[0], start[1], visited)
#
# # Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# start_position = (0, 0)  # Starting from the top-left corner
# dfs(matrix, start_position)

## Code is taken form the following source -> https://www.youtube.com/watch?v=155rbd224H0
## Translated from C++ to Python 
def dfs_recursive_v2(matrix, x, y, visited):
    
    def isValid(matrix, visited, x, y):
        rows, cols = len(matrix), len(matrix[0])
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y]
    
    visited[x][y] = True
    print(matrix[x][y], end=' ')
    
    # Check and move up
    if isValid(matrix, visited, x - 1, y):
        dfs_recursive_v2(matrix, x - 1, y, visited)
    
    # Check and move right
    if isValid(matrix, visited, x, y + 1):
        dfs_recursive_v2(matrix, x, y + 1, visited)
    
    # Check and move down
    if isValid(matrix, visited, x + 1, y):
        dfs_recursive_v2(matrix, x + 1, y, visited)
    
    # Check and move left
    if isValid(matrix, visited, x, y - 1):
        dfs_recursive_v2(matrix, x, y - 1, visited)


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    dfs_recursive_v2(matrix, 0, 0, visited)
    print("")

if __name__ == "__main__":
    main()



