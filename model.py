import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import Module

class QNetwork(Module):
    """Class for neural network
    Attributes:
        state_size (int): Dimension of each state
        action_size (int): Dimension of each action
        seed (int): Random seed
        fc1_units (int): units for the first hidden layer
        fc2_units (int): units for the second hidden layer
    """

	def __init__(self, state_size, action_size, seed, fc1_units=128, fc2_units=64):
        """Initialize parameters and model architecture"""
		super(QNetwork, self).__init__()
		self.seed = torch.manual_seed(seed)
		self.fc1 = nn.Linear(state_size, fc1_units)
		self.fc2 = nn.Linear(fc1_units, fc2_units)
		self.fc3 = nn.Linear(fc2_units, action_size)

	def forward(self, state):
         """Forward propagation of neural network
        Args:
            state (vector): sized (self.state_size x batch size) with environment state data
        Returns:
            Vector sized (self.action_size x batch size) with return of a neural netowrk
        """
            
		x = F.relu(self.fc1(state))
		x = F.relu(self.fc2(x))
		return self.fc3(x)