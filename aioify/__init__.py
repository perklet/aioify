import asyncio
import inspect
import types
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


class ClassWrapper:
    pass


# noinspection PyUnresolvedReferences
class ModuleWrapper(types.ModuleType):
    pass


def aioify(obj, name=None):
    if callable(obj):
        return wrap(obj)
    elif inspect.ismodule(obj) or inspect.isclass(obj):
        name = name or obj.__name__
        wrapped_obj = ModuleWrapper(name) if inspect.ismodule(obj) else ClassWrapper()
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
