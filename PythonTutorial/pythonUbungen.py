class Person(object):
    name = None
    age = None 
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sleep(self,nhours):
        print self.name,'is sleeping for',str(nhours),'hours'

#------------------------------------------------------------------------------------------------------------------------------------------

class Student(Person):
    
    def __init__(self,name,age):
        super(Student,self).__init__(name,age)
        
#-----------------------------------------------------------------------------------------------------------------------------------------

class Lecturer(Person):
    
    def __init__(self,name,age):
        super(Lecturer, self).__init__(name,age)

#######################################################################################
class Component(object):
    
    name = None


class Detector(Component):
    
    Id = None
    #name = None
    
    def __init__(self,Id,name):
        self.Id = Id
        self.name = name 
        
 #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
class Instrument(Component):
     
     #name = None
     detectors = []
     
     def __init__(self,name,detectors):
         self.name = name 
         self.detectors = detectors
         
     def printTree(self):
         for i in range(len(self.detectors)):
             print "Detector nr.",(i+1),"Id", self.detectors[i].Id,"name:",self.detectors[i].name
     
     
########################################################################################


person_object1 = Person('Martin',25)
person_object1.name = 'Franziska'

person_object2 = Person('Martin',23)

print "Person 1 name:",person_object1.name
print "Person 2 name:",person_object2.name

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

person1 = Person('Hans',12)

person1.sleep(7)

print 'Age of',person1.name,'is',person1.age

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

person_s = Student('Markus',20)
person_l = Lecturer('Lisa',40)

print 'Student name:', person_s.name 
print 'Lecturer name:',person_l.name 

 #######################################################################################
 
det1 = Detector(1,"bank1_1")
det2 = Detector(3,"bank1_2")
print 'DetectorId:',det1.Id,'and Detector name:',det1.name 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

dets = [det1,det1,det2]
inst1 = Instrument('MyInst',dets)
inst1.printTree()