#include <stdio.h>
#include <stdlib.h>
#include "Inutile.hpp"

int main(int argc, char ** argv){
	Inutile * i = new Inutile();
	i->saisie();
	i->affichage();
	delete i;
}
