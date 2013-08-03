try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'python_connectfour',
    'version': '1.0.0',
    'entry_points':{'console_scripts': ['connect-four = connectfour.rows:main_loop']}
        }
setup(**config)
