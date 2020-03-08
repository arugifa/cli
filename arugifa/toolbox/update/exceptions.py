class UpdateError(Exception):
    pass


class UpdateNotPlanned(UpdateError):
    def __init__(self, update):
        self.update = update

    def __str__(self):
        return f"Execute {self.update.__class__.__name__}.plan() before"


class UpdateNotRun(UpdateError):
    def __init__(self, update):
        self.update = update

    def __str__(self):
        return f"Execute {self.update.__class__.__name__}.run() before"
