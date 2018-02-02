

/* Insertion sort ascending order */
 
#include <stdio.h>
#include <stdlib.h>
 
int main()
{
  int n, c, d, t;
 
  printf("Donner la taille du tableau\n");
  scanf("%d", &n);
  int * array = (int *) malloc(n * sizeof(int));
  printf("Donner %d entiers\n", n);
 
  for (c = 0; c < n; c++) {
    scanf("%d", &array[c]);
  }
 
  for (c = 1 ; c <= n ; c++) {
    d = c;
 
    while ( d > 0 && array[d-1] > array[d]) {
      t          = array[d];
      array[d]   = array[d-1];
      array[d-1] = t;
 
      d--;
    }
  }
 
  printf("Tableau trié :\n");
 
  for (c = 0; c <= n - 1; c++) {
    printf("%d\n", array[c]);
  }
 
  return 0;
}
