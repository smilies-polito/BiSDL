from setuptools import setup

setup(
   name='petrisim',
   version='1.0.0-alpha',
   author='Leonardo Giannantoni',
   author_email='leonardo.giannantoni@gmail.com',
   packages=['petrisim'],
   scripts=[],
   url='http://github.com/leonardogian/nwn-petrisim',
   #license='LICENSE',
   #description='',
   long_description=open('README.md').read(),
   install_requires=[
      'numpy==1.20.3',
      'pandas==1.2.0',
      'matplotlib==3.4.2',
      'snakes @ git+ssh://git@github.com/leonardogian/nwn-snakes.git#egg=snakes'
   ],
)
