import numpy as np

class NueralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2*np.random.random((3,1))-1
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        return x*(1-x)
    def train(self,inp,outp,it):
        for i in range(it):
            output = self.think(inp)
            error = outp-output
            ad = np.dot(inp.T,error*self.sigmoid_derivative(output))
            self.synaptic_weights += ad
    def think(self,inp):
        inp = inp.astype(float)
        return self.sigmoid(np.dot(inp,self.synaptic_weights))
        
nueral_network = NueralNetwork()

print("random synaptic weights:")
print(nueral_network.synaptic_weights)

training_inputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

nueral_network.train(training_inputs,training_outputs,10000)

print("after training")
print(nueral_network.synaptic_weights)

a=input()
b=input()
c=input()

print(nueral_network.think(np.array([a,b,c])))
