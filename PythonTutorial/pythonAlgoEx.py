from mantid.kernel import *
from mantid.api import *

class Fibonacci(PythonAlgorithm):
    
    def category(self):
        return 'Exercise'
        
    def PyInit(self):
        self.declareProperty("NTerms",0,IntBoundedValidator(lower=0),doc="Number of the first numbers to be printet "
                                                                                                                        " to the log of the Fibonacci series")
        
        
    def PyExec(self):
        n = self.getProperty("NTerms").value
        first = 0
        second = 1
        
        for i in range(n):
            self.log().notice("Term " + str(i+1) + " in the Fibonacci series id: " + str(first))
            help = second
            second += first
            first = help
            
        
        
 ##########################################################################################
 
AlgorithmFactory.subscribe(Fibonacci) 
 
Fib = Fibonacci()
Fib.PyInit()
Fib.log().debug(Fib.getPropertyValue("NTerms"))