#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <unistd.h>
#include "global.h"


int haceArchivo( char *nombre, int *x, int n )
{
	FILE * arch;

	if ((arch=fopen( nombre, "w" ))==NULL ) {
		fprintf( stderr, "No puedo abrir archivo %s\n", nombre );
		exit(90);
	}

	fprintf( arch,
	  ".param W1=%du W2=%du W3=%du W4=%du W5=%du\n"
	  ".param W6=%du W7=%du", x[0], x[1], x[2], x[3], x[4], x[5], x[6] );

	fclose( arch );
	return( 0 );
}

void evalua_circuito( char *miargv[] )
{
	pid_t pid;
	int ret;
	char *envp[] = { NULL };

	switch ( pid = fork() ) {
		case -1:
			perror("fork()");
			exit(EXIT_FAILURE);

		case 0:  /* in the child */
			ret = execve("/usr/local/bin/ngspice", miargv, envp);
			/** fprintf( stderr, "Cir %d\n", ret );
			exit( ret ); ** only happens if execve(2) fails **/

		default:
			if ( waitpid(pid, &ret, 0) < 0 ) {
				perror("wait pid()");
				exit(EXIT_FAILURE);
			}
	}
}

void ejecutaNgspice( )
{
	char *argv1[6] = { "/usr/local/bin/ngspice", "-b", "-o", "", "", NULL };

	argv1[3] = "cir1.lis";
	argv1[4] = "cir1.sp";
	evalua_circuito( argv1 );

	argv1[3] = "cir2.lis";
	argv1[4] = "cir2.sp";
	evalua_circuito( argv1 );
	/**
	argv1[3] = "cir3.lis";
	argv1[4] = "cir3.sp";
	evalua_circuito( argv1 );
	**/
}


int checaSaturacion( char *nombreArchivo, double *sat, int ntran )
{
	#define DISPOSITIVOS 17
	char linea[100];
	FILE *parch;
	int estado, ndev;
	double vth[DISPOSITIVOS];
	double vgs[DISPOSITIVOS];
	double vds[DISPOSITIVOS];
	int nn, i;
	char *paux;
	char **ap, *argv[4];
 
	parch = fopen ( nombreArchivo, "r" );
	if( parch == NULL ) {
		fprintf( stderr, "No puedo abrir el archivo %s\n", nombreArchivo );
		exit(-2);
	}
 
	estado = 0;
	ndev = 0;

	nn = 0;
	i = 0;

	while(1) { 
		if( fgets( linea, 100, parch ) == NULL )
			break;

		if ( estado == 0 ) {
			if( strncmp( linea, " BSIM", 5 ) == 0 ) {
				if( strncmp( linea, " BSIM3v1:", 9 ) == 0 ) {
					estado = 1;
				}
			}
		}
		else if ( estado == 1 ) {
			if( strncmp( linea, "     device", 11 ) == 0 ) {
				paux = linea + 11;
				for (nn=0, ap = argv; (*ap = strsep( &paux, " ")) != NULL; ){
					if (**ap != '\0'){
						if (++ap > &argv[3])
							break;
						nn++;
					}
				}
				paux = argv[0];
				if ( *paux == 'm' ) {
					estado = 2;
				}
			} 
		}
		else if ( estado == 2 ) {
			if( strncmp( linea, "        vth", 11 ) == 0 ) {
				paux = linea + 11;
				for (i=0, ap = argv; (*ap = strsep( &paux, " ")) != NULL; ){
					if (**ap != '\0') {
						if (++ap > &argv[3])
							break;
						vth[ndev+i] = strtod( argv[i], (char **)NULL );
						i++;	
					}
				}
				estado = 3;
			}
		}
		else if ( estado == 3 ) {
			if( strncmp( linea, "        vgs", 11 ) == 0 ) {
				paux = linea + 11;
				for (i=0, ap = argv; (*ap = strsep( &paux, " ")) != NULL; ){
					if (**ap != '\0') {
						if (++ap >= &argv[4])
							break;
						vgs[ndev+i] = strtod( argv[i], (char **)NULL );
						i++;
					}
				}
				estado = 4;
			}
		}
		else if ( estado == 4 ) {
			if( strncmp( linea, "        vds", 11 ) == 0 ) {
				paux = linea + 11;
				for (i=0, ap = argv; (*ap = strsep( &paux, " ")) != NULL; ){
					if (**ap != '\0') {
						if (++ap >= &argv[4])
							break;
						vds[ndev+i] = strtod( argv[i], (char **)NULL );
						i++;
					}
				}
				ndev += nn;  //  Número global de transistores
				if ( ndev > DISPOSITIVOS ) {
					fprintf( stderr, "Aumentar los tamaños de los buffers\n" );
					exit(-1);
				}
				estado = 0;
			}
		}
	}

	fclose( parch );
	
	// Checa si los transistores están saturados
	if ( ndev != ntran ){
		fprintf( stderr, "Hay %d transistores en el archivo %s\n", ndev, nombreArchivo );
		return(-3);
	}
	// printf( "%d\n", ndev );
	for( i=0; i<ndev; i++ ) {
		if ( vgs[i] > vth[i] && vds[i] > (vgs[i] - vth[i]) )
			sat[i] = 1;
			//# print vgs[i], ">", vth[i]
			//# print vds[i], ">", vgs[i]-vth[i]
			//# print nom[i], 1
		else 
			//# print nom[i], -1
			sat[i] = -1;
	}
	return 0;
}

