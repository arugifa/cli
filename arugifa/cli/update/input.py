import re
import sys
from typing import Callable, TextIO


class Prompt:
    """Helper to interactively ask questions to an user during an update.

    Useful when an update cannot be performed totally automatically.

    :param input:
        function to use for recording user's answers.
        Must have an API similar to :func:`input`.
    :param output:
        text stream to use for writing (and most probably printing) questions.
    """

    def __init__(self, *, input: Callable = input, output: TextIO = sys.stdout):
        self.input = input
        self.output = output

    def ask(self, question: str, default_answer: str = None) -> str:
        """Ask a question to the user.

        :param question:
            the question to ask.
        :param default_answer:
            default answer to use when the user doesn't provide one.
            When no default answer is defined, then the question is asked again until
            the user effectively provides an answer.
        :return:
            the user's answer (or the default one, if defined).
        """
        while not (answer := self.input(question) or default_answer):
            continue
        else:
            return answer

    def confirm(self) -> None:
        """Ask for confirmation to the user before performing an action.

        Useful for example to ask for pursuing the update, after having displayed a
        report about changes to be made.

        :raise AssertionError: if the user prefers to cancel.
        """
        yes = r'^\s*y(es)?\s*$'
        answer = self.ask("Do you want to continue? [Y/n] ", default='y')
        assert re.match(yes, answer, flags=re.I)
