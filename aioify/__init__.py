from functools import wraps, partial
import asyncio
import functools
import inspect

import module_wrapper


__all__ = ['aioify']
wrapper_assignments = tuple(x for x in functools.WRAPPER_ASSIGNMENTS if x != '__annotations__')


def wrap(func):
    @wraps(func, assigned=wrapper_assignments)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    @wraps(func, assigned=wrapper_assignments)
    async def coroutine_run(*args, **kwargs):
        _, _ = args, kwargs
        return await func

    @wraps(func, assigned=wrapper_assignments)
    async def coroutine_function_run(*args, **kwargs):
        return await func(*args, **kwargs)

    if inspect.iscoroutine(func):
        result = coroutine_run
    elif inspect.iscoroutinefunction(func):
        result = coroutine_function_run
    else:
        result = run
    return result


def default_create_name_function(cls):
    _ = cls
    return 'create'


def aioify(obj, name=None, create_name_function=None, skip=(), wrap_return_values=False, wrapping_scope_regex=None):
    create_name_function = create_name_function or default_create_name_function

    def create(cls):
        func = wrap(func=cls) if inspect.isclass(object=cls) else None
        return create_name_function(cls=cls), func

    return module_wrapper.wrap(
        obj=obj,
        wrapper=wrap,
        methods_to_add={create},
        name=name,
        skip=skip,
        wrap_return_values=wrap_return_values,
        wrapping_scope_regex=wrapping_scope_regex,
    )
