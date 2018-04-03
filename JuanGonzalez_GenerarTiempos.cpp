#include <iostream>
#include <ctime>

using namespace std;

//declaro funciones
int fibonacci(int N);
float get_time(int N);
int main(){
	int i;
	//for de impresion de primeros 35 terminos
	for(i =0;i<35;i++){
		//imprimo i y el tiempo de fibo(i)
		cout<<i<<","<<get_time(i)<<endl;
	}
	return 0;
}
int fibonacci(int N){
	//casos base
	if(N==0){
		return 0;
	}if(N==1){
		return 1;
	}
	//recursividad
	else{
		return fibonacci(N-1)+fibonacci(N-2);
	}
}
float get_time(int N){
	clock_t t;
	//tiempo inicial
	t=clock();
	fibonacci(N);
	//tiempo despues de correr fibo(N)
	t=clock()-t;
	//lo convierto en float
	float time=((float)t)/CLOCKS_PER_SEC;
	return time;
}
