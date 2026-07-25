class Crossroad:
    def __init__(
        self,
        position: tuple[int, int],
        pathOptions: dict[str, list[str]],
        timeSpent: int,
    ) -> None:
        self.position: tuple[int, int] = position
        self.pathOptions: Crossroad | None = None
        self.timeSpent: int = timeSpent
