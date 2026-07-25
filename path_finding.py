import time
from crossroads import Crossroad


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


def next_pos(position: tuple[int, int], dir: str) -> tuple[int, int]:

    directions: dict[str, tuple[int, int]] = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }
    dx, dy = directions[dir]
    x, y = position
    nextPos = (x + dx, y + dy)

    return nextPos


def scan_around(
    dir: str, position: tuple[int, int], grid: list[list[str]]
) -> dict[str, list[str]]:

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

    pathOptions: dict[str, list[str]] = {
        "#": [],
        "=": [],
    }
    i = 0
    while i <= 3:
        x, y = next_pos(position, dir)
        # save different options ec. ["#"] to access later.
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            symbol: str = grid[y][x]
            if symbol in ("#", "="):
                pathOptions[symbol].append(dir)

        if i == 0:
            dir = turn_left[dir]
        elif i == 1:
            dir = turn_around[dir]
        elif i == 2:
            dir = turn_right[dir]
        i += 1

    return pathOptions


def pathToCrossroad(
    position: tuple[int, int],
    destination: tuple[int, int],
    pathOptions: dict[str, list[str]],
) -> tuple[tuple[int, int], str]:

    # Get positions of possible directions
    optionPositions: list[tuple[tuple[int, int], str]] = []
    for option in pathOptions["="]:
        optionPositions.append((next_pos(position, option), option))

    # print(optionPositions)

    # Get distances to destiantion of possible directions
    distances: list[float] = []
    dx, dy = destination
    for pos in optionPositions:
        x, y = pos[0]
        distances.append(abs((x - dx) + (y - dy)))

    # find shortest dist and get index
    closest: float = float("inf")
    for dist in distances:
        if dist < closest:
            closest = dist
    index: int = distances.index(closest)

    return optionPositions[index][0], optionPositions[index][1]


def printOutput(timeSpent: int, grid: list[list[str]]) -> int:
    timeSpent += 1
    print(timeSpent)
    for line in grid:
        print(line)
    print("------------------------------------------------------")
    time.sleep(0.5)
    return timeSpent


def isTurn(dir: str, newDir: str) -> bool:
    if dir == newDir:
        return False

    turn_around: dict[str, str] = {
        "up": "down",
        "down": "up",
        "right": "left",
        "left": "right",
    }

    if turn_around[dir] == newDir:
        return False

    return True


def no_fresh_grass(position, tempCrossroads, pathOptions, timeSpent, grid, dir):
    while position != tempCrossroads[len(tempCrossroads) - 1]:
        position, newDir = pathToCrossroad(
            position, tempCrossroads[len(tempCrossroads) - 1], pathOptions
        )
        if isTurn(dir, newDir):
            timeSpent += 1
        dir = newDir
        pathOptions = scan_around(dir, position, grid)
        timeSpent = printOutput(timeSpent, grid)
    _ = tempCrossroads.pop()


def execute_path(grid: list[list[str]]) -> tuple[int, list[Crossroad]]:
    # Start variable definitions
    dir = "up"
    position: tuple[int, int] = find_lawnmower(grid)
    tempCrossroads: list[tuple[int, int]] = []
    permCrossroads: list[Crossroad] = []
    timeSpent = 0

    while any("#" in row for row in grid):
        pathOptions = scan_around(dir, position, grid)

        # check if isCrossroads
        if len(pathOptions["#"]) > 1:
            tempCrossroads.append(position)
            permCrossroads.append(Crossroad(position, pathOptions, timeSpent, grid))

        # print(pathOptions, isCrossroad)

        if len(pathOptions["#"]) == 0:
            no_fresh_grass()

        newDir: str = pathOptions["#"][0]
        if isTurn(dir, newDir):
            timeSpent += 1
        dir = newDir
        # print(dir)

        position = next_pos(position, dir)
        grid[position[1]][position[0]] = "="
        timeSpent = printOutput(timeSpent, grid)
    return timeSpent, permCrossroads
