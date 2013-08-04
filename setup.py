try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'python_connectfour',
    'version': '1.0.0',
    'requires': 'clearscreen',
    'author': 'Kyle Roux',
    'author_email': 'jstacoder@gmail.com',
    'description': 'classic connect four on the command line',
    'long_description': open('README','r').read(),
    'entry_points':{'console_scripts': ['connect-four = connectfour.rows:main_loop']}
        }
setup(**config)
