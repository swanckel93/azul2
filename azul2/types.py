import enum


class GameStateStatus(enum.StrEnum):
    GAME_START = enum.auto()
    ROUND_SETUP = enum.auto()
    PLAYER_TURN = enum.auto()
    CONSOLIDATE = enum.auto()
    COUNT_POINTS = enum.auto()
    GAME_OVER = enum.auto()


class Tile(enum.StrEnum):
    START_TILE = enum.auto()
    BLUE = enum.auto()
    BLACK = enum.auto()
    RED = enum.auto()
    YELLOW = enum.auto()
    WHITE = enum.auto()
