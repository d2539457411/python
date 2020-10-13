# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
t=np.arange(-10.0, 10.0, 0.01)
y=np.exp(t*2)*3
plt.figure(1)
plt.subplot(211)
plt.plot(t, y)
show()