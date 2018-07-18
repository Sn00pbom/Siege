from neuralnetwork import ZekeNet
import pandas


net = ZekeNet(1,10,2)
input = pandas.Series([2.])
net.set_inputs(input)
net.print_weights()
print '----------------'
net.mutate_weights()
net.print_weights()
net.activate()
print net.get_output()

