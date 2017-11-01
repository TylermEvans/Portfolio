
all: copy compile


copy:
	/bin/cp \
		../libs-source/cgl/*.cpp 		\
		../libs-source/cgl/*.h 			\
		../libs-source/math3d/*.h 		\
		../libs-source/mixer/*.[ch] 	\
		../libs-source/net/*.[ch]		\
		../libs-source/png/*.[ch] 		\
		../libs-source/zlib/*.[ch] 		\
		../libs-source/*/*.txt 			\
		../libs-source/*/*.py			\
		.
compile:
	gcc -I. -I/usr/include/SDL2 -c -DOGG_MUSIC *.c
	g++ -c *.cpp
	
clean:
	-/bin/rm *.o
