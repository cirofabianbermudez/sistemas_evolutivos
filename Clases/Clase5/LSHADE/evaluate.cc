#include <math.h>

#define PI 3.1415926535897932384626433832795029

//  The same problema as before bur now with a constraint:

//double evaluate( double *vx, int n )
//{
	//double x = vx[0];
	//double y = (x-2.0)*(x-5.0) + sin(1.5*PI*x);

	//return( y );
//}


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


/**
import math

def Evalua( _n, vpar ) :
	suma = 0
	for i in range(_n):
		suma = suma +  (vpar[i]-2)*(vpar[i]-5) + math.sin( 1.5*math.pi*vpar[i])
		v = 0.1*suma
	return v
 
 def Evalua( _n, vpar ) :
	x = vpar[0]
	v = (x-2)*(x-5) + math.sin( 1.5*math.pi*x )

	return v
**/

/**
double evaluate( double *vx, int n )
{
	double x = vx[0];
	double y = (x-2.0)*(x-5.0) + sin(1.5*PI*x);

	double g = y - 5.0 - 2.5*(x - 6.0);

	//  The constraint is introduced according the penalization method :

	double c = g;
	if ( g > 0 ) {  // The solution is feasible
 		c = 0.0;
	}
	return( y + 20.0*c*c );
}
**/
