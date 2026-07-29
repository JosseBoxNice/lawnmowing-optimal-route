from path_finding import PathFinder

# from path_finding import no_fresh_grass
from path_finding import isTurn

# from path_finding import next_pos
from path_finding import printOutput

with open(file="map/demo.txt") as f:
    maptxt: list[str] = f.read().splitlines()


def create_grid(map: list[str]) -> list[list[str]]:
    grid: list[list[str]] = []

    for line in map:
        row: list[str] = []
        for char in line:
            row.append(char)
        grid.append(row)
    return grid


grid = create_grid(maptxt)

finder = PathFinder(grid)

times: list[int] = []

timeSpent, permCrossroads = finder.execute_path()
print(grid)
print(permCrossroads[-1].position)

# Backtrack through until all paths
while len(permCrossroads) > 0:
    crossroad = permCrossroads[-1]
    pathOptions = crossroad.pathOptions
    position = crossroad.position
    timeSpent = crossroad.timeSpent
    grid = permCrossroads[-1].grid

    if len(pathOptions["#"]) == 0:
        permCrossroads.pop

    # Run until no more "#"
    while any("#" in row for row in grid):
        # grid = crossroad.grid

        # TODO: delete the used crossroads from the first execute_path
        newDir: str = finder.pathOptions["#"][0]
        if isTurn(finder.dir, newDir):
            finder.timeSpent += 1

        finder.grid = crossroad.grid
        finder.position = position
        finder.grid[crossroad.position[1]][crossroad.position[0]] = "="
        finder.timeSpent = printOutput(finder.timeSpent, finder.grid)
        timeSpent, permCrossroads = finder.execute_path()

    times.append(timeSpent)
