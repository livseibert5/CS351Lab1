#include <stdlib.h>
#include <stdio.h>
#define LEN 32

void main() {
  unsigned char* key = (unsigned char*) malloc(sizeof(unsigned char) * LEN);
  FILE* random = fopen("/dev/urandom", "r");
  fread(key, sizeof(unsigned char)*LEN, 1, random);
  fclose(random);
  for (int i = 0; i < 32; i++) {
  	printf("%x", *key + i*sizeof(unsigned char));
  }
}