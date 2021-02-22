#include "de.h"

// The values for these variables will be set at the beginning
// of main function
int g_problem_size;
unsigned int g_max_num_evaluations;

int g_pop_size;
int g_memory_size;
double g_arc_rate;
double g_p_best_rate;

int main( int argc, char *argv[] )
{
	if ( argc != 2 ) {
		cout << "Args: seed\n"; 
		return 1;
	}
	unsigned seed = (unsigned) strtol( argv[1], NULL, 10);

	// El número de variables	
	g_problem_size = 10;

	//available number of fitness evaluations 
	// g_max_num_evaluations = g_problem_size * 2000;
	g_max_num_evaluations = 10000;

	//random seed is selected based on time according to competition rules
	// srand((unsigned)time(NULL));
	srand( seed );

	//L-SHADE parameters
	// g_pop_size = (int)round(g_problem_size * 18);
	g_pop_size = 180;
	

	// Parámetros por defecto
	g_memory_size = 5;
	g_arc_rate = 1.4;
	g_p_best_rate = 0.11;

	searchAlgorithm *alg = new LSHADE();
	Fitness v = alg->run();
	cout << v << endl;

	return 0;
}
