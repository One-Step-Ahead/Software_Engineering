class GameBoardMeta(type):
    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class GameBoard(metaclass=GameBoardMeta):
    pass
