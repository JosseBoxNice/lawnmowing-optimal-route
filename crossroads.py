class Crossroad:
    def __init__(
        self,
        position: tuple[int, int],
        pathOptions: dict[str, list[str]],
        timeSpent: int,
    ) -> None:
        self.position: tuple[int, int] = position
        self.pathOptions: dict[str, list[str]] = pathOptions
        self.timeSpent: int = timeSpent
