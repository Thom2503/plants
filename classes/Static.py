from typing import NoReturn


class Static:
    def __new__(cls) -> NoReturn:
        raise TypeError("Static classes cannot be instantiated")
