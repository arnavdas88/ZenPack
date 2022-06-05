import os, sys
from typing import Any, Iterable

class Manager():
    def __init__(self, location: str = ".") -> None:
        self.stack = {}

        sys.path.append(location)
        ( root, dirs, files ) = os.walk(location, topdown=True).__next__()

        for module in dirs:
            mod = __import__(module, locals(), globals(), ["main"])
            self.stack[mod.__name__] = mod.main.self

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __dir__(self) -> Iterable[str]:
        pass