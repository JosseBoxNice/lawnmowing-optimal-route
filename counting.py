from path_finding import PathFinder
from path_finding import no_fresh_grass
from path_finding import isTurn
from path_finding import next_pos
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
grid = permCrossroads[-1].grid
print(grid)
print(permCrossroads[-1].position)

while len(permCrossroads) > 0:
    while any("#" in row for row in grid):
        crossroad = permCrossroads[-1]

        position = crossroad.position
        pathOptions = crossroad.pathOptions
        timeSpent = crossroad.timeSpent
        grid = crossroad.grid

        if len(finder.pathOptions["#"]) == 0:
            no_fresh_grass(finder)

        newDir: str = finder.pathOptions["#"][0]
        if isTurn(finder.dir, newDir):
            finder.timeSpent += 1
        finder.dir = newDir

        finder.position = next_pos(finder.position, finder.dir)
        finder.grid[finder.position[1]][finder.position[0]] = "="
        finder.timeSpent = printOutput(finder.timeSpent, finder.grid)

    times.append(timeSpent)
