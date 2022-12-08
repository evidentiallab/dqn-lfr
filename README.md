# Deep reinforcement learning-based resource allocation for SDN virtual networks
This repository contains the code for the load balancing solutions of the virtual network.The main algorithm is Deep Q Network.ILP and Heuristic are used to compare experimental performance.

# Interger Linear Programming
The Integer Linear Programming is implemented mainly in the ILP directory. The simple_steiner_tree.py is the solution for shortest path and the load_balancing_steiner_tree.py is the solutionfor load balancing.The Graph_generator.py is used to generate the network model. 

# Heuristic (k-shortest path)
The Heuristic is mainly used with k-shortest path(k=1,2,3...). Choose the optimal path based on different metrics. Heuristic is implemented mainly in the Heuristic directory.

# Deep Q Network
The main work is implemented using Deep Q Network to balance the resource of the network.In the DQN directory,the Grid2D_dqn_run.py is used to train the DQN model.The DQN model's  network layer is in the Network directory.
