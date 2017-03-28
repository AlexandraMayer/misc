import numpy as np

xbins = 2000
ybins = 2000

datax = np.linspace(0.0, 324.0, xbins+1)
datay = np.ones((xbins*ybins))

ws = CreateWorkspace(DataX=datax, DataY=datay, DataE=np.sqrt(datay), NSpec=ybins, UnitX="DeltaE")

LoadInstrument(ws,False,InstrumentName="ARCS")
AddSampleLog(ws,"proposal_number","3")
AddSampleLog(ws, "proposal_title", "A")
AddSampleLog(ws,"experiment_team","Team name")
AddSampleLog(ws,"temperature","234.56", LogUnit="F")
AddSampleLog(ws,"Ei","1.23",LogUnit="meV")

path = os.path.expanduser("~/testpythonyda.yaml")

print ws.getNumberHistograms()
print ws.blocksize()

t0 = time.clock()
SaveYDA(ws,path)
print "SaveYDA: ", time.clock() - t0

#t0= time.clock()
#SaveYDAPy(ws,path)
#print "SaveYDAPy: ",time.clock() -t0