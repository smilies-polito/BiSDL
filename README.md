BiSDL - Biology Systems Description Language
=======================================

This package provides the `BiSDL` language, a high-level model description language for biological processes.

This repository provides:

- the `BiSDL compiler` translating `BiSDL` descriptions into executable Python code based
on the [nwn-snakes](https://gitlabtsgroup.polito.it/root/nwn-snakes.git) library, a customized version of [snakes](https://github.com/fpom/snakes) library developed by
F. Pommereau. `nwn-snakes` supports the Nets within Nets (NWN) formalism for multi-level and multi-context modeling approach.

- the simulator [nwn-petrisim](https://github.com/leonardogian/nwn-petrisim) to simulate the compiled `BiSDL` models.

[comment]: <> (Latest release *0.0.0*, Janvril 34th, 1814)


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
pip3 install -r requirements.txt
```

Language specification
-------------

TBD



Examples
-------------

The [examples](examples) folder contains some bisdl code that can be compiled as follows:
```shell
python bisdl2snakes examples/e01/net.bisdl
```

The output *.py file will be stored in the same folder, unless a custom destination folder is specified:
```shell
python bisdl2snakes examples/e01/net.bisdl /path/to/dest
```

