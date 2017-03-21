from mantid.kernel import *
from mantid.api import *

class HelloWorld(PythonAlgorithm):
    
    def category(self):
        return 'Falsch'
    
    def PyInit(self):
        self.declareProperty("Parameter",-1.0,FloatBoundedValidator(lower=0))
        self.declareProperty("Prefix","",StringMandatoryValidator())
        self.declareProperty("ProcessOption","Full",StringListValidator(["Full","QuickEstimate"]))
        self.declareProperty("NIterations",100,IntBoundedValidator(lower=0),"Number of iterations of the loop to perform (default=100)")
        self.declareProperty('InputValue', -1,direction = Direction.Input,doc="A input value for this algorithm")
        self.declareProperty('OutputValue',-1,direction = Direction.Output)
        self.declareProperty(name="SummedValue", defaultValue=0,doc="Outputs the sum of the n iterations",direction=Direction.Output)
        
    def PyExec(self):
        nloops = self.getProperty("NIterations").value
        sum = 0
        for i in range(nloops):
            sum += 1
            
        self.setProperty("SummedValue",sum)
        self.log().information("The coube of the sum " + str(sum) + " is " + str(i*i*i))
        
 ##########################################################################################       
        
#AlgorithmFactory.subscribe(HelloWorld) 

hei = HelloWorld()
hei.PyInit()
hei.setProperty("NIterations",50)
print hei.getPropertyValue("SummedValue")
hei.PyExec()
print hei.getPropertyValue("SummedValue")