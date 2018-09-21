import pyedflib
import sklearn
import matplotlib.pyplot as plt
import numpy as np

try:
    print('n')
    import matlab.engine
    eng = matlab.engine.start_matlab()
except:
    from oct2py import Oct2py
    import pprint
    #octave.addpath('/spectralcluster')

f = pyedflib.EdfReader("134_aliengonogo_parent.bdf")
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))
for i in np.arange(n):
    sigbufs[i, :] = f.readSignal(i)

print(sigbufs.shape)
out = octave.EEGClustering(sigbufs)
pprint.pprint(out)

'''for ds in sigbufs[:10]:
    plt.plot(ds); plt.show()'''

a = dir(f)
'''for m in a:
    attr = getattr(f,m)
    if callable(attr):
        try:
            print(m, ": ", attr())
        except:
            continue
    else:
        print(m, ": ", attr)'''

