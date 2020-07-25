// Construction of a Pascals Triangle
// Author: Pavan Kumar Paluri
#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int* pascal_triangle(int n)
{
  // Construct a 2-dimensional array
  int rows = n;
  int cols = n;
  int **pascal; // dynamic allocation of 2d array
  pascal = (int**)malloc(rows*sizeof(int*));
  for(int l=0; l<cols;l++)
    pascal[l] = (int*)malloc(cols*sizeof(int));
  int arr[rows];
  int val = -1;
  for(int i =0; i<n; i++)
  {
    for(int j=0; j<=i; j++)
    {
      // stopping condition 
      if(i==j || j==0)
      {
        pascal[i][j] = 1;
      }
      else 
      pascal[i][j] = pascal[i-1][j]+pascal[i-1][j-1];
    }
  }
  return pascal[n-1];

}
int main()
{
  int n = 6;
  int* arr;
  arr =pascal_triangle(n);
  for(int i=0; i<n;i++)
  cout << arr[i] << " ";

  return 0;
}
