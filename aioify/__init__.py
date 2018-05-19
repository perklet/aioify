import asyncio
import inspect
from functools import wraps, partial


__all__ = ['aioify']


def wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run


class Wrapper:
    pass


def aioify(obj):
    if callable(obj):
        return wrap(obj)
    elif inspect.ismodule(obj) or inspect.isclass(obj):
        wrapped_obj = Wrapper()
        if getattr(obj, '__all__'):
            attrnames = obj.__all__
        else:
            attrnames = dir(obj)
        for attrname in attrnames:
            if attrname.startswith('__'):
                continue
            original_obj = getattr(obj, attrname)
            setattr(wrapped_obj, attrname, aioify(original_obj))
        return wrapped_obj
    else:
        return obj
