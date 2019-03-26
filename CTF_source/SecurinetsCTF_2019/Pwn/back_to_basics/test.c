#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char *ff (char *a1) {
	char *result;
	result = &a1[strlen(a1) -1];
	// *result = 0;
	return result;
}

int main(void) {
	char a1[] = "exhausted!";
	char *a2;
	a2 = ff(a1);
	// puts(ff("exhausted!"));
	puts(a2);
	return 0;
}