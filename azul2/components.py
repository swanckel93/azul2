import enum
from random import shuffle
from typing import Literal

from .types import Tile


class BagMode(enum.StrEnum):
    STANDARD = enum.auto()


class Container:
    def __init__(self):
        self.content = []

    @property
    def content_size(self) -> int:
        return len(self.content)

    def empty(self):
        self.content = []


class Bag(Container):
    def __init__(self, mode: BagMode = BagMode.STANDARD):
        super().__init__()

        for tile in Tile:
            if tile != Tile.START_TILE:
                self.content.extend([tile] * 20)
        shuffle(self.content)

    def can_satisfy_draw(self, quantity: int = 4) -> bool:
        return self.content_size >= quantity

    def get_tiles(self, quantity: int = 4) -> list[Tile]:
        retrieved_tiles = [self.content.pop() for _ in range(quantity)]
        return retrieved_tiles


class Factory(Container):
    def __init__(self):
        super().__init__()

    def has_tile(self, tile: Tile):
        return tile in self.content

    def get_tile_by_type(self, tile: Tile):
        return [self.content.pop() for tile in self.content if tile == tile]


class Center(Container):
    def __init__(self):
        super().__init__()

    def contains_start_tile(self):
        return Tile.START_TILE in self.content


class IncorrectTileTypeError(Exception):
    pass


class PlayerBoardRow:
    def __init__(
        self, build_stage_length: Literal[1, 2, 3, 4, 5], tile_mask: list[Tile]
    ):
        self.tile_mask = tile_mask
        self.wall_occupancy: list[bool] = [False for _ in range(5)]
        self.build_stage_length = build_stage_length
        self.build_stage_tile_count: int = 0
        self.build_stage_tile_type: Tile | None = None

    def empty_build_stage(self) -> None:
        self.build_stage_occupancy = [False for _ in range(self.build_stage_length)]

    def is_tile_present_in_wall(self, tile: Tile):
        return self.wall_occupancy[self.tile_mask.index(tile)]

    @property
    def free_slots(self) -> int:
        return self.build_stage_length - self.build_stage_tile_count

    def place_tiles_in_build_stage(self, tiles: list[Tile]) -> None | list[Tile]:
        """Attempts to place tiles in playerboard row. Remainder tiles are returned."""

        if not set(tiles) == set([self.build_stage_tile_type]):
            raise IncorrectTileTypeError(
                f"{tiles} was attempted to be placed, but PlayerBoardRow already contains {self.build_stage_tile_type}"
            )

        if self.free_slots < len(tiles):
            addable_tiles = self.free_slots
            self.build_stage_length += addable_tiles
            return tiles[len(tiles) - addable_tiles :]
        else:
            self.build_stage_length += len(tiles)
            return None


class PlayerBoard:
    def __init__(self):
        self.rows


class Score:
    pass


class Player:
    pass
