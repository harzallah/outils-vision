#include <stdio.h>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

int main( int argc, char** argv ){
  if (argc < 2){
    printf("Need 1 argument\n");
    return -1;
  }
  printf("reading : %s \n", argv[1]);
  Mat m = imread(argv[1]);
  imshow("Image" , m);
  waitKey();
  return 0;
}
