#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv){

  int total;
  for (int i=0;i<argc;i++){
    total += atoi(argv[i]);
  }

  printf("Total is : %d \n", total);

}
