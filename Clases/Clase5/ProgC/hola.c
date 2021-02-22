#include <stdio.h>

extern double f( double );

int main( )
{
	// printf( "Hola mundo!\n" );
	double v;

	v = f( 2.0 );
	printf( "%lf\n", v );


	return 0;
}
