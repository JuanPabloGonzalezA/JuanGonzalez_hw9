gen_times.x : JuanGonzalez_GenerarTiempos.cpp
	c++ JuanGonzalez_GenerarTiempos.cpp -o gen_times.x
times_cpp.csv : gen_times.x
	./gen_times.c > times_cpp.csv
times_python.csv : JuanGonzalez_GenerarTiempos.py
	python JuanGonzalez_GenerarTiempos.py > times_python.csv
cpp_vs_python.png : JuanGonzalez_GenerarTiempos.py
	python JuanGonzalez_GenerarTiempos.py

