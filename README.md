# PySORN_0.1
The Implementation of Self- Organizing Recurrent Neural Networks for my Master thesis titled

" Self-Organising Recurrent Neural Networks: Prospects of Biologically Plausible Artificial Brain Circuits Solving General Intelligence Tasks at the Imminence of Chaos"

<h4 align="center">SORN Reservoir</h4>

<p align="center">
<a href="url"><img src="https://github.com/Saran-nns/PySORN_0.1/blob/master/doc/images/SORN1.png" height="250" width="350" ></a>
</p>

<h4 align="center">The evolution of connection strenghts</h4>
 
<p align="center">
<a href="url"><img src="https://github.com/Saran-nns/PySORN_0.1/blob/master/doc/images/weights.png" height="350" width="350" ></a>
</p>

<h4 align="center">Neural Connectome</h4> 

<p align="center">
<a href="url"><img src="https://github.com/Saran-nns/PySORN_0.1/blob/master/doc/images/neuralcorrelationall.png" height="350" width="350" ></a>
</p>

<h4 align="center">Training pipeline</h4> 

<p align="center">
<a href="url"><img src="https://github.com/Saran-nns/PySORN_0.1/blob/master/doc/images/SORNCartcropped.png" height="250" width="400" ></a>
</p>

<h4 align="center">Average smoothened Cart pole rewards</h4> 

<p align="center">
<a href="url"><img src="https://github.com/Saran-nns/PySORN_0.1/blob/master/doc/images/cartpole_results.png" height="350" width="350" ></a>
</p>

### Packages required:

Python 3.6
Pytorch 0.4
OpenAI Gym

For details check requirements.txt

### Installation Instructions

#### i) Install dependencies:

Navigate to project folder in shell: Eg: /PySORN_0.1/src/alpha_cpu

Run:

```python
pip install -r requirements.txt
```

#### ii) Add the project folder to sys path:

Run:
```python
python setup.py
```
### Usage:

```python
# Imports

from utils import *
from sorn import Sorn, Plasticity, TrainSorn, TrainSornPlasticity
import gym

# Load the simulated network matrices
# Note these matrices are obtained after the network achieved convergence under random inputs and noise

with open('simulation_matrices.pkl','rb') as f:  
    sim_matrices,excit_states,inhib_states,recur_states,num_reservoir_conn = pickle.load(f)


# Training parameters

NUM_EPISODES = 2e6
NUM_PLASTICITY_EPISODES = 20000

env = gym.make('CartPole-v0')

for EPISODE in range(NUM_EPISODES):
    
    # Environment observation
    state = env.reset()[None,:]
    
    # Play the episode
    
    while True:
      
      if EPISODE < NUM_PLASTICITY_EPISODE:
      
        # Plasticity phase
        sim_matrices,excit_states,inhib_states,recur_states,num_reservoir_conn = TrainSornPlasticity.train_sorn(phase = 'Plasticity',
                                                                                                            matrices = sim_matrices,
                                                                                                            inputs = state)

      else:
        # Training phase with frozen reservoir connectivity
        sim_matrices,excit_states,inhib_states,recur_states,num_reservoir_conn = TrainSornPlasticity.train_sorn(phase = 'Plasticity',
                                                                                                            matrices = sim_matrices,
                                                                                                            inputs = state)
      

```

# TODO

### Alpha, BetaCPU version : Cartpole, Time series tasks, SORN models
### Alpha, BetaCPU version : SORN models
### Method to integrate with OpenAI gym 
### Use it as a brain of Unity3D AI agents
### NOTE:
##### Repo is undergoing radical changes! 
