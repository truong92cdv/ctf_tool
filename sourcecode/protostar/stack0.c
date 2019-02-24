#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
	volatile int modified;
	char buffer[64];
	
	modified = 0;
	gets(buffer);

	if (modified != 0) {
		printf("You did it. You're flag is: {efiens}\n");
	} else {
		printf("Try again?\n");
	}
}