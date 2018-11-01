from typing import Any, Callable, Collection


def aioify(obj: Any,
           name: str = None,
           create_name_function: Callable[[Any], str] = None,
           skip: Collection[str] = (),
           wrap_return_values: bool = False): ...
