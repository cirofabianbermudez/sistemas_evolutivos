# Se código fuente del NSGA-II
#
# m número de objetivos
# a y b, dos soluciones
def dominancia( m, a, b ) :
	flag1 = 0 
	flag2 = 0 
	i = 0
	while i < m :
		if a[i] < b[i] :
			flag1 = 1
		elif a[i] > b[i] :
			flag2 = 1
		i += 1

	if flag1==1 and flag2==0 :
		return 1
	elif flag1==0 and flag2==1 :
		return -1
	else :
		return 0
 
