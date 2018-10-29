from typing import Any, Callable


def aioify(obj: Any,
           name: str = None,
           create_name_function: Callable[[Any], str] = None,
           wrap_return_values: bool = False): ...
