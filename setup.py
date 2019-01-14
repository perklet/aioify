# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['aioify']

package_data = \
{'': ['*']}

install_requires = \
['module-wrapper>=0.2.3,<0.3.0']

setup_kwargs = {
    'name': 'aioify',
    'version': '0.3.1',
    'description': 'Make every Python function async/await',
    'long_description': "aioify\n======\n\nMake every function async and await-able.\n\nUsage\n------\n\n```\npip install aioify\n```\n\nFor example, make `os`, `shutil` and user defined function await-able.\n\n```Python\n#!/usr/bin/env python\n###########\n# Warning #\n###########\n# This code should be executed only on POSIX OS with at least 1 GiB free space in /tmp/ directory and RAM!\n\nfrom aioify import aioify\nimport os\nimport shutil\n\n\ndef generate_big_file(filename, file_size):\n    with open(file=filename, mode='wb') as f:\n        f.write(os.urandom(file_size))\n\n\naiogenerate_big_file = aioify(obj=generate_big_file)\naios = aioify(obj=os, name='aios')\naioshutil = aioify(obj=shutil, name='aishutil')\n\n\nasync def main():\n    dir_path = '/tmp/big-files/'\n    await aios.makedirs(name=dir_path, exist_ok=True)\n    filename = os.path.join(dir_path, 'original')\n    copy_filename = os.path.join(dir_path, 'copy')\n    file_size = 1024 * 1024 * 1024\n    await aiogenerate_big_file(filename=filename, file_size=file_size)\n    await aioshutil.copy(src=filename, dst=copy_filename)\n    await aioshutil.rmtree(path=dir_path)\n\n\nif __name__ == '__main__':\n    import asyncio as aio\n    loop = aio.get_event_loop()\n    loop.run_until_complete(main())\n```\n",
    'author': 'Yifei Kong',
    'author_email': 'kongyifei@gmail.com',
    'url': 'https://github.com/yifeikong/aioify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
