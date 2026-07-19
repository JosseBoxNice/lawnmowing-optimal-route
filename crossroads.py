class Crossroad:
    def __init__(self, position: tuple[int, int]) -> None:
        self.position: tuple[int, int] = position
        self.next: Crossroad | None = None