double analiza( char *nombre, char *etiqueta )
{
	FILE *parch;
	char linea[84];
	char *paux1, *paux2;
	int n, m;

	parch = fopen( nombre, "r" );
	if ( parch == NULL ){
		fprintf( stderr, "No puedo abrir el archivo %s\n", nombre );
		exit(-1);
	}

	n = strlen( etiqueta );

	while( 1 ) {
		if( fgets( linea, 84, parch ) == NULL ) {
			fprintf( stderr, "No se encontró etiqueta %s en archivo %s\n", etiqueta, nombre );
			fclose( parch );
			return -10;
			// exit(-2);
		}

		if( strncmp( linea, etiqueta, n ) == 0 ) {
			paux1 = linea;
			while ( *paux1 != '=' )	
				paux1++;
			paux1++;
			while ( *paux1 == ' ' )	
				paux1++;

			m = strlen( linea );
			paux2 = linea + m;
			while ( *paux2 == '\n' || *paux2 == '\0'  )	
				*paux2-- = '\0';

			// printf( "%s ", paux1 );
			fclose( parch );
			return ( strtod( paux1, (char **)NULL) );
		}
	}
}

int analiza3( char *nombre, char *etiqueta1, char *etiqueta2, char *etiqueta3, double val[] )
{
	FILE *parch;
	char linea[84];
	char *paux1, *paux2;
	int n1, n2, n3, estado=0;

	parch = fopen( nombre, "r" );
	if ( parch == NULL ){
		fprintf( stderr, "No puedo abrir el archivo %s\n", nombre );
		exit(-1);
	}

	n1 = strlen( etiqueta1 );
	n2 = strlen( etiqueta2 );
	n3 = strlen( etiqueta3 );

	while( 1 ) {
		if( fgets( linea, 84, parch ) == NULL ) {
			fprintf( stderr, "No se encontró etiquetas en archivo %s\n", nombre );
			fclose( parch );
			return -10;
			// exit(-2);
		}

		if ( estado==0 ) {
			if( strncmp( linea, etiqueta1, n1 ) == 0 ) {
				paux1 = linea;
				while ( *paux1 != '=' )	
					paux1++;
				paux1++;
				while ( *paux1 == ' ' )	
					paux1++;
	
				paux2 = linea + strlen( linea );
				while ( *paux2 == '\n' || *paux2 == '\0'  )	
					*paux2-- = '\0';

				val[0] = strtod( paux1, (char **)NULL);
				estado = 1;
			}
		}
		else if ( estado==1 ) {
			if( strncmp( linea, etiqueta2, n2 ) == 0 ) {
				paux1 = linea;
				while ( *paux1 != '=' )	
					paux1++;
				paux1++;
				while ( *paux1 == ' ' )	
					paux1++;
	
				paux2 = linea + strlen( linea );
				while ( *paux2 == '\n' || *paux2 == '\0'  )	
					*paux2-- = '\0';

				val[1] = strtod( paux1, (char **)NULL);
				estado = 2;
			}
		}
		else if ( estado==2 ) {
			if( strncmp( linea, etiqueta3, n3 ) == 0 ) {
				paux1 = linea;
				while ( *paux1 != '=' )	
					paux1++;
				paux1++;
				while ( *paux1 == ' ' )	
					paux1++;
	
				paux2 = linea + strlen( linea );
				while ( *paux2 == '\n' || *paux2 == '\0'  )	
					*paux2-- = '\0';

				val[2] = strtod( paux1, (char **)NULL);
				estado = 3;
				break;
			}
		}
	}
	fclose( parch );
	if ( estado != 3 ) return -1;
	return 0;
}

