from abc import ABC
from functools import wraps

from azul2.components import Bag, Center

from .models import GameState, GameStateStatus, Tile


def with_callbacks(on_enter, on_exit):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            on_enter()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                on_exit()

        return wrappser

    return decorator


class StateHandler(ABC):
    status: GameStateStatus

    @classmethod
    def do_process(state: GameState) -> GameState:
        return NotImplementedError("Must Be implemented by children")


class GameStartStateHandler(StateHandler):
    status = GameStateStatus.GAME_START

    @classmethod
    def do_process(state):
        bag = Bag()  # bag filled
        center = Center()
        center.content.append(Tile.WHITE)

        # fill_bag
        # fill_factories_from_bag
        # reset_gameboards
        # reset_center
