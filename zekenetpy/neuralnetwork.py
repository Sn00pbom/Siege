from pandas import Series
from neuron import Neuron, RestrictedNeuron


class ZekeNet(object):

    def __init__(self, num_in, num_out, *num_hidden):

        self.num_in = num_in
        self.num_out = num_out
        self.num_hidden = num_hidden
        self.num_layers = 2 + len(num_hidden)

        # Neuron array l, n
        self.layers = []
        self.bias = []

        # setup neurons in layers array
        for l in range(self.num_layers):
            if l == 0:
                layer = [RestrictedNeuron() for x in range(self.num_in)]
                self.layers.append(layer)
            elif l == self.num_layers-1:
                layer = [Neuron() for x in range(self.num_out)]
                self.layers.append(layer)
            else:
                layer = [Neuron() for x in range(self.num_hidden[l-1])]
                self.layers.append(layer)

        # setup restricted neurons in bias array
        for l in range(self.num_layers-1):
            self.bias.append(RestrictedNeuron())

        # setup connections
        for l in range(self.num_layers - 1, 0, -1): # start at final index / output layer
            k_layer = self.layers[l]
            n_layer = self.layers[l-1]
            n_bias_neuron = RestrictedNeuron()
            for k_neuron in k_layer:
                for n_neuron in n_layer:
                    k_neuron.add_inbound_connection(n_neuron)

                k_neuron.add_inbound_connection(n_bias_neuron)


    def set_inputs(self, series):
        if series.size != self.num_in:
            print 'ZekeNet Error: Input mismatch'
            return
        for n in range(self.num_in):
            self.layers[0][n].val = series[n]

    def activate(self):
        for neuron in self.layers[self.num_layers-1]:
            neuron.activate()

    def mutate_weights(self):
        for layer in self.layers:
            for neuron in layer:
                if type(neuron) != RestrictedNeuron:
                    for connection in neuron.inbound_connections:
                        connection.mutate()


    def print_weights(self):
        num = 0
        for layer in self.layers:
            for neuron in layer:
                for connection in neuron.inbound_connections:
                    print connection.weight
                    num += 1
        print num
        # TODO FIX THIS SHIT

    def get_output(self):
        series = Series([neuron.val for neuron in self.layers[len(self.layers) -1 ]])
        return series