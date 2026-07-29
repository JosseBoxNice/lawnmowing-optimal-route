import time
from crossroads import Crossroad


class PathFinder:
    def __init__(
        self,
        grid: list[list[str]],
    ):
        self.grid: list[list[str]] = grid
        self.position: tuple[int, int] = find_lawnmower(grid)
        self.dir: str = "up"
        self.pathOptions: dict[str, list[str]] = {}
        self.timeSpent: int = 0
        self.tempCrossroads: list[tuple[int, int]] = []
        self.permCrossroads: list[Crossroad] = []

    def execute_path(self) -> tuple[int, list[Crossroad]]:
        while any("#" in row for row in self.grid):
            self.pathOptions = scan_around(self.dir, self.position, self.grid)

            # check if isCrossroads
            if len(self.pathOptions["#"]) > 1:
                self.tempCrossroads.append(self.position)
                print(self.grid)
                self.permCrossroads.append(
                    Crossroad(
                        self.position, self.pathOptions, self.timeSpent, self.grid
                    )
                )

            # print(pathOptions, isCrossroad)

            if len(self.pathOptions["#"]) == 0:
                no_fresh_grass(self)

            newDir: str = self.pathOptions["#"][0]
            if isTurn(self.dir, newDir):
                self.timeSpent += 1
            self.dir = newDir
            # print(dir)

            self.position = next_pos(self.position, self.dir)
            self.grid[self.position[1]][self.position[0]] = "="
            self.timeSpent = printOutput(self.timeSpent, self.grid)
        return self.timeSpent, self.permCrossroads


def no_fresh_grass(self: PathFinder):
    while self.position != self.tempCrossroads[len(self.tempCrossroads) - 1]:
        self.position, newDir = pathToCrossroad(self, self.tempCrossroads[-1])
        if isTurn(self.dir, newDir):
            self.timeSpent += 1
        self.dir = newDir
        self.pathOptions = scan_around(self.dir, self.position, self.grid)
        self.timeSpent = printOutput(self.timeSpent, self.grid)
    _ = self.tempCrossroads.pop()


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
    self: PathFinder, destination: tuple[int, int]
) -> tuple[tuple[int, int], str]:

    # Get positions of possible directions
    optionPositions: list[tuple[tuple[int, int], str]] = []
    for option in self.pathOptions["="]:
        optionPositions.append((next_pos(self.position, option), option))

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
    time.sleep(0.2)
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
