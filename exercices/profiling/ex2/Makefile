default: prog

prog: Inutile.o ex2.o
	g++ Inutile.o ex2.o -o prog

ex2.o: ex2.cpp
	g++ -c ex2.cpp

Inutile.o: Inutile.cpp
	g++ -c Inutile.cpp

clean:
	rm *.o prog
