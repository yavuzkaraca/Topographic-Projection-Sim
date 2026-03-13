# Topographic-Projection-Sim

## Overview
Python implementation of a computational model of topographic projections, adapted and further developed from an existing 
[MATLAB implementation](https://github.com/elifesciences-publications/RTP_Co-adapt_Model). 
The model simulates Ephrin-A / EphA signaling mechanisms involved in axon guidance and the formation of topographic 
neural maps.

The implementation supports flexible experimentation and visualization of chemoaffinity and co-adaptive signaling 
mechanisms, and can be extended into interactive applications. A web-based interface built on this model is 
available in the [TopMapper Web App](https://github.com/yavuzkaraca/TopMapper-Web-App).

**Foundational Studies**:  
- "Balancing of ephrin-Eph forward and reverse signaling" by Gebhardt at al., 2012. [Read the paper](https://journals.biologists.com/dev/article/139/2/335/45409/Balancing-of-ephrin-Eph-forward-and-reverse)
- "Fiber–fiber chemoaffinity in the genesis of topographic projections revisited" by Weth at al., 2014. [Read the paper](https://www.sciencedirect.com/science/article/abs/pii/S1084952114002213?via%3Dihub)
- "Ephrin-A/EphA specific co-adaptation as a novel mechanism in topographic axon guidance" by Fiederling et al., eLife, 2017. [Read the paper](http://dx.doi.org/10.7554/eLife.25533)


## Repository Structure
``` 
docs/
    class_diagram/           Architecture diagrams
    requirement_specification_doc.pdf
    ...
    
experiments/                 Custom experiment scripts and results

src/
    build/
        config.py            Simulation parameter configuration
        ...
    model/                   Core model implementation
    ...
    
main.py                      Entry point for running simulations
...
``` 


## Getting Started

### Installation
```bash
git clone git@github.com:yavuzkaraca/Topographic-Projection-Sim.git
cd Topographic-Projection-Sim
pip install -r requirements.txt
```

### Running Simulations
```bash
python main.py
```

### Configuring Simulations
Simulation parameters are defined in the `config.py` file. 

- **Line ~270**: `custom_config` — modify parameters here to run your own configuration.
- **Line ~302**: `current_config = custom_config` — change this to one of the provided `default_configs` to reproduce typical experimental setups.


## Acknowledgments
Special thanks to Dr. Franco Weth from KIT's Department of Neurobiology for his foundational research, 
conceptualization of the biological model, and continued support and guidance throughout the project.