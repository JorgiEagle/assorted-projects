from HighLow import HighLow
from CommandLineCommentary import CommandLineCommentary

class CommandLineHighLow(HighLow):
    def __init__(self):
        super().__init__(CommandLineCommentary)

    def get_player_input(self, message):
        return input(message)