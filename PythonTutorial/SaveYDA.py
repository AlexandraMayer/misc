from mantid.api import *
from mantid.kernel import*

import yaml
import math

class SaveYDAPy(PythonAlgorithm):
    
    def category(self):
        return 'DataHandling'   
    
    def PyInit(self):
        
        wsValidators = CompositeValidator()
        wsValidators.add(WorkspaceUnitValidator("DeltaE"))
        wsValidators.add(InstrumentValidator())
        
        self.declareProperty(MatrixWorkspaceProperty("InputWorkspace","",validator=wsValidators,direction=Direction.Input),doc="Workspace to save")
        self.declareProperty(FileProperty(name="Filename",defaultValue="",action=FileAction.Save,extensions=""),"The name to use when writing the file")
        
        
    def getBinCenters(self,ax,bin):
        
        ax = None
        bin = []
        
        for i in range (1,ax.length()):
            bin.append((ax.getValue(i)+ax.getValue(i-1))/2)
        
        
    def validateInputs(self):
        
        issues = dict()
        
        #allowedUnits = ['q']
        ws = self.getProperty("InputWorkspace").value
        
        allowedUnit = 'q'
        ax = ws.getAxis(1)
        
        if not ax.isSpectra() and axis.unit().capiton() != allowedUnit:
            issues["InputWorkspace"] = "Y axis is not 'Spectrum Axis' or 'Momentum Transfer'"
        
        if isinstance(ws,IEventWorkspace):
            issues["InputWorkspace"] = "The InputWorkspace must be a Workspace2D"

        return issues
        
        
    def PyExec(self):
        
        ws = mtd[self.getPropertyValue('InputWorkspace')]
        filename = self.getProperty("Filename").value
        
        file = open(filename,"w")
        
        run = ws.getRun()
        ax = ws.getAxis(1)
        nHist = ws.getNumberHistograms()
        
        metadata = dict()
        
        metadata["format"] = "yaml/frida 2.0"
        metadata["type"] = "gerneric tabular data"
        
        
        hist = []
        
        propn ="Proposal number " + run.getLogData("proposal_number").value
        propt = run.getLogData("proposal_title").value
        expt = run.getLogData("experiment_team").value
        
        hist.append(propn)
        hist.append(propt)
        hist.append(expt)
        hist.append("data reduced with mantid")
        
        
        rpar = []
        
        temperature = run.getLogData("temperature").value
        eimeV = run.getLogData("Ei").value
        
        temp = dict()
        temp["name"] = "T"
        temp["unit"] = "K"
        temp["val"] =  temperature
        temp["stdv"] = 0
        
        ei = dict()
        ei["name"] = "Ei"
        ei["unit"] = "meV"
        ei["val"] = eimeV
        ei["stdv"] = 0
        
        rpar.append(temp)
        rpar.append(ei)
        
        coord = []
        
        xc = dict()
        x = dict()
        
        x["name"] = "w"
        x["unit"] = "meV"
        
        xc["x"] =  x
        
        yc = dict()
        y = dict()
        
        y["name"] = "S(q,w)"
        y["unit"] = "meV-1"
       
        yc["y"] = y
        
        zc = dict()
        z = dict()
        
        if(ax.isSpectra):
            zname = "2th"
            zunit = "deg"
        else:
            zname = "q"
            zunit = "A-1"
        
        z["name"] =  zname
        z["unit"] = zunit
        
        zc["z"] = z
        
        coord.append(xc)
        coord.append(yc)
        coord.append(zc)
        
        slices = []
        
        bin = []
        
        if(ax.isSpectra):
            samplePos = ws.getInstrument().getSample().getPos()
            sourcePos = ws.getInstrument().getSource().getPos()
            beamPos = samplePos - sourcePos
            for i in range(nHist):
                detector = ws.getDetector(i)
                twoTheta = detector.getTwoTheta(samplePos,beamPos)*180/math.pi
                bin.append(twoTheta)
        elif(ax.length() == nHist):
            for i in range(ax.length()):
                bin.append(ax.getValue())
        else:
            bin = getBinCenters(ax,bin).bin
            
        for i in range(nHist):
            
            ys = ws.y(i)
            
            yv = []
            xcenters = []
            
            xcenters= getBinCenters(ws.getAxis(0), xcenters)
            
            for j in range(ys.size()):
                yv.append(ys[j])
            
        
            slicethis = dict()
            slicethis["j"] =
            slicethis["z"] =
            slicethis
            
            slices.append()
            
   
            
        
        data = dict()
        
        data["Meta"] = metadata
        data["History"]  = hist
        data["RPar"] = rpar
        data["Coord"] = coord
        data["Test"] = bin
        
        print yaml.dump(data,default_flow_style=False)
        
        
        file.write('')
        
        
        
AlgorithmFactory.subscribe(SaveYDAPy) 