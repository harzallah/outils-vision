#include <stdio.h>
#include <stdlib.h>

void mult(int a, int b, int *res){
	res = 0;
	*res = a*b;
}

int fact(int n){
	int f;
	if (n > 1){
		f = 1;
	}else{
		mult(n, fact(n-1), &f);
	}
	return f;
}

int main(int argc, char ** argv){
  int n;
  printf("Donner un entier \n");
  scanf("%d", &n);
  int f = fact(n);
  
  printf("Le produit factoriel est : %d\n", f);
}
