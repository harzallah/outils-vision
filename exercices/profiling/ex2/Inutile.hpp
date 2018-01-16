#include <stdio.h>
#include <stdlib.h>

#define TABSIZE 5

class Inutile{
	private :
	  int * tab;
	public :
		Inutile(){
			tab = (int *) malloc(sizeof(int)*TABSIZE);
		}
		
		~Inutile(){
			
		}
		
		void saisie();
		void affichage();
	
};
