/**
 * @file train_mnist
 * @brief Read mnist images and train a zero classifier
 * @author H. Harzallah
 */

#include "opencv2/opencv_modules.hpp"
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <opencv2/ml/ml.hpp>
#include <stdio.h>
#include <iostream>
#include <fstream>


using namespace std;
using namespace cv;

int main( int argc, char** argv )
{
  // Répertoire contenant les données MNIST
  char IMGDIR[] = "MNISTOpenCV/";
  string line;
  vector<Mat> posimgs;
  vector<Mat> negimgs;
  char lablfile[1024], imgname[1024];
  sprintf(lablfile, "%s%s", IMGDIR, "trainLabels.txt");
  
  int nbdim = 0;
  int lab, cc = 0;
  FILE * fd = fopen(lablfile, "r");
  // lire le fichier des labels d'apprentissage entier par entier
  while (fscanf(fd, "%d", &lab) != EOF){
	  // lire l'image correspondante
	  sprintf(imgname, "%sTrain/%d.jpg", IMGDIR, cc);
	  Mat m = imread(imgname, CV_LOAD_IMAGE_GRAYSCALE);
	  nbdim = m.rows * m.cols;
	  // en fonction que ça contienne un zero ou nom mettre dans la liste correspondante
	  if (lab == 0){
		  posimgs.push_back(m);
	  }else{
		  negimgs.push_back(m);
	  }
	  
	  cc++;
  }
  
  cc = 0;
  // déclarer une matrice qui devrait contenir tous les labels
  Mat labelsMat = Mat::zeros(posimgs.size()+negimgs.size(), 1, CV_32SC1);
  // un matrice qui devrait contenir toutes les données
  Mat trainingDataMat;
  for (unsigned int i=0;i<posimgs.size();i++){
	  Mat m = posimgs[i];
	  // une image est transformée en un vecteur
	  m = m.reshape(1, 1);
	  // on parcoure la liste des images positives, mettre le label à 1
	  labelsMat.at<int>(cc, 0) = 1.0;
	  if (cc == 0){
		// initialiser la matrice de données
		trainingDataMat = m.clone();
	  }else{
		// ajouter une ligne à la matrice de données
		trainingDataMat.push_back(m);
	  }
	  cc++;
  }
  
  for (unsigned int i=0;i<negimgs.size();i++){
	  Mat m = negimgs[i];
	  // une image est transformée en un vecteur
	  m = m.reshape(1, 1);
	  // on parcoure la liste des images négatives, mettre le label à 0
	  labelsMat.at<int>(cc, 0) = 0.0;
	  // ajouter une ligne à la matrice de données
	  trainingDataMat.push_back(m);
	  cc++;
  }
  
  trainingDataMat.convertTo(trainingDataMat, CV_32F);
  labelsMat.convertTo(labelsMat, CV_32F);
  
  printf("%d %d\n", trainingDataMat.type(), labelsMat.type());
  printf("Size : %d %d\n", trainingDataMat.rows, trainingDataMat.cols);
  printf("Pos size : %d\n", posimgs.size());
  printf("Neg size : %d\n", negimgs.size());
  
  CvSVMParams params;
  params.svm_type    = CvSVM::C_SVC;
  params.kernel_type = CvSVM::LINEAR;
  params.term_crit   = cvTermCriteria(CV_TERMCRIT_ITER, 100, 1e-6);
  
  // déclarer le SVM
  CvSVM SVM;
  // lancer l'apprentissage
  SVM.train(trainingDataMat, labelsMat, Mat(), Mat(), params);
  // enregistrer le modèle
  SVM.save("model.xml");

  return 0;
}
