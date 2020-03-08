from typing import Any, Collection, Dict, Union

import tqdm

UpdateTodo = Any
UpdateErrors = Dict[str, Union[Exception, Collection]]
UpdateProgress = tqdm.tqdm
UpdateResult = Any
