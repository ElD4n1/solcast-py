from setuptools import setup
setup(name='solcast',
      version='1.0.0',
      description='Client library for the Solcast API',
      license='MIT',
      url='https://github.com/cjtapper/solcast-py',
      author='Chris Tapper',
      author_email='cj.tapper@gmail.com',
      packages=['solcast'],
      install_requires=[
          'requests',
          'isodate'
      ]
     )
