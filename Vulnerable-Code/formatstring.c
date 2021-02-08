//Format string example
//If you give %p %n as an argument this will cause a segmentation fault
#include <stdio.h>

int main(int argc, char* argv){
	printf(argv[1]);
	return 0;
}
