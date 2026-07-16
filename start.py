from crossroads import crossroads

with open(file="map/demo.txt") as f:
    maptxt: list[str] = f.read().splitlines()

#   01234
# 0 #####
# 1 ###x#
# 2 ##xxx
# 3 ###x#
# 4 #####
# 5 L####


def create_grid(map: list[str]) -> list[list[str]]:
    grid: list[list[str]] = []

    for line in map:
        row: list[str] = []
        for char in line:
            row.append(char)
        grid.append(row)
    return grid


def find_lawnmower(grid: list[list[str]]) -> tuple[int, int]:
    x: int = 0
    y: int = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "L":
                x = j
                y = i
                break
    return x, y


grid: list[list[str]] = create_grid(map=maptxt)

position: tuple[int, int] = find_lawnmower(grid)

crossroards: crossroads = crossroads(position)
