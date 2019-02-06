#include <stdio.h>

int main(int argc, char **argv) {
	char buffer[512];
	int cookie = 0;
	printf("&cookie: %p\n", &cookie);
	gets(buffer);
	printf("cookie = %.8X\n", cookie);
	printf(buffer);
	printf("\ncookie = %.8X\n", cookie);
	return 0;
}