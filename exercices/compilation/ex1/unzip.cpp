#include <iostream>
#include <string>
#include <gzstream.h>
using namespace std;

int main (int argc, char ** argv)
{
  cout << "START" << endl;

  igzstream in(argv[1]);
  string line;
  while (getline(in, line))
  {
    cout << line << endl;
  }

  cout << "END" << endl;
}
