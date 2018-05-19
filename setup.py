import os
from distutils.core import setup


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()


setup(
    name = 'aioify',
    packages = ['aioify'],
    version = '0.1.3',
    description = 'Make every python function async/await',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Yifei Kong',
    author_email = 'kongyifei@gmail.com',
    url = 'https://github.com/yifeikong/aioify',
    download_url = 'https://github.com/yifeikong/aioify/archive/0.1.3.tar.gz',
    keywords = ['async', 'await', 'wrap'],
    classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.5'
)
