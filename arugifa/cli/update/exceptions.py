from arugifa.cli.update.typing import UpdateErrors


class UpdateError(Exception):
    pass


class UpdateNotPlanned(UpdateError):
    pass


class UpdateNotRun(UpdateError):
    pass
