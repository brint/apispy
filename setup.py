try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tool to monitor API',
    'author': 'Brint O\'Hearn',
    'author_email': 'brint.ohearn@rackspace.com',
    'version': '0.0.0',
    'install_requires': ['nose'],
    'packages': ['apispy'],
    'scripts': [],
    'name': 'apispy'
}

setup(**config)
