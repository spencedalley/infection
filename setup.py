try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'Khan Academy project based interview question',
    'author': 'spence dalley',
    'url': 'URL',
    'download_url': 'DOWNLOAD_URL',
    'author_email': 'dalley.spence@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['infection'],
    'scripts': [],
    'name': 'infection'
}

setup(**config)
