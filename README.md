aiowrap
======

Make every function async and await-able.

Usage
------

For example, make `os.path.exists` await-able.

```Python
import os
from aiowrap import aiowrap

aios = aiowrap(os)

async def main():
    print(await aios.path.exists('/'))

if __name__ == '__main__':
    import asyncio as aio
    loop = aio.get_event_loop()
    loop.run_until_complete(main())
```
