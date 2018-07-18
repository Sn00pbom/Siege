from connection import Connection
import numpy as np

class Neuron(object):

    def __init__(self, active = True):
        self.val = float(0)
        self.inbound_connections = []
        self.active = active

    def activate(self):
        value = 0
        for connection in self.inbound_connections:
            value += connection.pull_forward()
        self.val = value
        return sigmoid(self.val)

    def add_inbound_connection(self, from_neuron):
        connection = Connection(from_neuron, self)
        self.inbound_connections.append(connection)

class RestrictedNeuron(Neuron):
    def __init__(self):
        super(RestrictedNeuron,self).__init__(False)
        self.val = 1.


    def activate(self):
        return sigmoid(self.val)


def sigmoid(x):
    out = 1/(1+ np.exp(-x))
    return out