import numpy as np
import matplotlib.pyplot as plt
import time

def fibonacci(N):
	if N==0:#caso base
		return 0
	elif N==1:#caso base
		return 1
	else:#caso recursivo
		return fibonacci(N-1)+fibonacci(N-2)
def get_time(N):
	t0=time.time()#tiempo inicial
	fibonacci(N)#corro fibo(N)
	return time.time()-t0#retorno la diferencia de tiempos
for i in range(0,35):#recorrido para imprimir de 0 a 34 fibo(n)
	print str(i)+","+str(get_time(i))
