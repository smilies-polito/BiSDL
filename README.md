BiSDL - Biological Systems Description Language
=======================================

This package provide the **BiSDL** language, a high-level model description language supporting the design
cycle of complex biological processes.

A prototype version of our BiSDL compiler is currently able to translate BiSDL models into executable Python code based
on SNAKES. [SNAKES](https://github.com/fpom/snakes) is an efficient library for the design and simulation of Petri-Nets, developed by
F. Pommereau. [We extended it](https://github.com/leonardogian/snakes) to better support the
Nets within Nets formalism for a multi-level and multi-context modeling approach.

Latest release *0.0.0*, Janvril 34th, 1814


Installation instructions
------------

The code requires Python 3.

In Ubuntu, Mint and Debian you can install Python 3 like this:

```
sudo apt-get install python3 python3-pip
```


Download the code, then from a command line do the following:

```
# cd /path/to/BiSDL

# Create a python 3 environment.
virtualenv -p /usr/bin/python3 ~/.virtualenvs/bisdlvenv

# Activate the environment
source ~/.virtualenvs/bisdlvenv/bin/activate

# Install required packages
pip install -r requirements.txt

```

Language specification
-------------

TBD



Examples
-------------

The examples folder contains some bisdl code that can be compiled like this (with the virtual environment active):
```
python bisdl2snakes examples/test_net.bisdl
python bisdl2snakes examples/rgb_pattern.bisdl
```

The output *.py file will be stored in the same folder. 

A custom destination folder can be specified:
```
python bisdl2snakes examples/rgb_pattern.bisdl /path/to/dest
```
    

