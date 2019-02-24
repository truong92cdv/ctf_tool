#include "stdio.h"
#include "stdint.h"
#include <string.h>

int CheckKey(uint8_t value, uint8_t index) {

	if (((((index >> 1) & 0x01) & !((index >> 7) & 0x01) & !((index >> 4) & 0x01) & !((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 1) & 0x01) & !((index >> 6) & 0x01) & !((index >> 5) & 0x01) & !((index >> 3) & 0x01) & ((index >> 4) & 0x01)) | (!((index >> 5) & 0x01) & ((index >> 4) & 0x01) & ((index >> 0) & 0x01) & !((index >> 7) & 0x01) & !((index >> 2) & 0x01) & ((index >> 1) & 0x01) & ((index >> 3) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 6) & 0x01) & !((index >> 2) & 0x01) & !((index >> 4) & 0x01) & !((index >> 1) & 0x01) & ((index >> 5) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01)) | (!((index >> 4) & 0x01) & !((index >> 1) & 0x01) & !((index >> 0) & 0x01) & !((index >> 6) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 2) & 0x01)) | (((index >> 0) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01) & ((index >> 2) & 0x01)) | (((index >> 2) & 0x01) & !((index >> 0) & 0x01) & !((index >> 5) & 0x01) & !((index >> 7) & 0x01) & ((index >> 1) & 0x01) & !((index >> 6) & 0x01)) | (((index >> 2) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01) & !((index >> 7) & 0x01) & ((index >> 3) & 0x01) & !((index >> 6) & 0x01))) != ((value >> 0) & 0x01)) {
		return 0;
	}
	if (((!((index >> 6) & 0x01) & !((index >> 7) & 0x01) & ((index >> 0) & 0x01) & !((index >> 1) & 0x01) & !((index >> 5) & 0x01) & !((index >> 3) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 6) & 0x01) & ((index >> 3) & 0x01) & !((index >> 0) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01)) | (((index >> 1) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & ((index >> 4) & 0x01) & !((index >> 5) & 0x01) & !((index >> 2) & 0x01)) | (((index >> 4) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & !((index >> 5) & 0x01) & ((index >> 1) & 0x01) & !((index >> 3) & 0x01)) | (((index >> 2) & 0x01) & !((index >> 1) & 0x01) & !((index >> 5) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & ((index >> 0) & 0x01)) | (!((index >> 5) & 0x01) & ((index >> 2) & 0x01) & !((index >> 4) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & !((index >> 0) & 0x01))) != ((value >> 1) & 0x01)) {
		return 0;
	}
	if (((!((index >> 2) & 0x01) & !((index >> 5) & 0x01) & ((index >> 0) & 0x01) & !((index >> 3) & 0x01) & !((index >> 6) & 0x01) & !((index >> 4) & 0x01) & !((index >> 7) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 0) & 0x01) & !((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 2) & 0x01) & !((index >> 1) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & !((index >> 0) & 0x01) & !((index >> 7) & 0x01)) | (!((index >> 7) & 0x01) & ((index >> 2) & 0x01) & ((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01) & !((index >> 6) & 0x01) & ((index >> 0) & 0x01)) | (!((index >> 6) & 0x01) & ((index >> 2) & 0x01) & ((index >> 4) & 0x01) & !((index >> 5) & 0x01) & !((index >> 7) & 0x01) & ((index >> 0) & 0x01)) | (!((index >> 4) & 0x01) & !((index >> 1) & 0x01) & !((index >> 6) & 0x01) & ((index >> 0) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01) & !((index >> 2) & 0x01)) | (!((index >> 6) & 0x01) & !((index >> 2) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01) & !((index >> 7) & 0x01) & !((index >> 3) & 0x01))) != ((value >> 2) & 0x01)) {
		return 0;
	}
	if (((!((index >> 6) & 0x01) & !((index >> 5) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01) & !((index >> 0) & 0x01) & !((index >> 4) & 0x01) & ((index >> 1) & 0x01)) | (!((index >> 0) & 0x01) & !((index >> 6) & 0x01) & ((index >> 2) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 4) & 0x01)) | (!((index >> 4) & 0x01) & !((index >> 6) & 0x01) & ((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01) & !((index >> 7) & 0x01) & !((index >> 2) & 0x01)) | (((index >> 2) & 0x01) & ((index >> 1) & 0x01) & !((index >> 0) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 4) & 0x01) & !((index >> 6) & 0x01)) | (((index >> 0) & 0x01) & ((index >> 4) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & !((index >> 3) & 0x01) & !((index >> 1) & 0x01) & !((index >> 2) & 0x01) & !((index >> 7) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & ((index >> 1) & 0x01) & ((index >> 4) & 0x01) & ((index >> 2) & 0x01) & ((index >> 0) & 0x01)) | (((index >> 2) & 0x01) & !((index >> 6) & 0x01) & ((index >> 0) & 0x01) & ((index >> 3) & 0x01) & !((index >> 7) & 0x01) & !((index >> 1) & 0x01) & !((index >> 5) & 0x01)) | (!((index >> 7) & 0x01) & ((index >> 5) & 0x01) & !((index >> 4) & 0x01) & !((index >> 2) & 0x01) & !((index >> 3) & 0x01) & !((index >> 6) & 0x01) & ((index >> 0) & 0x01) & !((index >> 1) & 0x01))) != ((value >> 3) & 0x01)) {
		return 0;
	}
	if (((((index >> 0) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & ((index >> 2) & 0x01)) | (((index >> 1) & 0x01) & !((index >> 6) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & ((index >> 2) & 0x01)) | (!((index >> 4) & 0x01) & !((index >> 7) & 0x01) & ((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 0) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 4) & 0x01) & ((index >> 1) & 0x01) & ((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 5) & 0x01) & !((index >> 1) & 0x01) & ((index >> 4) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 5) & 0x01) & ((index >> 0) & 0x01) & !((index >> 6) & 0x01) & !((index >> 3) & 0x01) & ((index >> 4) & 0x01)) | (!((index >> 6) & 0x01) & ((index >> 0) & 0x01) & !((index >> 7) & 0x01) & ((index >> 4) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01)) | (!((index >> 6) & 0x01) & !((index >> 0) & 0x01) & !((index >> 5) & 0x01) & !((index >> 7) & 0x01) & ((index >> 3) & 0x01) & ((index >> 1) & 0x01)) | (!((index >> 3) & 0x01) & !((index >> 4) & 0x01) & !((index >> 1) & 0x01) & ((index >> 0) & 0x01) & !((index >> 2) & 0x01) & !((index >> 6) & 0x01) & !((index >> 7) & 0x01) & ((index >> 5) & 0x01)) | (((index >> 3) & 0x01) & ((index >> 2) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & !((index >> 5) & 0x01))) != ((value >> 4) & 0x01)) {
		return 0;
	}
	if (((((index >> 2) & 0x01) & !((index >> 5) & 0x01) & !((index >> 0) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 2) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & ((index >> 1) & 0x01)) | (!((index >> 6) & 0x01) & !((index >> 7) & 0x01) & ((index >> 2) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01) & !((index >> 3) & 0x01)) | (!((index >> 5) & 0x01) & !((index >> 6) & 0x01) & ((index >> 3) & 0x01) & !((index >> 7) & 0x01) & ((index >> 1) & 0x01)) | (!((index >> 4) & 0x01) & !((index >> 3) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & !((index >> 1) & 0x01) & !((index >> 2) & 0x01)) | (!((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 4) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 2) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & ((index >> 0) & 0x01) & ((index >> 3) & 0x01)) | (!((index >> 6) & 0x01) & ((index >> 4) & 0x01) & !((index >> 5) & 0x01) & !((index >> 0) & 0x01) & !((index >> 7) & 0x01))) != ((value >> 5) & 0x01)) {
		return 0;
	}
	if (((((index >> 2) & 0x01) & !((index >> 6) & 0x01) & !((index >> 7) & 0x01) & ((index >> 1) & 0x01) & !((index >> 0) & 0x01) & !((index >> 5) & 0x01) & !((index >> 4) & 0x01)) | (!((index >> 3) & 0x01) & !((index >> 2) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 0) & 0x01) & !((index >> 1) & 0x01) & !((index >> 3) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & !((index >> 7) & 0x01)) | (!((index >> 5) & 0x01) & !((index >> 6) & 0x01) & !((index >> 7) & 0x01) & ((index >> 4) & 0x01) & ((index >> 1) & 0x01) & ((index >> 0) & 0x01)) | (!((index >> 2) & 0x01) & !((index >> 7) & 0x01) & !((index >> 4) & 0x01) & !((index >> 3) & 0x01) & ((index >> 0) & 0x01) & !((index >> 1) & 0x01) & !((index >> 6) & 0x01)) | (!((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 1) & 0x01) & ((index >> 0) & 0x01) & !((index >> 6) & 0x01) & !((index >> 4) & 0x01)) | (!((index >> 5) & 0x01) & ((index >> 0) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & !((index >> 2) & 0x01) & !((index >> 4) & 0x01)) | (!((index >> 5) & 0x01) & !((index >> 6) & 0x01) & !((index >> 7) & 0x01) & !((index >> 2) & 0x01) & !((index >> 0) & 0x01) & ((index >> 4) & 0x01)) | (!((index >> 1) & 0x01) & !((index >> 7) & 0x01) & !((index >> 5) & 0x01) & !((index >> 6) & 0x01) & ((index >> 0) & 0x01) & ((index >> 3) & 0x01) & ((index >> 2) & 0x01)) | (!((index >> 2) & 0x01) & !((index >> 1) & 0x01) & !((index >> 4) & 0x01) & !((index >> 7) & 0x01) & !((index >> 6) & 0x01) & !((index >> 5) & 0x01))) != ((value >> 6) & 0x01)) {
		return 0;
	}

	return 1;
}

int main() {
	char input[256];
	int szFlag = 34;
	
	printf("*******************************\n");
	printf("*    .:Welcome to Efiens:.    *\n");
	printf("*******************************\n");
	
	memset(input, 0, sizeof(input));
	
	printf("Enter your flag: ");
	if (!fgets(input, sizeof(input), stdin)) {
		return 1;
	}
	
	input[szFlag] = 0;
	
	for (int i = 0; i < szFlag; i++) {
		if (CheckKey(input[i], i) == 0) {
			printf("Invalid flag!\n");
			return 1;
		}
	}
	
	printf("Valid flag!\nSubmit online to claim your point.\n");
	
	return 0;
}