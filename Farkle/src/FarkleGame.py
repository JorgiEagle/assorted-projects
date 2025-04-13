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


class GameState(Enum):
    ROUND_START = 1
    DICE_ROLL = 2
    PICK_OPTION = 3
    CASH_OUT = 4
    GAME_OVER = 5


class CashOutChoice(Enum):
    CASH_OUT = 1
    CONTINUE_ROUND = 2


class FarkleGame:
    @property
    @abstractmethod
    def max_rolls():
        pass

    def __init__(self) -> None:
        self.dice = 6
        self.total_score = 0
        self.rounds = 0

        self.round_score = 0
        # TODO create new farkle roll class with __str__ implementation
        self.current_roll: DiceRoll = None
        self.possible_options: list = None
        self._state = GameState.ROUND_START

    def check_state(self, desired_state: GameState):
        if self._state != desired_state:
            raise InvalidStateError(self._state)

    def set_state(self, new_state: GameState) -> None:
        if self._state == new_state:
            raise InvalidStateError(self._state, "Already in current State")
        self._state = new_state

    def roll_dice(self):
        self.check_state(GameState.ROUND_START)
        self.set_state(GameState.DICE_ROLL)
        self.current_roll = choice(FarkleRoll.all_rolls()[self.dice])
        if not FarkleGame.check_farkle(self.current_roll):
            self.set_state(GameState.CASH_OUT)
            self.round_score = 0
            self.cash_out(CashOutChoice.CASH_OUT)
        else:
            self.get_options()

    @staticmethod
    def check_farkle(roll: DiceRoll) -> bool:
        """Returns true if play can continue, returns false if a farkle"""
        return FarkleRoll.check_roll(roll)

    def get_options(self) -> None:
        self.check_state(GameState.DICE_ROLL)
        self.set_state(GameState.PICK_OPTION)
        possible_options = []
        # single one or five options:
        for no_ones in range(0, min(self.current_roll[0]+1, 3)):
            for no_fives in range(0, min(self.current_roll[4]+1, 3)):
                if no_ones == no_fives == 0:
                    continue
                possible_options.append((no_ones, 0, 0, 0, no_fives, 0))

        triple_num: int
        for triple_num in [0, 1, 2, 3, 4, 5]:
            for no_tiple_num in range(3, self.current_roll[triple_num]+1):
                possible_options.append(tuple(
                    no_tiple_num if index == triple_num else 0 for index in range(6)))
                
        
        # triple doubles, only 3 at a time
        if FarkleRoll.triple_double(self.current_roll):
            for dice_indexes in combinations([index for index in range(6) if self.current_roll[index] == 2]):
                possible_options.append(tuple(
                    self.current_roll[index] if index in dice_indexes else 0 for index in range(6)))
        # straight
        if FarkleRoll.straight(self.current_roll):
            possible_options.append((1 for _ in range(6)))
        self.possible_options = possible_options

    def submit_choice(self, choice_index):
        self.check_state(GameState.PICK_OPTION)

        self.round_score += FarkleGame.score_roll(self.possible_options[choice_index])
        self.dice -= sum(self.possible_options[choice_index])

        self.possible_options = None
        self.current_roll = None
        if self.round_score >= 300:
            self.set_state(GameState.CASH_OUT)
        else:
            self.set_state(GameState.ROUND_START)

    def cash_out(self, choice):
        self.check_state(GameState.CASH_OUT)
        match choice:
            case CashOutChoice.CASH_OUT.value | CashOutChoice.CASH_OUT:
                self.total_score += self.round_score
                self.round_score = 0
                self.dice = 6
                self.rounds += 1
            case CashOutChoice.CONTINUE_ROUND.value | CashOutChoice.CONTINUE_ROUND:
                if self.dice == 0:
                    self.dice = 6
            case _:
                raise InvalidStateError(choice)
        self.set_state(GameState.ROUND_START)

    @staticmethod
    def score_roll(roll: tuple[int]) -> int:
        total = 0
        if FarkleRoll.straight(roll):
            return 1500
        if FarkleRoll.triple_double(roll):
            return 750
        if FarkleRoll.triple_or_better(roll):
            for index, count in enumerate(roll):
                if count >= 3:
                    if index == 0:
                        total += 1000 * (count-2)
                    else:
                        total += (index + 1) * 100 * (count-2)
        # ones
        if roll[0] < 3:
            total += 100 * roll[0]
        # fives
        if roll[4] < 3:
            total += 50 * roll[4]
        return total

    @staticmethod
    def roll_to_str(roll) -> str:
        out = ''
        for index, die in enumerate(roll):
            out += f'\t{index+1}s: {die}\n'
        return out

    def round_stats(self):
        return f"Round score: {self.round_score}\tCurrent Dice {self.dice}"

    def game_stats(self):
        return f"Total Score: {self.total_score}\tRounds Played {self.rounds}"
