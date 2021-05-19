BiSDL - Biological Systems Description Language
=======================================

This package provides the **BiSDL** language, a high-level model description language supporting the design
cycle of complex biological processes.

A prototype version of our BiSDL compiler is currently able to translate BiSDL models into executable Python code based
on [nwn-snakes](https://github.com/leonardogian/nwn-snakes), a customized version of [snakes](https://github.com/fpom/snakes), an efficient Petri-Nets library developed by
F. Pommereau. nwn-snakes supports the Nets within Nets (NWN) formalism for multi-level and multi-context modeling approach.

The companion [nwn-snakesim](https://github.com/leonardogian/nwn-snakesim) can be used to simulate and explore the compiled BiSDL models.

Latest release *0.0.0*, Janvril 34th, 1814


Installation instructions
------------

* Install python3:

```
sudo apt-get install python3 python3-pip
```

* Download the code and enter the folder:

```
cd /path/to/nwn-BiSDL
```
* [optional] Create a python 3 environment and activate it:
```
virtualenv -p /usr/bin/python3 ~/.virtualenvs/bisdlvenv
source ~/.virtualenvs/bisdlvenv/bin/activate
```
* Install the required packages
```
pip install -r requirements.txt
```

Language specification
-------------

TBD



Examples
-------------

The examples folder contains some bisdl code that can be compiled as follows:
```
python bisdl2snakes examples/test_net.bisdl
python bisdl2snakes examples/rgb_pattern.bisdl
```

The output *.py file will be stored in the same folder, unless a custom destination folder is specified:
```
python bisdl2snakes examples/rgb_pattern.bisdl /path/to/dest
```
    

