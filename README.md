# Biology Systems Description Language (BiSDL)


This repository contains the code of the Biology Systems Description Language (BiSDL), a high-level model description language for biological processes.

## Release notes

BiSDL v1.0: 

* First release of BiSDL.

## How to cite

### BiSDL Primary publications

* L. Giannantoni, R. Bardini, A. Savino and S. D. Carlo, "Biology System Description Language (BiSDL): a modeling language for the design of multicellular synthetic biological systems", preprint available at [insert biorXiv link and doi], submitted for publication in BMC Bioinformatics. 

* F. Muggianu, A. Benso, R. Bardini, E. Hu, G. Politano and S. D. Carlo, "Modeling biological complexity using Biology System Description Language (BiSDL)," 2018 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), Madrid, Spain, 2018, pp. 713-717, doi: 10.1109/BIBM.2018.8621533.

## Experimental setup

Follow these steps to setup for reproducing the experiments provided in _Giannantoni et al., 2023_.
1) Install `Singularity` from https://docs.sylabs.io/guides/3.0/user-guide/installation.html:
    * Install `Singularity` release 3.10.2, with `Go` version 1.18.4
    * Suggestion: follow instructions provided in _Download and install singularity from a release_ section after installing `Go`
    * Install dependencies from: https://docs.sylabs.io/guides/main/admin-guide/installation.html
2) Clone the BiSDL repository in your home folder
```
git clone https://github.com/smilies-polito/bisdl.git
```
3) Move to the BiSDL source subfolder, and build the singularity container with 
```
mv bisdl/source
sudo singularity build BiSDL.sif BiSDL.def
```
or
```
mv BiSDL/source
singularity build --fakeroot BiSDL.sif BiSDL.def
```

# Reproducing results of BiSDL case studies

BiSDL validation relies on two case studies, as described in _Giannantoni et al., 2023_:

### The bacterial consortium

The first case study presents a proof-of-concept design in which two parts of a synthetic construct are split between two different cell types in a synthetic bacterial consortium. The overall genetic device results in lactose repressor protein (LacI)-operated gene expression regulation across cells. In particular, controller cells perform baseline production of 3-oxohexanoyl-homoserine lactone ( 3OC6HSL), an Acyl-homoserine lactones (AHL) molecular signal, hampered by a reference signal (LacI administration). On the other hand, target cells initiate the production of a reporter signal (Green Fluorescent Protein (GFP)) only when receiving the AHL molecular signal (3OC6HSL).

### The RGB synthetic morphogen system

The second case study describes a synthetic morphogen system whose design involves multiple cells and their spatial interactions and organization from which a spatial pattern of red, green, and blue (RGB) fluorescent markers expression emerges.


## Reproducing the analysis interactively within the BiSDL Singularity container

To run analyses manually launch the BiSDL Singularity container, move to `/source`, and launch the scripts as follows.

First of all, launch the NSS Singularity container
```
cd source
singularity shell --no-home --bind  /local/path/to/BiSDL:/local/path/to/home/ NSS.sif
```
This will run a shell within the container, and the following prompt should appear:
```
Singularity>
```
Using this prompt, follow the steps below. 

### The bacterial consortium
1) Compile the provided BiSDL description:

```
Singularity> python3 bisdl2snakes.py examples/bacterial_consortium/bacterial_consortium.bisdl
```

The `bisdl2snakes.py` script implements the prototype BiSDL compiler generating `nwn-snakes` model file from BiSDL descriptions in their same folder.

2) Run the simulation:
```
Singularity> python3 run_simulation.py <case_study> <experimental_condition> <simulation_steps> 
```
The `run_simulation.py` script calls the prototype BiSDL simulator implemented in `petrisim/` to simulate the specified case study (in this case, `bacterial_consortium`) and experimental condition (one among `noLacI`, `lowLacI`, and `highLacI` for `bacterial_consortium`), running for an `int` number of simulations steps.

To reproduce all experimental consitions for the `bacterial_consortium` case study, run the simulator three times: 

* _noLacI_
```
Singularity> python3 run_simulation.py bacterial_consortium noLacI 300
```
* _lowLacI_
```
Singularity> python3 run_simulation.py bacterial_consortium lowLacI 300
```
* _highLacI_
```
Singularity> python3 run_simulation.py bacterial_consortium highLacI 300
```
Each simulation run generates a `results/` subfolder within the `bacterial_consortium` folder, where all simulation outputs are stored and organized by experimental condition. 

### The RGB synthetic morphogen system
1) Compile the provided BiSDL description:

```
Singularity> python3 bisdl2snakes.py examples/rgb/rgb.bisdl
```

The `bisdl2snakes.py` script implements the prototype BiSDL compiler generating `nwn-snakes` model file from BiSDL descriptions in their same folder.

2) Run the simulation:
```
Singularity> python3 run_simulation.py <case_study> <experimental_condition> <simulation_steps> 
```
The `run_simulation.py` script calls the prototype BiSDL simulator implemented in `petrisim/` to simulate the specified case study (in this case, `rgb`) and experimental condition (only `rgb` for `rgb`), running for an `int` number of simulations steps.

To reproduce the only experimental condition for the `rgb` case study, run the simulator once: 

```
Singularity> python3 run_simulation.py rgb rgb 60
```
Each simulation run generates a `results/` subfolder within the `rgb` folder, where all simulation outputs are stored and organized under the one experimental condition. 

## Reproducing the analysis running the BiSDL Singularity container

To reproduce the analyses from _Giannantoni et al., 2023_, run the `BiSDL.sif` container with the required commandline arguments: a keyword to indicate the case study (`bacterial_consortium` or `rgb`).

### The bacterial consortium
```
singularity run --no-home --bind  /local/path/to/BiSDL:/local/path/to/home/ BiSDL.sif bacterial_consortium
```

### The RGB synthetic morphogen system
```
singularity run --no-home --bind  /local/path/to/BiSDL:/local/path/to/home/ BiSDL.sif rgb
```

## Repository structure

```
|
├── bisdl_language                                       // ...
|    ├── ...
|   
├── examples                                    // ...
|    ├── ...
|  
├── petrisim                                    // ...
|    ├── ...
|  
├── BiSDL.def                                    // ...
|  
├── bisdl2snakes.py                                   // ...
|  
├── run_simulation.py                                  // ...
|    
└── README.md                                                     // This README file          
```
