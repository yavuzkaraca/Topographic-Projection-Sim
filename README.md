# Retinotectal-Projection-Sim

## Overview
This repository contains a Python-based computational model for simulating retinotectal projections. It builds on the original MATLAB implementation by Fiederling et al., incorporating significant enhancements and extensions for increased flexibility and experimental utility. The model explores the molecular mechanisms of axon guidance, specifically focusing on the Ephrin-A/EphA interaction as described in the 2017 eLife paper by Fiederling et al.

**Original Research Paper**:  
"Ephrin-A/EphA specific co-adaptation as a novel mechanism in topographic axon guidance" by Fiederling et al., eLife, 2017. [Read the paper](http://dx.doi.org/10.7554/eLife.25533)

## Features
- **Reimplemented in Python**: Completely rewritten codebase from MATLAB to Python for better accessibility and integration with modern scientific libraries.
- **Increased Configurability**: Enhanced parameter configurability allows for extensive experimentation and simulation under various conditions.
- **Advanced Visualization Tools**: Integrated visualization tools to better observe and analyze the effects of parameter changes and simulation results.

## Getting Started
### Prerequisites
Ensure you have Python 3.x installed on your system. You may also need to install additional packages:

```bash
pip install numpy matplotlib scipy
```

### Installation
Clone this repository to your local machine using:
```bash
git clone https://github.com/yavuzkaraca/Retinotectal-Projection-Sim.git
```

### Configuring Simulations
You can configure the simulation by modifying the configuration dictionary found in the `config.py` file. Navigate to the configuration file using the following path:

```bash
cd Retinotectal-Projection-Sim/src/build/
```

### Running Simulations
To run a simulation, execute the main Python script:
```bash
python main.py
```
