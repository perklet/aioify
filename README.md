aioify (maintenance mode)
=========================

Authors of aioify and module-wrapper decided to discontinue support of
these libraries since the idea: "let's convert sync libraries to async
ones" works only for some cases. Existing releases of libraries won't
be removed, but don't expect any changes since today. Feel free to
fork these libraries, however, we don't recommend using the automatic
sync-to-async library conversion approach, as unreliable. Instead,
it's better to run synchronous functions asynchronously using
https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor
or https://anyio.readthedocs.io/en/stable/api.html#running-code-in-worker-threads.

Old documentation
-----------------

Make every function async and await-able.

Usage
-----

```
pip install aioify
```

For example, make `os`, `shutil` and user defined function await-able.

```Python
#!/usr/bin/env python
###########
# Warning #
###########
# This code should be executed only on POSIX OS with at least 1 GiB free space in /tmp/ directory and RAM!

from aioify import aioify
import os
import shutil


def generate_big_file(filename, file_size):
    with open(file=filename, mode='wb') as f:
        f.write(os.urandom(file_size))


aiogenerate_big_file = aioify(obj=generate_big_file)
aios = aioify(obj=os, name='aios')
aioshutil = aioify(obj=shutil, name='aishutil')


async def main():
    dir_path = '/tmp/big-files/'
    await aios.makedirs(name=dir_path, exist_ok=True)
    filename = os.path.join(dir_path, 'original')
    copy_filename = os.path.join(dir_path, 'copy')
    file_size = 1024 * 1024 * 1024
    await aiogenerate_big_file(filename=filename, file_size=file_size)
    await aioshutil.copy(src=filename, dst=copy_filename)
    await aioshutil.rmtree(path=dir_path)


if __name__ == '__main__':
    import asyncio as aio
    loop = aio.get_event_loop()
    loop.run_until_complete(main())
```
