#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
	char buffer[16];
	volatile int modified;
	
	modified = 0;
	gets(buffer);

	if (modified != 0) {
		printf("You did it. You're flag is: {efiens}\n");
	} else {
		printf("Try again?\n");
	}
}