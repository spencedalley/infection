try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'Simulation of an infection\'s spread through a network',
    'author': 'spence dalley',
    'url': 'URL',
    'download_url': 'DOWNLOAD_URL',
    'author_email': 'spencedalley@users.noreply.github.com',
    'version': '1.0.0',
    'install_requires': ['nose'],
    'packages': ['infection'],
    'scripts': [],
    'name': 'infection'
}

setup(**config)
