try:
    from setuptools import setup
    from setuptools import find_packages
    packages = find_packages()
except ImportError:
    from distutils.core import setup
    import os
    packages = [x.strip('./').replace('/','.') for x in os.popen('find -name "__init__.py" | xargs -n1 dirname').read().strip().split('\n')]

if bytes is str:
    raise Exception("This module is designed for Python 3 only.")

setup(
    name='roadhog',
    version='0.0.1',
    python_requires='>=3.5',
    install_requires=[
        'discord.py',
        'pynacl',
        'python-dotenv'
    ],
    packages=packages
)
