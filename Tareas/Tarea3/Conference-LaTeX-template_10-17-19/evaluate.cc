#include <math.h>
#define PI 3.1415926535897932384626433832795029

double evaluate( double *vx, int n )
{
	//double x = vx[0];
	double y = 0.0;
	for (int i = 0; i <= 9; i++) {
		y = y + (vx[i]-2.0)*(vx[i]-5.0) + sin(1.5*PI*vx[i]);
      }
	
	y = 0.1*y;

	return( y );
}