int analiza4( char *nombre, char *etiqueta1, char *etiqueta2, char *etiqueta3, char *etiqueta4, double val[] )
{
	FILE *parch;
	char linea[84];
	char *paux1, *paux2;
	int n1, n2, n3, n4, estado=0;

	parch = fopen( nombre, "r" );
	if ( parch == NULL ){
		fprintf( stderr, "No puedo abrir el archivo %s\n", nombre );
		exit(-1);
	}

	n1 = strlen( etiqueta1 );
	n2 = strlen( etiqueta2 );
	n3 = strlen( etiqueta3 );
	n4 = strlen( etiqueta4 );

	while( 1 ) {
		if( fgets( linea, 84, parch ) == NULL ) {
			fprintf( stderr, "No se encontró etiquetas en archivo %s\n", nombre );
			fclose( parch );
			return -10;
			// exit(-2);
		}

		if ( estado==0 ) {
			if( strncmp( linea, etiqueta1, n1 ) == 0 ) {
				paux1 = linea;
				while ( *paux1 != '=' )	
					paux1++;
				paux1++;
				while ( *paux1 == ' ' )	
					paux1++;
	
				paux2 = linea + strlen( linea );
				while ( *paux2 == '\n' || *paux2 == '\0'  )	
					*paux2-- = '\0';

				val[0] = strtod( paux1, (char **)NULL);
				estado = 1;
			}
		}
		else if ( estado==1 ) {
			if( strncmp( linea, etiqueta2, n2 ) == 0 ) {
				paux1 = linea;
				while ( *paux1 != '=' )	
					paux1++;
				paux1++;
				while ( *paux1 == ' ' )	
					paux1++;
	
				paux2 = linea + strlen( linea );
				while ( *paux2 == '\n' || *paux2 == '\0'  )	
					*paux2-- = '\0';

				val[1] = strtod( paux1, (char **)NULL);
				estado = 2;
			}
		}
		else if ( estado==2 ) {
			if( strncmp( linea, etiqueta3, n3 ) == 0 ) {
				paux1 = linea;
				while ( *paux1 != '=' )	
					paux1++;
				paux1++;
				while ( *paux1 == ' ' )	
					paux1++;
	
				paux2 = linea + strlen( linea );
				while ( *paux2 == '\n' || *paux2 == '\0'  )	
					*paux2-- = '\0';

				val[2] = strtod( paux1, (char **)NULL);
				estado = 3;
			}
		}
		else if ( estado==3 ) {
			if( strncmp( linea, etiqueta4, n4 ) == 0 ) {
				paux1 = linea;
				while ( *paux1 != '=' )	
					paux1++;
				paux1++;
				while ( *paux1 == ' ' )	
					paux1++;
	
				paux2 = linea + strlen( linea );
				while ( *paux2 == '\n' || *paux2 == '\0'  )	
					*paux2-- = '\0';

				val[3] = strtod( paux1, (char **)NULL);
				estado = 4;
				break;
			}
		}
	}
	fclose( parch );
	if ( estado != 4 ) return -1;
	return 0;
}

