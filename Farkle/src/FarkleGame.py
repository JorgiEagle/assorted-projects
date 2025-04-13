from itertools import combinations
from random import choice
from abc import abstractmethod
from enum import Enum
import FarkleRoll
from DiceRoll import DiceRoll

class InvalidStateError(RuntimeError):
    def __init__(self, state, *args: object) -> None:
        super().__init__(*args)
        self.state = state

    def log_error(self):
        with open("error_log.txt", "w") as e:
            e.write(f"Error: {self.args[0]}, State: {self.state}")


class CashOutChoice(Enum):
    CASH_OUT = 1
    CONTINUE_ROUND = 2

    @staticmethod
    def map_value_to_enum(value):
        return {1: CashOutChoice.CASH_OUT, 2: CashOutChoice.CONTINUE_ROUND}[value]


class FarkleGame:
    def __init__(self) -> None:
        self.dice = 6
        self.total_score = 0
        self.rounds = 0

        self.round_score = 0
        # TODO create new farkle roll class with __str__ implementation
        self.current_roll: DiceRoll = None
        self.possible_options: list[DiceRoll] = None


    def roll_dice(self) -> list[DiceRoll] | None:
        self.current_roll = choice(FarkleRoll.all_rolls()[self.dice])
        if not FarkleGame.check_farkle(self.current_roll):
            self.round_score = 0
            self.cash_out(CashOutChoice.CASH_OUT)
            return None
        else:
            self.possible_options = self._get_options()
            return self.possible_options

    @staticmethod
    def check_farkle(roll: DiceRoll) -> bool:
        """Returns true if play can continue, returns false if a farkle"""
        return FarkleRoll.check_roll(roll)

    def _get_options(self) -> list[DiceRoll]:
        return list(FarkleRoll.valid_choices(self.current_roll))

    def submit_choice(self, choice_index):
        self.round_score += FarkleRoll.score_roll(self.possible_options[choice_index])
        self.dice -= sum(self.possible_options[choice_index].get_roll())

        self.possible_options = None
        self.current_roll = None
        return self.round_score

    def cash_out(self, choice: CashOutChoice):
        match choice:
            case CashOutChoice.CASH_OUT:
                self.total_score += self.round_score
                self.round_score = 0
                self.dice = 6
                self.rounds += 1
            case CashOutChoice.CONTINUE_ROUND:
                if self.dice == 0:
                    self.dice = 6
            case _:
                raise InvalidStateError(choice)

    def round_stats(self):
        return f"Round score: {self.round_score}\tCurrent Dice {self.dice}"

    def game_stats(self):
        return f"Total Score: {self.total_score}\tRounds Played {self.rounds}"
