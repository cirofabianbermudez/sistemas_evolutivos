9.04.2020
Fraga

LSHADE source code
obtained from:

https://ryojitanabe.github.io/publication

Ryoji Tanabe and Alex Fukunaga:
Improving the Search Performance of SHADE Using Linear Population Size Reduction,
Proc. IEEE Congress on Evolutionary Computation (CEC2014), (pdf)

The search range must be adjusted in function:

void searchAlgorithm::initializeFitnessFunctionParameters() {

within file "search_algorithm.cc"

The function to optimize must be edited inside "evaluate.cc" file

To compile you can try:

$ make
$ ./lshade 123

