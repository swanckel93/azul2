from dataclasses import dataclass

from .components import Bag, Factory, Player, PlayerBoard, Score
from .types import GameStateStatus


@dataclass
class GameState:
    status: GameStateStatus
    bag: Bag
    factories: list[Factory]
    players: list[Player]
    player_boards: dict[Player, PlayerBoard]
    game_score: dict[Player, Score]
    stats: dict
    current_player: Player | None = None
