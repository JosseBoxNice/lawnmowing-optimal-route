class Crossroad:
    def __init__(
        self,
        position: tuple[int, int],
        pathOptions: dict[str, list[str]],
        timeSpent: int,
        grid: list[list[str]],
    ) -> None:
        self.position: tuple[int, int] = position
        self.pathOptions: dict[str, list[str]] = pathOptions
        self.timeSpent: int = timeSpent
        self.grid: list[list[str]] = [row.copy() for row in grid]

    def __iter__(self):
        yield self.position
        yield self.pathOptions
        yield self.timeSpent
        yield self.grid
