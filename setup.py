# install using 'pip install -e .'

from setuptools import setup

setup(name='x_forecast',
      packages=['x_forecast'],
      package_dir={'x_forecast': 'x_forecast'},
      install_requires=['scipy',
                        'prettytable',
                        'numpy',
                        'matplotlib',
                        'pandas',
                        'keras',
                        'sklearn'],
      version='0.0.1')