typedef struct datos {
	double Ao;
	double bw;
	double ugf;
	double fase;
	double gm;
	double error;
	double vout;
} DATOS;

void cascodeOTA(int n, individual *ind)
{
	#define NPARAM 5
	#define RESTRICCIONES 15
	DATOS da;
	// float x[NPARAM];
	int x[7];
	int i, j, c;
	double val[4], constr[21];

	/**
	for( i=0; i<NPARAM; i++ )
		x[i] = floor(ind->xreal[i]);
	x[0] = x[1] =  2.0;
	**/

	for( i=0; i<NPARAM; i++ ){
		x[i] = floor(ind->xreal[i] + 0.5);
		// ind->xreal[i] = x[i];
	}
	x[5] = 20;
	x[6] = 15;

	haceArchivo( "wsvals.lib", x, NPARAM );

	ejecutaNgspice( );

	if ( checaSaturacion( "cir1.lis", constr, RESTRICCIONES+2 ) == 0 ) { 
		/**
		da.vout = analiza( "m1.lis", "v(out)" );
		printf("Saturación:\n");
		for( i=0; i<12; i++ )
			printf("%d ", (int)constr[i] );
		printf("\n");
		**/
		for( i=0, j=0; i<RESTRICCIONES+2; i++, j++ ) {
			/** No tomamos en cuenta los transistores M11 y M12 **/
			if ( i==3 )
				i++;
			if ( i==4 )
				i++;
			ind->constr[j] = constr[i];
		}
	}
	else{
		for( i=0; i<RESTRICCIONES; i++ ) {
			ind->constr[i] = -1;
		}
	}

	if ( analiza3( "cir2.lis", "aodb", "bw", "faseok", val ) == 0 ) {
		da.Ao = val[0];
		// printf("Ao = %lf\n", da.Ao );
		// da.ugf = val[1];
		da.bw = val[1];
		// printf("UGF = %lf\n", da.ugf );
		da.fase = val[2];
		// printf("Phase = %lf\n", da.fase );
	}
	else {
		da.Ao = 0.0;
		da.bw = 0.0;
		da.fase = 0.0;
	}

	/**

	val[0] = val[1] = val[2] = val[3] = 0;
	if( analiza3( "m3.lis", "simetria", "suma", "gm", val ) == 0 ) {
	// if ( analiza4( "m3.lis", "iini", "ifin", "suma", "gm", val ) == 0 ) {
		if( val[0] <= 0.0 ){
			da.error = 100.0;
			da.Ao = -10.0;
			da.bw = -2.0;
			da.gm = 10.0;
			da.fase = 0.0;
		} 
		else {
			// printf("Corrientes %d\n", val[1]>val[0] );
			da.error = val[1];
			// printf("Error = %g\n", da.error );
			da.gm = val[2];
			// printf("gm = %g\n", da.gm );
		}
	}
	else{
		da.error = 100.0;
		da.gm = 10.0;
	}
	**/

	if( da.fase > 60.0 ) 
		ind->constr[RESTRICCIONES] = 1.0;
	else
		ind->constr[RESTRICCIONES] = -1.0;

	/**
	if ( da.gm < 0.33 )  
		ind->constr[RESTRICCIONES+1] = 1.0;
	else
		ind->constr[RESTRICCIONES+1] = -1.0;

	if ( da.gm > 0.30  )  
		ind->constr[RESTRICCIONES+2] = 1.0;
	else
		ind->constr[RESTRICCIONES+2] = -1.0;
	**/

	for( c=0, i=0; i<=RESTRICCIONES; i++ ) {
		if( ind->constr[i] < 0 ) c--;
	}
	ind->constr_violation = c;

	ind->obj[0] = -da.Ao;
	ind->obj[1] = -da.bw;
	// ind->obj[2] = da.error;
	// ind->obj[3] = fabs(da.vout);
}


/* Routine to evaluate objective function values and constraints for a population */
void evaluate_pop (population *pop)
{
	int i;
	for (i=0; i<popsize; i++) {
		cascodeOTA (i, &(pop->ind[i]));
	}
}

