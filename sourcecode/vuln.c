//vuln.c
#include <stdio.h>
#include <string.h>

void foo(char* arg);
void bar(char* arg);

void foo(char* arg) {
 bar(arg); /* [1] */
}

void bar(char* arg) {
 char buf[256];
 strcpy(buf, arg); /* [2] */
}

int main(int argc, char *argv[]) {
 if(strlen(argv[1])>256) { /* [3] */
  printf("Attempted Buffer Overflow\n");
  fflush(stdout);
  return -1;
 }
 foo(argv[1]); /* [4] */
 return 0;
}