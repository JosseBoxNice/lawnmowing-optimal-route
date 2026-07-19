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


def next_pos(position: tuple[int, int], dir: str) -> tuple[bool, tuple[int, int], str]:

    nextPos: tuple[int, int] = position

    # if 0 <= y <= len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == "#":
    #    return isCrossroads, nextPos, dir
    print(pathOptions)
    print(dir)
    print(nextPos)
    return isCrossroads, nextPos, dir


def scan_around(dir: str) -> tuple[bool, list[str]]:
    directions: dict[str, tuple[int, int]] = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    turn_left: dict[str, str] = {
        "up": "left",
        "left": "down",
        "down": "right",
        "right": "up",
    }

    turn_around: dict[str, str] = {
        "up": "down",
        "down": "up",
        "right": "left",
        "left": "right",
    }

    turn_right: dict[str, str] = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up",
    }

    pathOptions: list[str] = []
    i = 0
    while i <= 3:
        dx, dy = directions[dir]
        x, y = position
        nextPos = (x + dx, y + dy)
        x, y = nextPos
        # save different options ec. ["#"] to access later.
        if 0 <= y <= len(grid) and 0 <= x < len(grid[0]):
            if grid[y][x] == "#":
                pathOptions.append(dir)

        if i == 0:
            dir = turn_left[dir]
        elif i == 1:
            dir = turn_around[dir]
        elif i == 2:
            dir = turn_right[dir]
        i += 1

    # check if isCrossroads
    isCrossroad: bool = False
    if len(pathOptions) > 1:
        isCrossroad = True

    return isCrossroad, pathOptions


dir = "up"
grid: list[list[str]] = create_grid(map=maptxt)
position: tuple[int, int] = find_lawnmower(grid)

while any("#" in row for row in grid):
    grid[position[1]][position[0]] = "="

    isCrossroad, pathOptions = scan_around(dir)
    print(pathOptions, isCrossroad)
    isCrossroads, position, dir = next_pos(position, dir)

    for line in grid:
        print(line)
    print("------------------------------------------------------")

    crossroards: crossroads = crossroads(position)
