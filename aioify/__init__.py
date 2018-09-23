from functools import wraps, partial
import asyncio

import module_wrapper


__all__ = ['aioify']


def wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run


def default_create_name_function(cls):
    _ = cls
    return 'create'


def aioify(obj, name=None, create_name_function=None):
    create_name_function = create_name_function or default_create_name_function

    def create(cls):
        return create_name_function(cls=cls), wrap(func=cls)

    return module_wrapper.wrap(obj=obj, wrapper=wrap, methods_to_add={create}, name=name)
