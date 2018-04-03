import numpy as np
import matplotlib.pyplot as plt

#importo datos de cpp y python
cpp=np.genfromtxt('times_cpp.csv',delimiter=',')
pyth=np.genfromtxt('times_python.csv',delimiter=',')

#graficas
plt.plot(cpp[:,0],cpp[:,1],label='c++')
plt.plot(pyth[:,0],pyth[:,1],label='python')
plt.xlabel('N')
plt.ylabel('tiempo')
plt.title('tiempo vs N')
plt.legend()
plt.savefig('cpp_vs_python.png')
