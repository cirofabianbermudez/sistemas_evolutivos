#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <unistd.h>

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
	char *argv1[6] = { "/opt/local/bin/ngspice", "-b", "-o", "", "", NULL };

	argv1[3] = "cir1.lis";
	argv1[4] = "cir1.sp";
	evalua_circuito( argv1 );

	argv1[3] = "cir2.lis";
	argv1[4] = "cir2.sp";
	evalua_circuito( argv1 );
}


void checaSaturacion( char *nombreArchivo, double *sat, int ntran )
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
		exit(-3);
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
			exit(-2);
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

void analiza3( char *nombre, char *etiqueta1, char *etiqueta2, char *etiqueta3, double val[] )
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
			exit(-2);
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
}

typedef struct datos {
	double Ao;
	double ugf;
	double bw;
	double fase;
	double gm;
	double error;
} DATOS;

int main( int argc, char*argv[] )
{
	#define NPARAM 7
	DATOS da;
	int x[NPARAM];
	int i, j;
	double val[4], constr[17];
	double vout;

	if( argc != 8 ){
		fprintf( stderr, "Args: w1 w2 w3 w4 w5 w6 w7\n" );
		return(-1);
	}
	for( i=0; i<NPARAM; i++ )
		x[i] = (int)strtol( argv[i+1], (char **)NULL, 10);


	haceArchivo( "wsvals.lib", x, NPARAM );

	ejecutaNgspice( );

	checaSaturacion( "cir1.lis", constr, 17 );
	printf("Saturación:\n");
	for( i=0; i<17; i++ ){
		if ( i==3 )
			i++;
		if ( i==4 )
			i++;
		printf("%d ", (int)constr[i] );
	}
	printf("\n");
	vout = analiza( "cir1.lis", "v(out)" );
	printf("vout = %lf\n", vout );
	

	analiza3( "cir2.lis", "aodb", "bw", "faseok", val );
	da.Ao = val[0];
	printf("Ao = %lf\n", da.Ao );
	da.bw = val[1];
	// printf("UGF = %lf\n", da.ugf );
	printf("BW = %lf\n", da.bw );
	da.fase = val[2];
	printf("Phase = %lf\n", da.fase );

	return( 0 );
}

