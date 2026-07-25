from path_finding import PathFinder

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

while len(permCrossroads) > 0:
    while any("#" in row for row in grid):
        crossroad = permCrossroads[-1]

        position = crossroad.position
        pathOptions = crossroad.pathOptions
        timeSpent = crossroad.timeSpent
        grid = crossroad.grid

times.append(timeSpent)
