path = os.path.expanduser("~/testpythonyda.yaml")

#t0c = time.clock()
#ws = LoadYDA(path)
#t1c  = time.clock() - t0c



t0p = time.clock()
ws = LoadYDAPy(path)
t1p = time.clock() - t0p

print "Histograms: ", ws.getNumberHistograms()
print "Values: ", ws.blocksize()

#print "Time cpp: ", t1c
print "Time Python: ", t1p