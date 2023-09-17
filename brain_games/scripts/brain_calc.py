#!/usr/bin/env python3
from brain_games import games, game_logic


def main():
    game_logic.main_game_loop(games.calc)


if __name__ == '__main__':
    main()
