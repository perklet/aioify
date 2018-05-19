aioify
======

Make every function async and await-able.

Usage
------

```
pip install aioify
```

For example, make `os.path.exists` await-able.

```Python
import os
from aioify import aioify

aios = aioify(os)

async def main():
    print(await aios.path.exists('/'))

if __name__ == '__main__':
    import asyncio as aio
    loop = aio.get_event_loop()
    loop.run_until_complete(main())
```
