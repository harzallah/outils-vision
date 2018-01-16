#include "Inutile.hpp"

void Inutile::affichage(){
	int s;
	for (int i=0;i<TABSIZE;i++){
		printf("pos : %d, val : %d\n", i, tab[i]);
		s += tab[i];
	}
	printf("La somme est : %d\n", s);
}

void Inutile::saisie(){
	
	for (int i=0;i<TABSIZE;i++){
		printf("Donner un entier\n");
		scanf("%d", &tab[i]);
	}
	
	
}
