cpp_vs_python.png : times_python.csv times_cpp.csv
	python JuanGonzalez_Graficas.py
times_python.csv : 
	python JuanGonzalez_GenerarTiempos.py > times_python.csv
times_cpp.csv : gen_times.x
	./gen_times.x > times_cpp.csv
gen_times.x : 
	c++ JuanGonzalez_GenerarTiempos.cpp -o gen_times.x


clean : 
	rm times_cpp.csv times_python.csv cpp_vs_python.png gen_times.x

